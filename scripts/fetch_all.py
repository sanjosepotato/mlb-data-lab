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

    # チーム略称の正規化マップ（正式名 → 略称）
    TEAM_ABBR_MAP = {
        "Arizona Diamondbacks":"ARI","Atlanta Braves":"ATL","Baltimore Orioles":"BAL",
        "Boston Red Sox":"BOS","Chicago Cubs":"CHC","Chicago White Sox":"CWS",
        "Cincinnati Reds":"CIN","Cleveland Guardians":"CLE","Colorado Rockies":"COL",
        "Detroit Tigers":"DET","Houston Astros":"HOU","Kansas City Royals":"KC",
        "Los Angeles Angels":"LAA","Los Angeles Dodgers":"LAD","Miami Marlins":"MIA",
        "Milwaukee Brewers":"MIL","Minnesota Twins":"MIN","New York Mets":"NYM",
        "New York Yankees":"NYY","Oakland Athletics":"OAK","Philadelphia Phillies":"PHI",
        "Pittsburgh Pirates":"PIT","San Diego Padres":"SD","San Francisco Giants":"SFG",
        "Seattle Mariners":"SEA","St. Louis Cardinals":"STL","Tampa Bay Rays":"TB",
        "Texas Rangers":"TEX","Toronto Blue Jays":"TOR","Washington Nationals":"WSH",
        "Athletics":"OAK",
    }

    def normalize_team(team_info):
        abbr = team_info.get("abbreviation", "")
        if abbr: return abbr
        name = team_info.get("name", "")
        return TEAM_ABBR_MAP.get(name, team_info.get("teamCode", "???").upper())

    for league_id, league_key in [(AL_ID, "AL"), (NL_ID, "NL")]:
        d = get(
            f"/stats?stats=season&group=hitting&season={season}"
            f"&sportId=1&limit=10&sortStat=homeRuns"
            f"&leagueId={league_id}"
        )
        if d and d.get("stats"):
            for s in d["stats"][0].get("splits", []):
                out["hrLeaders"][league_key].append({
                    "id":   s["player"]["id"],
                    "name": s["player"]["fullName"],
                    "team": normalize_team(s.get("team", {})),
                    "hr":   s["stat"]["homeRuns"],
                    "avg":  s["stat"].get("avg", ".000"),
                    "ops":  s["stat"].get("ops", ".000"),
                })
        print(f"    {league_key}: {len(out['hrLeaders'][league_key])} players")

    # 日本人野手を強制追加（圏外でも必ずペース換算に表示）
    # hrLeadersには混ぜず、別フィールド jpHitters として保存
    JP_HITTER_IDS = {
        660271: {"name": "Shohei Ohtani",     "team": "LAD", "league": "NL"},
        673548: {"name": "Seiya Suzuki",       "team": "CHC", "league": "NL"},
        807799: {"name": "Masataka Yoshida",   "team": "BOS", "league": "AL"},
        808959: {"name": "Munetaka Murakami",  "team": "CWS", "league": "AL"},
        672960: {"name": "Kazuma Okamoto",     "team": "TOR", "league": "AL"},
    }
    existing_ids = {p["id"] for p in out["hrLeaders"]["AL"] + out["hrLeaders"]["NL"]}
    out["jpHitters"] = []
    for pid, info in JP_HITTER_IDS.items():
        dj = get(f"/people/{pid}/stats?stats=season&group=hitting&season={season}")
        hr_val = 0
        avg_val = ".000"
        ops_val = ".000"
        if dj and dj.get("stats"):
            splits = dj["stats"][0].get("splits", [])
            if splits:
                st = splits[0]["stat"]
                hr_val  = int(st.get("homeRuns", 0) or 0)
                avg_val = st.get("avg", ".000")
                ops_val = st.get("ops", ".000")
        in_ranking = pid in existing_ids
        out["jpHitters"].append({
            "id": pid, "name": info["name"], "team": info["team"],
            "league": info["league"], "hr": hr_val,
            "avg": avg_val, "ops": ops_val,
            "inRanking": in_ranking,  # hrLeadersに入っているかどうか
        })
        status = "ランキング内" if in_ranking else "ランク外"
        print(f"    JP野手: {info['name']} {hr_val}HR ({status})")

    # 合算（HR降順 TOP15）- 日本人は含まない純粋なランキング
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

    # ④ サイヤング候補（AL/NL 別 上位7名 + 注目選手 + 日本人投手強制追加）
    print("  Fetching Cy Young candidates (AL/NL)...")
    out["cyYoung"] = {"AL": [], "NL": []}

    JP_PITCHER_IDS = {
        817202: {"name": "Yoshinobu Yamamoto", "team": "LAD", "league": "NL"},
        681911: {"name": "Shota Imanaga",      "team": "CHC", "league": "NL"},
        660271: {"name": "Shohei Ohtani",      "team": "LAD", "league": "NL"},
        808967: {"name": "Roki Sasaki",        "team": "LAD", "league": "NL"},
        608372: {"name": "Kodai Senga",        "team": "COL", "league": "NL"},
    }
    # 注目選手（規定投球回未達でも表示したい選手）
    NOTABLE_PITCHER_IDS = {
        694973: {"name": "Paul Skenes",   "team": "PIT", "league": "NL"},
        592789: {"name": "Gerrit Cole",   "team": "NYY", "league": "AL"},
        477132: {"name": "Zack Wheeler",  "team": "PHI", "league": "NL"},
        543037: {"name": "Corbin Burnes", "team": "BAL", "league": "AL"},
    }
    MIN_IP = 40.0  # シーズン序盤は低めに設定

    def calc_qs(pid, season):
        """gameLogからQS（6回以上・自責3以下）を計算して割合(%)を返す"""
        gl = get(f"/people/{pid}/stats?stats=gameLog&group=pitching&season={season}&gameType=R")
        if not gl or not gl.get("stats"):
            return 0
        splits = gl["stats"][0].get("splits", [])
        gs = [s for s in splits if int(s["stat"].get("gamesStarted", 0)) > 0]
        if not gs:
            return 0
        qs_count = 0
        for s in gs:
            st  = s["stat"]
            ip  = float(st.get("inningsPitched", 0) or 0)
            er  = int(st.get("earnedRuns", 0) or 0)
            if ip >= 6.0 and er <= 3:
                qs_count += 1
        return round(qs_count / len(gs) * 100) if gs else 0

    def build_pitcher_entry(pid, s, is_jp=False, compute_qs=False):
        st        = s["stat"]
        team_info = s.get("team", {})
        ip_raw    = float(st.get("inningsPitched", 0) or 0)
        so_val    = int(st.get("strikeOuts", 0) or 0)
        bb_val    = int(st.get("baseOnBalls", 0) or 0)
        qs_val    = calc_qs(pid, season) if compute_qs else 0
        return {
            "id":   pid,
            "name": s["player"]["fullName"],
            "team": normalize_team(team_info),
            "isJP": is_jp,
            "w":    int(st.get("wins", 0) or 0),
            "era":  float(st.get("era", 0) or 0),
            "so":   so_val,
            "whip": float(st.get("whip", 0) or 0),
            "ip":   ip_raw,
            "k9":   round(so_val / ip_raw * 9, 1) if ip_raw > 0 else 0.0,
            "bb9":  round(bb_val / ip_raw * 9, 1) if ip_raw > 0 else 0.0,
            "kbb":  round(so_val / bb_val, 1)     if bb_val > 0 else 0.0,
            "fip":  0.0,   # Stats APIでは取得不可
            "war":  0.0,   # Stats APIでは取得不可
            "qs":   qs_val,
        }

    for league_id, league_key in [(AL_ID, "AL"), (NL_ID, "NL")]:
        # qualifyingOnly=false + limit=50 で多めに取得し、IP/ERA条件でフィルタ
        d = get(
            f"/stats?stats=season&group=pitching&season={season}"
            f"&sportId=1&limit=50&sortStat=era&qualifyingOnly=false"
            f"&leagueId={league_id}"
        )
        if d and d.get("stats"):
            for s in d["stats"][0].get("splits", []):
                pid    = s["player"]["id"]
                ip_raw = float(s["stat"].get("inningsPitched", 0) or 0)
                era    = float(s["stat"].get("era", 99) or 99)
                is_jp  = pid in JP_PITCHER_IDS
                # IP不足 or ERA異常値（リリーフ投手混入対策）をスキップ
                if ip_raw < MIN_IP or era >= 9.00:
                    continue
                if len(out["cyYoung"][league_key]) >= 7:
                    break
                entry = build_pitcher_entry(pid, s, is_jp, compute_qs=True)
                out["cyYoung"][league_key].append(entry)
        print(f"    cyYoung {league_key}: {len(out['cyYoung'][league_key])} players")

    # 注目選手（Paul Skenes等）を強制追加
    cy_existing = {p["id"] for v in out["cyYoung"].values() for p in v}
    for pid, info in NOTABLE_PITCHER_IDS.items():
        if pid in cy_existing:
            continue
        dj = get(f"/people/{pid}/stats?stats=season&group=pitching&season={season}")
        if not dj or not dj.get("stats"):
            continue
        splits = dj["stats"][0].get("splits", [])
        if not splits:
            continue
        ip_raw = float(splits[0].get("stat", {}).get("inningsPitched", 0) or 0)
        if ip_raw < MIN_IP:
            print(f"    注目選手スキップ(IP不足): {info['name']} IP={ip_raw}")
            continue
        s_fake = {
            "player": {"id": pid, "fullName": info["name"]},
            "team":   {"abbreviation": info["team"]},
            "stat":   splits[0].get("stat", {}),
        }
        entry = build_pitcher_entry(pid, s_fake, is_jp=False, compute_qs=True)
        out["cyYoung"][info["league"]].append(entry)
        print(f"    注目選手追加: {info['name']} ERA={entry['era']} IP={entry['ip']} QS={entry['qs']}%")

    # 日本人投手を強制追加（規定未達でも表示）
    cy_existing = {p["id"] for v in out["cyYoung"].values() for p in v}
    for pid, info in JP_PITCHER_IDS.items():
        if pid in cy_existing:
            continue
        dj = get(f"/people/{pid}/stats?stats=season&group=pitching&season={season}")
        if not dj or not dj.get("stats"):
            continue
        splits = dj["stats"][0].get("splits", [])
        if not splits:
            continue
        s_fake = {
            "player": {"id": pid, "fullName": info["name"]},
            "team":   {"abbreviation": info["team"]},
            "stat":   splits[0].get("stat", {}),
        }
        entry = build_pitcher_entry(pid, s_fake, is_jp=True, compute_qs=True)
        out["cyYoung"][info["league"]].append(entry)
        print(f"    JP投手追加: {info['name']} ERA={entry['era']} IP={entry['ip']} QS={entry['qs']}%")

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

    # ⑦ チーム別消化試合数（全30球団）+ ヒートマップ用詳細（主要6チーム）
    # teamGamesは消化試合数（整数）を全球団分保存する
    print("  Fetching team games...")
    td = get(f"/teams?sportId=1&season={season}")
    team_id_map = {}
    if td:
        for t in td.get("teams", []):
            abbr = t.get("abbreviation", "")
            if abbr:
                team_id_map[abbr] = t["id"]

    out["teamGames"] = {}
    # standings から全チームの消化試合数を取得（APIコール1回で済む）
    st_data = get(f"/standings?leagueId=103,104&season={season}&standingsType=regularSeason")
    if st_data and st_data.get("records"):
        for div in st_data["records"]:
            for t in div["teamRecords"]:
                abbr = t["team"].get("abbreviation", "")
                if abbr:
                    out["teamGames"][abbr] = t.get("wins", 0) + t.get("losses", 0)
    print(f"    teamGames: {len(out['teamGames'])} teams")

    # ヒートマップ用詳細データ（主要6チームのみ・試合結果リスト）
    HEATMAP_TEAMS = ["LAD", "NYY", "CHC", "BOS", "HOU", "ATL"]
    out["teamGameDetails"] = {}
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
        out["teamGameDetails"][abbr] = games
        print(f"    {abbr}: {len(games)} games")

    # ⑧ HR累積推移（combined TOP10 の日別累積 HR）
    # キーを選手ID（数値）にしてHTMLから引きやすくする
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
        # キーをID文字列にする（JSONはオブジェクトキーが文字列のみ）
        out["hrProgression"][str(pid)] = {
            "name": player["name"],
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
