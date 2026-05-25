import json, requests
from datetime import datetime, timezone, timedelta

API = "https://statsapi.mlb.com/api/v1"
JST = timezone(timedelta(hours=9))

def get(path):
    try:
        r = requests.get(API + path, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  warn: {path} -> {e}")
        return None

# ── リーグ・ディビジョンID定義 ──
AL_ID = 103
NL_ID = 104

# サイヤング候補の評価に使う指標キー（MLB Stats API → 独自キー）
CY_STAT_MAP = {
    "wins":           "w",
    "era":            "era",
    "strikeOuts":     "so",
    "whip":           "whip",
    "inningsPitched": "ip",
}

def main():
    season = datetime.now().year if datetime.now().month >= 3 else datetime.now().year - 1
    updated = datetime.now(JST).strftime("%Y年%m月%d日 %H:%M JST")
    print(f"=== Fetching {season} season ({updated}) ===")
    out = {"season": season, "updatedAt": updated}

    # ① 本日のスコア
    today = datetime.now(JST).strftime("%Y-%m-%d")
    d = get(f"/schedule?sportId=1&date={today}&hydrate=team,linescore")
    out["scores"] = d["dates"][0]["games"] if d and d.get("dates") else []
    print(f"  scores: {len(out['scores'])} games")

    # ② HR ランキング（AL/NL 分け + 合算 TOP15）
    #    leagueId を指定して AL / NL 別に取得する
    print("  Fetching HR leaders (AL/NL)...")
    out["hrLeaders"] = {"AL": [], "NL": [], "combined": []}

    for league_id, league_key in [(AL_ID, "AL"), (NL_ID, "NL")]:
        d = get(
            f"/stats?stats=season&group=hitting&season={season}"
            f"&sportId=1&limit=10&sortStat=homeRuns"
            f"&leagueId={league_id}"
        )
        if d and d.get("stats"):
            for s in d["stats"][0].get("splits", []):
                team_info = s.get("team", {})
                out["hrLeaders"][league_key].append({
                    "id":   s["player"]["id"],
                    "name": s["player"]["fullName"],
                    "team": (team_info.get("abbreviation")
                             or team_info.get("teamCode")
                             or team_info.get("name", "???")),
                    "hr":   s["stat"]["homeRuns"],
                    "avg":  s["stat"].get("avg", ".000"),
                    "ops":  s["stat"].get("ops", ".000"),
                })
        print(f"    {league_key}: {len(out['hrLeaders'][league_key])} players")

    # 合算（ALとNLをマージしてHR降順 TOP15）
    combined = out["hrLeaders"]["AL"] + out["hrLeaders"]["NL"]
    out["hrLeaders"]["combined"] = sorted(combined, key=lambda x: x["hr"], reverse=True)[:15]
    print(f"    combined: {len(out['hrLeaders']['combined'])} players")

    # ③ 先発投手リーダー（全体）
    d = get(
        f"/stats?stats=season&group=pitching&season={season}"
        f"&sportId=1&limit=30&sortStat=era&qualifyingOnly=true"
    )
    out["pitchers"] = []
    if d and d.get("stats"):
        for s in d["stats"][0].get("splits", []):
            st = s["stat"]
            team_info = s.get("team", {})
            ip = float(st.get("inningsPitched", 0) or 0)
            so = int(st.get("strikeOuts", 0) or 0)
            out["pitchers"].append({
                "name": s["player"]["fullName"],
                "team": (team_info.get("abbreviation")
                         or team_info.get("teamCode")
                         or team_info.get("name", "???")),
                "era":  float(st.get("era", 0)),
                "whip": float(st.get("whip", 0)),
                "k9":   round(so / ip * 9, 1) if ip > 0 else 0,
                "ip":   ip,
                "so":   so,
            })
    print(f"  pitchers: {len(out['pitchers'])} players")

    # ④ サイヤング候補（AL/NL 別 上位7名）
    #    FIP・WAR・K/BB・BB9・QS は Stats API 単体では取れないため
    #    取得できる指標（ERA/WHIP/W/SO/IP/K9）だけ入れ、
    #    FIP/WAR/K/BB/QS はフロントで 0 をフォールバックにする
    print("  Fetching Cy Young candidates (AL/NL)...")
    out["cyYoung"] = {"AL": [], "NL": []}

    for league_id, league_key in [(AL_ID, "AL"), (NL_ID, "NL")]:
        d = get(
            f"/stats?stats=season&group=pitching&season={season}"
            f"&sportId=1&limit=7&sortStat=era&qualifyingOnly=true"
            f"&leagueId={league_id}"
        )
        if d and d.get("stats"):
            for s in d["stats"][0].get("splits", []):
                pid       = s["player"]["id"]
                st        = s["stat"]
                team_info = s.get("team", {})
                ip_raw    = float(st.get("inningsPitched", 0) or 0)
                so_val    = int(st.get("strikeOuts", 0) or 0)
                bb_val    = int(st.get("baseOnBalls", 0) or 0)
                gs_val    = int(st.get("gamesStarted", 0) or 0)
                # QS は Stats API に存在しないので 0（将来的に補完）
                # FIP / WAR も同様
                k9_val    = round(so_val / ip_raw * 9, 1) if ip_raw > 0 else 0.0
                bb9_val   = round(bb_val / ip_raw * 9, 1) if ip_raw > 0 else 0.0
                kbb_val   = round(so_val / bb_val, 1) if bb_val > 0 else 0.0

                # 日本人選手判定
                JP_IDS = {660271, 681911, 817202, 808967, 608372}
                is_jp   = pid in JP_IDS

                out["cyYoung"][league_key].append({
                    "id":   pid,
                    "name": s["player"]["fullName"],
                    "team": (team_info.get("abbreviation")
                             or team_info.get("teamCode")
                             or team_info.get("name", "???")),
                    "isJP": is_jp,
                    # Stats API から取れる指標
                    "w":    int(st.get("wins", 0) or 0),
                    "era":  float(st.get("era", 0) or 0),
                    "so":   so_val,
                    "whip": float(st.get("whip", 0) or 0),
                    "ip":   ip_raw,
                    "k9":   k9_val,
                    "bb9":  bb9_val,
                    "kbb":  kbb_val,
                    # Stats API では取得困難 → 0 フォールバック
                    # フロント側で「データなし」表示を推奨
                    "fip":  0.0,
                    "war":  0.0,
                    "qs":   0,
                })
        print(f"    cyYoung {league_key}: {len(out['cyYoung'][league_key])} players")

    # ⑤ 日本人選手スタッツ
    JP_IDS = {
        660271: {"nameJa": "大谷 翔平",   "team": "LAD", "type": "hitter"},
        673548: {"nameJa": "鈴木 誠也",   "team": "CHC", "type": "hitter"},
        807799: {"nameJa": "吉田 正尚",   "team": "BOS", "type": "hitter"},
        681911: {"nameJa": "今永 昇太",   "team": "CHC", "type": "pitcher"},
        817202: {"nameJa": "山本 由伸",   "team": "LAD", "type": "pitcher"},
        808967: {"nameJa": "佐々木 朗希", "team": "LAD", "type": "pitcher"},
        808959: {"nameJa": "村上 宗隆",   "team": "CWS", "type": "hitter"},
        672960: {"nameJa": "岡本 和真",   "team": "TOR", "type": "hitter"},
        608372: {"nameJa": "菅野 智之",   "team": "COL", "type": "pitcher"},
    }
    out["jpPlayers"] = []
    for pid, info in JP_IDS.items():
        group = "hitting" if info["type"] == "hitter" else "pitching"
        d = get(f"/people/{pid}/stats?stats=season&group={group}&season={season}")
        stats = {}
        if d and d.get("stats"):
            splits = d["stats"][0].get("splits", [])
            if splits:
                stats = splits[0].get("stat", {})
        out["jpPlayers"].append({**info, "id": pid, "stats": stats})
        print(f"    {info['nameJa']}: OK")

    # ⑥ 順位表
    d = get(f"/standings?leagueId=103,104&season={season}&standingsType=regularSeason")
    out["standings"] = []
    if d and d.get("records"):
        for div in d["records"]:
            teams = []
            for t in div["teamRecords"]:
                team_info = t.get("team", {})
                teams.append({
                    "abbr": team_info.get("abbreviation", team_info.get("teamCode", "???")),
                    "name": team_info.get("teamName", team_info.get("name", "Unknown")),
                    "w":    t.get("wins", 0),
                    "l":    t.get("losses", 0),
                    "pct":  t.get("winningPercentage", 0),
                    "gb":   t.get("gamesBack", "-"),
                })
            out["standings"].append({
                "divId":   div["division"].get("id", 0),
                "divName": div["division"].get("name", div["division"].get("nameShort", "Unknown")),
                "teams":   sorted(teams, key=lambda x: -float(x["pct"] or 0)),
            })
    print(f"  standings: {len(out['standings'])} divisions")

    # ⑦ チーム別試合結果（ヒートマップ用）
    HEATMAP_TEAMS = ["LAD", "NYY", "CHC", "BOS", "HOU", "ATL"]
    out["teamGames"] = {}
    td = get(f"/teams?sportId=1&season={season}")
    team_id_map = {}
    if td:
        for t in td.get("teams", []):
            team_id_map[t["abbreviation"]] = t["id"]
    for abbr in HEATMAP_TEAMS:
        team_id = team_id_map.get(abbr)
        games = []
        if team_id:
            sd = get(
                f"/schedule?sportId=1&season={season}&teamId={team_id}"
                f"&gameType=R&hydrate=team,linescore"
            )
            if sd and sd.get("dates"):
                for date in sd["dates"]:
                    for g in date["games"]:
                        if g["status"]["detailedState"] == "Final":
                            home = g["teams"]["home"]
                            away = g["teams"]["away"]
                            is_home = home["team"]["abbreviation"] == abbr
                            my  = home if is_home else away
                            opp = away if is_home else home
                            games.append({
                                "date":  date["date"],
                                "win":   my["score"] > opp["score"],
                                "score": f"{my['score']}-{opp['score']}",
                                "opp":   opp["team"]["abbreviation"],
                            })
        out["teamGames"][abbr] = games
        print(f"    {abbr}: {len(games)} games")

    # ⑧ HR累積推移（combined TOP10 の日別累積 HR）
    print("  Fetching HR progression...")
    out["hrProgression"] = {}
    for player in out["hrLeaders"]["combined"][:10]:
        pid = player.get("id")
        if not pid:
            continue
        gl = get(
            f"/people/{pid}/stats?stats=gameLog"
            f"&group=hitting&season={season}&gameType=R"
        )
        if not gl or not gl.get("stats"):
            continue
        splits = gl["stats"][0].get("splits", [])
        cumulative = 0
        progression = []
        for game in splits:
            hr_today = int(game["stat"].get("homeRuns", 0))
            cumulative += hr_today
            progression.append({
                "date": game.get("date", ""),
                "hr":   cumulative,
            })
        out["hrProgression"][player["name"]] = {
            "team": player["team"],
            "data": progression,
        }
        print(f"    {player['name']}: {len(progression)} games, {cumulative} HR")
    print(f"  hrProgression: {len(out['hrProgression'])} players")

    # ⑨ HR飛距離（Baseball Savant）※ Bot対策でブロックされる場合は空配列
    print("  Fetching HR distance data (Statcast)...")
    out["hrDistance"] = []
    try:
        import csv, io
        savant_url = (
            f"https://baseballsavant.mlb.com/statcast_search/csv"
            f"?hfAB=home+run%7C&hfGT=R%7C&hfSea={season}%7C"
            f"&player_type=batter&sort_col=hit_distance_sc&sort_order=desc"
            f"&min_results=0&type=details"
            f"&chk_stats_hit_distance_sc=on&chk_stats_launch_speed=on&chk_stats_launch_angle=on"
        )
        headers = {"User-Agent": "Mozilla/5.0 (compatible; mlb-data-lab/1.0)"}
        r = requests.get(savant_url, timeout=30, headers=headers)
        r.raise_for_status()
        reader = csv.DictReader(io.StringIO(r.text))
        rows = [
            row for row in reader
            if row.get("hit_distance_sc", "").strip().lstrip("-").isdigit()
            and float(row["hit_distance_sc"]) > 300
        ]
        for row in sorted(rows, key=lambda x: float(x["hit_distance_sc"]), reverse=True)[:10]:
            name = row.get("player_name", "")
            if "," in name:
                parts = name.split(", ")
                name = f"{parts[1].strip()} {parts[0].strip()}"
            out["hrDistance"].append({
                "name":  name,
                "team":  row.get("batter_team") or row.get("home_team", "???"),
                "dist":  round(float(row["hit_distance_sc"])),
                "ev":    round(float(row.get("launch_speed", 0) or 0), 1),
                "angle": round(float(row.get("launch_angle", 0) or 0), 1),
                "date":  row.get("game_date", ""),
            })
    except Exception as e:
        print(f"  warn: hrDistance -> {e}")
    print(f"  hrDistance: {len(out['hrDistance'])} records")

    # 保存
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Saved data.json ({len(json.dumps(out)) // 1024}KB)")

if __name__ == "__main__":
    main()
