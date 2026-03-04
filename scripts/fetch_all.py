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

    # ② HR ランキング TOP15
    d = get(f"/stats?stats=season&group=hitting&season={season}&sportId=1&limit=15&sortStat=homeRuns")
    out["hrLeaders"] = []
    if d and d.get("stats"):
        for s in d["stats"][0].get("splits", []):
            out["hrLeaders"].append({
                "name": s["player"]["fullName"],
                "team": s["team"]["abbreviation"],
                "hr":   s["stat"]["homeRuns"],
                "avg":  s["stat"].get("avg", ".000"),
            })
    print(f"  hrLeaders: {len(out['hrLeaders'])} players")

    # ③ 先発投手リーダー
    d = get(f"/stats?stats=season&group=pitching&season={season}&sportId=1&limit=30&sortStat=era&qualifyingOnly=true")
    out["pitchers"] = []
    if d and d.get("stats"):
        for s in d["stats"][0].get("splits", []):
            st = s["stat"]
            ip = float(st.get("inningsPitched", 0) or 0)
            so = int(st.get("strikeOuts", 0) or 0)
            out["pitchers"].append({
                "name": s["player"]["fullName"],
                "team": s["team"]["abbreviation"],
                "era":  float(st.get("era", 0)),
                "whip": float(st.get("whip", 0)),
                "k9":   round(so / ip * 9, 1) if ip > 0 else 0,
                "ip":   ip,
                "so":   so,
            })
    print(f"  pitchers: {len(out['pitchers'])} players")

    # ④ 日本人選手スタッツ
    JP_IDS = {
        660271: {"nameJa": "大谷 翔平",  "team": "LAD", "type": "hitter"},
        673548: {"nameJa": "鈴木 誠也",  "team": "CHC", "type": "hitter"},
        807799: {"nameJa": "吉田 正尚",  "team": "BOS", "type": "hitter"},
        681911: {"nameJa": "今永 昇太",  "team": "CHC", "type": "pitcher"},
        817202: {"nameJa": "山本 由伸",  "team": "LAD", "type": "pitcher"},
        808967: {"nameJa": "佐々木 朗希","team": "LAD", "type": "pitcher"},
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

    # ⑤ 順位表
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
                "divId":   div["division"]["id"],
                "divName": div["division"]["name"],
                "teams":   sorted(teams, key=lambda x: -float(x["pct"] or 0)),
            })
    print(f"  standings: {len(out['standings'])} divisions")

    # ⑥ チーム別試合結果（ヒートマップ用）
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
            sd = get(f"/schedule?sportId=1&season={season}&teamId={team_id}&gameType=R&hydrate=team,linescore")
            if sd and sd.get("dates"):
                for date in sd["dates"]:
                    for g in date["games"]:
                        if g["status"]["detailedState"] == "Final":
                            home = g["teams"]["home"]
                            away = g["teams"]["away"]
                            is_home = home["team"]["abbreviation"] == abbr
                            my = home if is_home else away
                            opp = away if is_home else home
                            games.append({
                                "date": date["date"],
                                "win":  my["score"] > opp["score"],
                                "score": f"{my['score']}-{opp['score']}",
                                "opp":  opp["team"]["abbreviation"],
                            })
        out["teamGames"][abbr] = games
        print(f"    {abbr}: {len(games)} games")

    # 保存
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Saved data.json ({len(json.dumps(out)) // 1024}KB)")

if __name__ == "__main__":
    main()
