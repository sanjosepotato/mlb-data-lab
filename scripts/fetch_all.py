<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>サイヤング賞争い 2026 | サンノゼポテト</title>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2592831002858501" crossorigin="anonymous"></script>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+JP:wght@400;500;700;900&family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:        #f8f7f4;
    --surface:   #ffffff;
    --surface2:  #fafaf8;
    --border:    #e8e4dc;
    --border2:   #d4cfc5;
    --red:       #c8102e;
    --red-light: #fff0f2;
    --jp:        #0057a8;
    --jp-light:  #e8f0fa;
    --text:      #1a1a1a;
    --text2:     #4a4a4a;
    --muted:     #8a8a8a;
    --green:     #1a7a3a;
    --gold:      #b8860b;
  }
  *, *::before, *::after { box-sizing:border-box; margin:0; padding:0; }
  body { background:var(--bg); color:var(--text); font-family:'Noto Sans JP',sans-serif; min-height:100vh; }

  .topbar { background:var(--red); color:#fff; text-align:center; padding:6px 16px; font-family:'Roboto Mono',monospace; font-size:11px; letter-spacing:2px; }

  .hero { background:var(--surface); border-bottom:3px solid var(--red); padding:36px 24px 28px; text-align:center; }
  .hero-eyebrow { font-family:'Roboto Mono',monospace; font-size:11px; letter-spacing:4px; color:var(--red); text-transform:uppercase; margin-bottom:10px; }
  .hero h1 { font-family:'Bebas Neue',sans-serif; font-size:clamp(40px,9vw,88px); letter-spacing:3px; color:var(--text); line-height:1; }
  .hero h1 em { color:var(--red); font-style:normal; }
  .hero-sub { margin-top:10px; font-size:13px; color:var(--muted); font-family:'Roboto Mono',monospace; }
  .hero-sub b { color:var(--green); }

  .tabs { background:var(--surface); border-bottom:1px solid var(--border); display:flex; justify-content:center; position:sticky; top:0; z-index:100; box-shadow:0 2px 8px rgba(0,0,0,.06); overflow-x:auto; }
  .tab-btn { font-family:'Noto Sans JP',sans-serif; font-size:13px; font-weight:500; padding:14px 22px; border:none; border-bottom:3px solid transparent; background:transparent; color:var(--muted); cursor:pointer; transition:all .18s; white-space:nowrap; }
  .tab-btn:hover:not(.active) { color:var(--text); background:var(--bg); }
  .tab-btn.active { color:var(--red); border-bottom-color:var(--red); font-weight:700; }

  .container { max-width:1080px; margin:0 auto; padding:28px 20px 80px; }
  .tab-panel { display:none; }
  .tab-panel.active { display:block; }

  .card { background:var(--surface); border:1px solid var(--border); border-radius:4px; overflow:hidden; margin-bottom:20px; box-shadow:0 1px 4px rgba(0,0,0,.04); }
  .card-header { display:flex; align-items:center; justify-content:space-between; padding:14px 20px; border-bottom:1px solid var(--border); background:var(--surface2); }
  .card-title { font-size:12px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--text2); font-family:'Roboto Mono',monospace; }
  .league-badge { font-family:'Bebas Neue',sans-serif; font-size:22px; letter-spacing:2px; color:var(--red); background:var(--red-light); padding:2px 12px; border-radius:2px; }

  /* ── スコアバナー ── */
  .score-banner {
    display:grid;
    grid-template-columns:56px 1fr auto;
    align-items:center;
    gap:16px;
    padding:18px 20px;
    background:var(--surface);
    border-bottom:2px solid var(--border);
    position:relative;
    overflow:hidden;
  }
  .score-banner::before {
    content:'';
    position:absolute; left:0; top:0; bottom:0; width:4px;
    background:var(--border2);
  }
  .score-banner:nth-child(1)::before { background:var(--gold); }
  .score-banner:nth-child(2)::before { background:#888; }
  .score-banner:nth-child(3)::before { background:#a0522d; }
  .score-banner.jp { background:var(--jp-light); }
  .score-banner.jp::before { background:var(--jp) !important; }

  .score-rank { font-family:'Bebas Neue',sans-serif; font-size:32px; color:var(--border2); text-align:center; line-height:1; }
  .score-banner:nth-child(1) .score-rank { color:var(--gold); font-size:38px; }
  .score-banner:nth-child(2) .score-rank { color:#888; font-size:34px; }
  .score-banner:nth-child(3) .score-rank { color:#a0522d; font-size:34px; }

  .score-info {}
  .score-name-ja { font-size:16px; font-weight:900; color:var(--text); line-height:1.2; }
  .score-banner.jp .score-name-ja { color:var(--jp); }
  .score-name-en { font-size:11px; color:var(--muted); font-family:'Roboto Mono',monospace; margin-top:2px; }
  .score-team { font-size:11px; color:var(--muted); font-family:'Roboto Mono',monospace; margin-top:3px; }
  .score-team .ja { color:var(--text2); font-family:'Noto Sans JP',sans-serif; }
  .jp-badge { display:inline-block; font-size:9px; font-family:'Roboto Mono',monospace; color:var(--jp); border:1px solid var(--jp); padding:1px 5px; border-radius:2px; margin-left:6px; letter-spacing:1px; vertical-align:middle; }

  /* スコアメーター */
  .score-meter { text-align:right; min-width:120px; }
  .score-num { font-family:'Bebas Neue',sans-serif; font-size:42px; color:var(--text); line-height:1; }
  .score-banner:nth-child(1) .score-num { color:var(--red); font-size:50px; }
  .score-banner.jp .score-num { color:var(--jp); }
  .score-label { font-family:'Roboto Mono',monospace; font-size:9px; letter-spacing:2px; color:var(--muted); margin-bottom:4px; }
  .score-bar-wrap { height:4px; background:var(--border); border-radius:2px; margin-top:5px; overflow:hidden; }
  .score-bar { height:100%; border-radius:2px; transition:width 1.2s ease; background:var(--border2); }
  .score-banner:nth-child(1) .score-bar { background:var(--red); }
  .score-banner.jp .score-bar { background:var(--jp); }

  /* ── 指標チップ ── */
  .stat-area { padding:12px 20px 16px 92px; border-bottom:1px solid var(--border); background:var(--surface2); }
  .score-banner.jp + .stat-area { background:#f0f6ff; }
  .stats-grid { display:flex; flex-wrap:wrap; gap:6px; }

  .stat-chip {
    position:relative;
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:4px;
    padding:7px 10px;
    min-width:64px;
    text-align:center;
    cursor:default;
    transition:border-color .15s, box-shadow .15s;
  }
  .stat-chip:hover { border-color:var(--red); box-shadow:0 2px 8px rgba(200,16,46,.08); z-index:10; }

  .chip-label { font-family:'Roboto Mono',monospace; font-size:9px; letter-spacing:1.5px; color:var(--muted); text-transform:uppercase; margin-bottom:3px; display:flex; align-items:center; justify-content:center; gap:3px; }
  .hint-icon { width:11px; height:11px; background:var(--border2); border-radius:50%; display:inline-flex; align-items:center; justify-content:center; font-size:7px; color:var(--muted); flex-shrink:0; }
  .stat-chip:hover .hint-icon { background:var(--red); color:#fff; }

  .chip-val { font-family:'Bebas Neue',sans-serif; font-size:20px; color:var(--text); line-height:1; }
  .chip-val.great { color:var(--red); font-size:23px; }
  .chip-val.good  { color:var(--green); }

  /* リーグ順位バッジ */
  .chip-rank { font-family:'Roboto Mono',monospace; font-size:9px; margin-top:3px; }
  .chip-rank.r1 { color:var(--gold); font-weight:700; }
  .chip-rank.r2 { color:#888; }
  .chip-rank.r3 { color:#a0522d; }
  .chip-rank.rn { color:var(--muted); }

  /* ── ツールチップ ── */
  .tooltip { display:none; position:absolute; bottom:calc(100% + 8px); left:50%; transform:translateX(-50%); background:var(--text); color:#fff; border-radius:4px; padding:10px 14px; width:220px; font-size:12px; font-family:'Noto Sans JP',sans-serif; line-height:1.6; z-index:999; text-align:left; box-shadow:0 4px 16px rgba(0,0,0,.2); pointer-events:none; }
  .tooltip::after { content:''; position:absolute; top:100%; left:50%; transform:translateX(-50%); border:6px solid transparent; border-top-color:var(--text); }
  .tooltip .tip-label { font-family:'Roboto Mono',monospace; font-size:10px; letter-spacing:1px; color:#aaa; margin-bottom:4px; }
  .tooltip .tip-val { font-weight:700; font-size:13px; margin-bottom:4px; }
  .stat-chip:hover .tooltip { display:block; }

  /* ── 指標解説 ── */
  .glossary-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1px; background:var(--border); }
  .glossary-item { background:var(--surface); padding:20px; }
  .glossary-item.advanced { background:#fffaf8; }
  .g-label { font-family:'Bebas Neue',sans-serif; font-size:22px; color:var(--red); letter-spacing:1px; margin-bottom:4px; }
  .g-name { font-size:11px; color:var(--muted); font-family:'Roboto Mono',monospace; margin-bottom:8px; }
  .g-desc { font-size:13px; color:var(--text2); line-height:1.7; }
  .g-bench { margin-top:8px; font-size:11px; font-family:'Roboto Mono',monospace; background:var(--surface2); border:1px solid var(--border); border-radius:3px; padding:5px 10px; color:var(--text2); }
  .g-bench b { color:var(--green); }
  .g-tag { display:inline-block; font-size:9px; font-family:'Roboto Mono',monospace; padding:1px 6px; border-radius:2px; letter-spacing:1px; margin-bottom:8px; }
  .g-tag.adv { color:var(--red); border:1px solid var(--red-light); background:var(--red-light); }
  .g-tag.bas { color:var(--text2); border:1px solid var(--border); background:var(--surface2); }

  /* スコア計算式 */
  .weight-box { padding:20px; border-top:1px solid var(--border); background:var(--surface2); }
  .weight-box .title { font-family:'Roboto Mono',monospace; font-size:10px; letter-spacing:2px; color:var(--red); margin-bottom:12px; }
  .weight-chips { display:flex; flex-wrap:wrap; gap:8px; }
  .weight-chip { background:var(--surface); border:1px solid var(--border); border-radius:4px; padding:6px 12px; font-size:12px; font-family:'Roboto Mono',monospace; }
  .weight-chip b { color:var(--red); }
  .weight-note { margin-top:12px; font-size:12px; color:var(--muted); line-height:1.7; }

  /* グラフ */
  .chart-wrap { padding:20px; height:300px; }

  /* アドセンス */
  .adsense-slot { padding:12px 20px; border-top:1px solid var(--border); background:var(--surface2); }
  .adsense-placeholder { height:60px; background:repeating-linear-gradient(-45deg,#f0ede8,#f0ede8 6px,#fff 6px,#fff 12px); border:1px dashed var(--border2); border-radius:3px; display:flex; align-items:center; justify-content:center; font-size:11px; color:var(--muted); font-family:'Roboto Mono',monospace; letter-spacing:1px; }

  /* ── サイトナビゲーション ── */
  .site-nav {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 0 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
  }
  .site-brand {
    display: flex;
    align-items: baseline;
    gap: 10px;
    padding: 12px 0;
    text-decoration: none;
  }
  .site-brand-main {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px;
    letter-spacing: 2px;
    color: var(--text);
    line-height: 1;
  }
  .site-brand-main em { color: var(--red); font-style: normal; }
  .site-brand-sub {
    font-family: 'Roboto Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1px;
  }
  .site-nav-links {
    display: flex;
    align-items: center;
    gap: 4px;
  }
  .nav-link {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 12px;
    font-weight: 500;
    color: var(--muted);
    text-decoration: none;
    padding: 6px 12px;
    border-radius: 3px;
    transition: all .15s;
    white-space: nowrap;
  }
  .nav-link:hover { color: var(--text); background: var(--bg); }
  .nav-link.current { color: var(--red); font-weight: 700; }
  .nav-link.home-link {
    color: var(--text2);
    border: 1px solid var(--border);
  }
  .nav-link.home-link:hover { border-color: var(--red); color: var(--red); }

  /* ── スコア注釈 ── */
  .score-note {
    margin: 0 0 16px;
    padding: 14px 18px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--red);
    border-radius: 4px;
    font-size: 12px;
    color: var(--text2);
    line-height: 1.8;
    font-family: 'Roboto Mono', monospace;
  }
  .score-note .note-title {
    font-size: 10px;
    letter-spacing: 2px;
    color: var(--red);
    margin-bottom: 6px;
    font-weight: 700;
  }
  .score-note b { color: var(--text); }

  /* ── ランキング下部スコア説明 ── */
  .score-footer {
    border-top: 1px solid var(--border);
    background: var(--surface2);
    padding: 14px 20px;
    cursor: pointer;
    transition: background .15s;
  }
  .score-footer:hover { background: var(--red-light); }
  .score-footer-inner {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }
  .score-footer-label {
    font-family: 'Roboto Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: var(--red);
    letter-spacing: 1px;
    white-space: nowrap;
  }
  .score-footer-avg {
    font-family: 'Roboto Mono', monospace;
    font-size: 11px;
    color: var(--text2);
    flex: 1;
  }
  .score-footer-avg b { color: var(--text); }
  .score-footer-cta {
    font-family: 'Roboto Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    white-space: nowrap;
  }
  .score-footer:hover .score-footer-cta { color: var(--red); }

  /* ── モーダル ── */
  .modal-overlay {
    display: none;
    position: fixed; inset: 0;
    background: rgba(0,0,0,0.45);
    z-index: 2000;
    align-items: center;
    justify-content: center;
  }
  .modal-overlay.open { display: flex; }
  .modal-box {
    background: var(--surface);
    border-radius: 6px;
    padding: 32px 28px;
    max-width: 520px;
    width: 92%;
    box-shadow: 0 8px 40px rgba(0,0,0,0.18);
    position: relative;
    animation: fadeUp .2s ease;
  }
  .modal-close {
    position: absolute; top: 14px; right: 16px;
    font-size: 20px; cursor: pointer; color: var(--muted);
    background: none; border: none; line-height: 1;
  }
  .modal-close:hover { color: var(--text); }
  .modal-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px; letter-spacing: 2px;
    color: var(--red); margin-bottom: 4px;
  }
  .modal-sub {
    font-family: 'Roboto Mono', monospace;
    font-size: 11px; color: var(--muted); margin-bottom: 20px;
  }
  .modal-formula {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-left: 3px solid var(--red);
    border-radius: 3px;
    padding: 14px 16px;
    font-family: 'Roboto Mono', monospace;
    font-size: 12px; line-height: 1.8;
    color: var(--text2); margin-bottom: 16px;
  }
  .modal-formula b { color: var(--red); }
  .modal-avg {
    background: var(--red-light);
    border: 1px solid var(--red-mid);
    border-radius: 4px;
    padding: 14px 16px;
    margin-bottom: 16px;
  }
  .modal-avg-title {
    font-family: 'Roboto Mono', monospace;
    font-size: 10px; letter-spacing: 2px;
    color: var(--red); font-weight: 700; margin-bottom: 10px;
  }
  .modal-avg-stats {
    display: flex; flex-wrap: wrap; gap: 12px;
  }
  .modal-avg-stat {
    text-align: center; min-width: 60px;
  }
  .modal-avg-stat-val {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px; color: var(--red); line-height: 1;
  }
  .modal-avg-stat-label {
    font-family: 'Roboto Mono', monospace;
    font-size: 9px; color: var(--muted); letter-spacing: 1px;
  }
  .modal-note {
    font-size: 11px; color: var(--muted); line-height: 1.6;
  }

  /* スコアクリック可能スタイル */
  .score-meter { cursor: pointer; }
  .score-meter:hover .score-num { text-decoration: underline dotted; }
  .score-label-clickable {
    font-family: 'Roboto Mono', monospace;
    font-size: 9px; letter-spacing: 2px; color: var(--muted);
    margin-bottom: 4px;
  }
  .score-label-clickable::after {
    content: ' ⓘ';
    font-size: 10px; color: var(--red);
  }

  /* W・SO・ERAのツールチップ有効化 */
  .stat-chip.has-tip:hover { border-color: var(--red); box-shadow: 0 2px 8px rgba(200,16,46,.08); }

  .footer { text-align:center; padding:20px; font-size:11px; color:var(--muted); font-family:'Roboto Mono',monospace; border-top:1px solid var(--border); background:var(--surface); }

  @keyframes fadeUp { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
  .score-banner { animation:fadeUp .35s ease both; }
  .score-banner:nth-child(1){animation-delay:.04s} .score-banner:nth-child(2){animation-delay:.10s}
  .score-banner:nth-child(3){animation-delay:.16s} .score-banner:nth-child(4){animation-delay:.22s}
  .score-banner:nth-child(5){animation-delay:.28s}

  @media(max-width:680px){
    .stat-area { padding-left:20px; }
    .tab-btn { padding:12px 12px; font-size:12px; }
    .score-num { font-size:32px; }
  }
</style>
</head>
<body>

<div class="topbar">2026 MLB SEASON &nbsp;|&nbsp; 毎朝10時JST自動更新 &nbsp;|&nbsp; DATA: MLB Stats API</div>

<!-- サイヤングスコア解説モーダル -->
<div class="modal-overlay" id="score-modal" onclick="closeModal(event)">
  <div class="modal-box">
    <button class="modal-close" onclick="document.getElementById('score-modal').classList.remove('open')">✕</button>
    <div class="modal-title">CY YOUNG SCORE</div>
    <div class="modal-sub">サンノゼポテト独自の投手総合評価スコア</div>
    <div class="modal-formula">
      各指標のリーグ内順位を点数化（<b>1位=100pt</b>、最下位=約14pt）し、重みを乗じて合算。<br>
      <b>ERA×3.5</b> + <b>WHIP×3.0</b> + SO×1.2 + W×1.0<br>
      + K/9×1.0 + BB/9×1.0 + K/BB×0.8 + QS%×0.5
    </div>
    <div class="modal-avg">
      <div class="modal-avg-title">過去5年（2021-2025）受賞者平均 ← この水準が目安</div>
      <div class="modal-avg-stats">
        <div class="modal-avg-stat">
          <div class="modal-avg-stat-val">2.35</div>
          <div class="modal-avg-stat-label">ERA</div>
        </div>
        <div class="modal-avg-stat">
          <div class="modal-avg-stat-val">0.96</div>
          <div class="modal-avg-stat-label">WHIP</div>
        </div>
        <div class="modal-avg-stat">
          <div class="modal-avg-stat-val">225</div>
          <div class="modal-avg-stat-label">SO</div>
        </div>
        <div class="modal-avg-stat">
          <div class="modal-avg-stat-val">14.9</div>
          <div class="modal-avg-stat-label">W</div>
        </div>
        <div class="modal-avg-stat">
          <div class="modal-avg-stat-val">190.7</div>
          <div class="modal-avg-stat-label">IP</div>
        </div>
      </div>
    </div>
    <div class="modal-note">
      WARは公式APIで取得できないため除外。FIPも同様。<br>
      ERA・WHIPを重視した設計は実際のサイヤング賞投票傾向に基づいています。<br>
      詳細は「指標解説」タブをご覧ください。
    </div>
  </div>
</div>

<!-- サイトナビゲーション -->
<nav class="site-nav">
  <a class="site-brand" href="https://ponshu-usa.jp/">
    <span class="site-brand-main">MLB<em>と</em>マリオット</span>
    <span class="site-brand-sub">サンノゼポテトの米国生活</span>
  </a>
  <div class="site-nav-links">
    <a class="nav-link home-link" href="https://ponshu-usa.jp/">HOME</a>
    <a class="nav-link" href="/mlb-tracker/hr-race.html">HR王争い</a>
    <a class="nav-link current" href="/mlb-tracker/cy-young.html">サイヤング賞争い</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-eyebrow">2026 MLB Cy Young Award Race</div>
  <h1>サイヤング<em>賞</em>争い</h1>
  <div class="hero-sub">最終更新: <b id="last-updated">読み込み中...</b></div>
</div>

<div class="tabs">
  <button class="tab-btn active" onclick="switchTab('al',this)">ア・リーグ</button>
  <button class="tab-btn" onclick="switchTab('nl',this)">ナ・リーグ</button>
  <button class="tab-btn" onclick="switchTab('trend',this)">受賞者実績</button>
  <button class="tab-btn" onclick="switchTab('glossary',this)">指標解説</button>
</div>

<div class="container">

  <div id="tab-al" class="tab-panel active">
    <div class="card">
      <div class="card-header">
        <span class="card-title">American League — Cy Young Score Ranking</span>
        <span class="league-badge">AL</span>
      </div>
      <div id="al-list"></div>
      <!-- スコア説明フッター -->
      <div class="score-footer" onclick="openScoreModal()">
        <div class="score-footer-inner">
          <span class="score-footer-label">CY YOUNG SCORE とは？</span>
          <span class="score-footer-avg">受賞者平均の目安 &nbsp; ERA <b>2.35</b> &nbsp; WHIP <b>0.96</b> &nbsp; SO <b>225</b> &nbsp; W <b>14.9</b> &nbsp; IP <b>190.7</b></span>
          <span class="score-footer-cta">クリックで詳細 ⓘ</span>
        </div>
      </div>
    </div>
  </div>

  <div id="tab-nl" class="tab-panel">
    <div class="card">
      <div class="card-header">
        <span class="card-title">National League — Cy Young Score Ranking</span>
        <span class="league-badge">NL</span>
      </div>
      <div id="nl-list"></div>
      <!-- スコア説明フッター -->
      <div class="score-footer" onclick="openScoreModal()">
        <div class="score-footer-inner">
          <span class="score-footer-label">CY YOUNG SCORE とは？</span>
          <span class="score-footer-avg">受賞者平均の目安 &nbsp; ERA <b>2.35</b> &nbsp; WHIP <b>0.96</b> &nbsp; SO <b>225</b> &nbsp; W <b>14.9</b> &nbsp; IP <b>190.7</b></span>
          <span class="score-footer-cta">クリックで詳細 ⓘ</span>
        </div>
      </div>
    </div>
  </div>

  <div id="tab-trend" class="tab-panel">
    <div class="card">
      <div class="card-header">
        <span class="card-title">過去5年 サイヤング賞受賞者の成績</span>
        <span style="font-size:11px;color:var(--muted);font-family:'Roboto Mono',monospace;">受賞時の指標が今季の「目安」になる</span>
      </div>
      <div style="overflow-x:auto;">
        <table id="cy-history-table" style="width:100%;border-collapse:collapse;font-size:13px;">
          <thead>
            <tr style="background:var(--surface2);border-bottom:2px solid var(--border);">
              <th style="padding:10px 16px;text-align:left;font-family:'Roboto Mono',monospace;font-size:10px;letter-spacing:1.5px;color:var(--muted);font-weight:700;">年</th>
              <th style="padding:10px 8px;text-align:left;font-family:'Roboto Mono',monospace;font-size:10px;letter-spacing:1.5px;color:var(--muted);font-weight:700;">L</th>
              <th style="padding:10px 12px;text-align:left;font-family:'Noto Sans JP',sans-serif;font-size:11px;color:var(--muted);font-weight:700;">選手</th>
              <th style="padding:10px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--muted);font-weight:700;">W</th>
              <th style="padding:10px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--muted);font-weight:700;">ERA</th>
              <th style="padding:10px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--muted);font-weight:700;">SO</th>
              <th style="padding:10px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--muted);font-weight:700;">WHIP</th>
              <th style="padding:10px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--muted);font-weight:700;">IP</th>
              <th style="padding:10px 12px;text-align:left;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--muted);font-weight:700;">チーム</th>
            </tr>
          </thead>
          <tbody id="cy-history-body"></tbody>
        </table>
      </div>
      <div style="padding:14px 20px;font-size:11px;color:var(--muted);font-family:'Roboto Mono',monospace;border-top:1px solid var(--border);background:var(--surface2);">
        ※ 2025年スキーンズは途中成績のため平均算出から除外。DATA: MLB公式記録。
      </div>
    </div>
  </div>

  <div id="tab-glossary" class="tab-panel">
    <div class="card">
      <div class="card-header">
        <span class="card-title">指標解説 — Stat Glossary</span>
        <span style="font-size:11px;color:var(--muted);font-family:'Roboto Mono',monospace;">各チップにホバーでも確認</span>
      </div>
      <div class="glossary-grid" id="glossary-grid"></div>
      <div class="weight-box">
        <div class="title">CY YOUNG SCORE — 重み付け設計</div>
        <div class="weight-chips" id="weight-chips"></div>
        <div class="weight-note">
          各指標のリーグ内順位を点数化（1位=100点、最下位=20点）し、重みを乗じて合算。<br>
          ERA・WHIP・WARを重視した設計は実際のサイヤング賞投票傾向に基づいています。
        </div>
      </div>
    </div>
  </div>

</div>

<div class="adsense-slot" style="max-width:1080px;margin:0 auto 24px;padding:0 20px;">
  <ins class="adsbygoogle"
    style="display:block"
    data-ad-client="ca-pub-2592831002858501"
    data-ad-slot="1337690252"
    data-ad-format="auto"
    data-full-width-responsive="true"></ins>
  <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
</div>

<div class="footer">
  © サンノゼポテト &nbsp;|&nbsp; DATA: MLB Stats API (statsapi.mlb.com) &nbsp;|&nbsp; JP = 日本人選手
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script>
// ============================================================
// 変換テーブル
// ============================================================
// チーム正式名 → 略称（data.jsonのteamフィールドが正式名の場合に対応）
const TEAM_NAME_TO_ABBR = {
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
};
const TEAM_JA = {
  LAD:"ドジャース",LAA:"エンゼルス",NYY:"ヤンキース",NYM:"メッツ",
  BOS:"レッドソックス",CHC:"カブス",HOU:"アストロズ",ATL:"ブレーブス",
  SEA:"マリナーズ",SFG:"ジャイアンツ",STL:"カージナルス",PHI:"フィリーズ",
  TOR:"ブルージェイズ",MIL:"ブルワーズ",ARI:"ダイヤモンドバックス",
  MIN:"ツインズ",CLE:"ガーディアンズ",TB:"レイズ",BAL:"オリオールズ",
  DET:"タイガース",KC:"ロイヤルズ",CWS:"ホワイトソックス",
  OAK:"アスレチックス",TEX:"レンジャーズ",COL:"ロッキーズ",
  SD:"パドレス",CIN:"レッズ",MIA:"マーリンズ",WSH:"ナショナルズ",PIT:"パイレーツ",
};
const PLAYER_JA = {
  808967:"山本 由伸",660271:"大谷 翔平",681911:"今永 昇太",
  808963:"佐々木 朗希",608372:"菅野 智之",
};

// ============================================================
// 指標定義
// ============================================================
const STAT_DEFS = [
  { key:"era",  label:"ERA",  name:"防御率",             advanced:false, lowGood:true,
    desc:"9イニングあたりの自責点。投手の安定感を示す最も基本的な指標。",
    bench:"3.00以下が優秀、2.00以下はエース級" },
  { key:"whip", label:"WHIP", name:"WHIP",               advanced:true,  lowGood:true,
    desc:"1イニングに許した走者数（四球＋安打）。守備に依存しない被出塁の許容度。",
    bench:"1.00以下が優秀、0.90以下はエリート" },
  { key:"w",    label:"W",    name:"勝利数",             advanced:false, lowGood:false,
    desc:"先発投手が勝利投手になった回数。打線の援護にも左右されるため単独では評価しにくい。",
    bench:"10勝以上でトップクラス" },
  { key:"so",   label:"SO",   name:"奪三振",             advanced:false, lowGood:false,
    desc:"三振を奪った総数。球の支配力・制球力の高さを示す。",
    bench:"シーズン200奪三振以上でトップクラス" },
  { key:"k9",   label:"K/9",  name:"K/9",               advanced:true,  lowGood:false,
    desc:"9イニングあたりの奪三振数。球の支配力・空振り能力を示す。",
    bench:"10.0以上が優秀" },
  { key:"bb9",  label:"BB/9", name:"BB/9",              advanced:true,  lowGood:true,
    desc:"9イニングあたりの与四球数。少ないほど制球力が高い。",
    bench:"2.0以下が優秀" },
  { key:"kbb",  label:"K/BB", name:"K/BB比",            advanced:true,  lowGood:false,
    desc:"奪三振÷与四球。高いほど「三振は奪えるが四球を出さない」理想的な投球スタイル。",
    bench:"3.0以上が優秀、5.0以上はエリート" },
  { key:"qs",   label:"QS%",  name:"クオリティスタート率",advanced:true,  lowGood:false,
    desc:"先発登板のうち「6回以上・自責3以下」を達成した割合。先発としての安定感の指標。",
    bench:"60%以上が優秀" },
];

// ============================================================
// 重み付け設定（ERA/WHIP/WAR重視）
// FIP/WAR/QSはデータなし(0)の場合はスコア計算から除外
// ============================================================
const WEIGHTS = {
  era:3.5, whip:3.0,
  so:1.2, w:1.0, k9:1.0, bb9:1.0, kbb:0.8, qs:0.5,
};
// データなし(0)を許容する指標（Stats APIで取得不可）
const NO_DATA_KEYS = new Set([]);

const TOTAL_WEIGHT = Object.values(WEIGHTS).reduce((a,b)=>a+b,0);

// ============================================================
// スコア計算エンジン
// FIP/WAR/QS=0の場合はその指標をスコアから除外
// ============================================================
function calcCyScore(pitchers) {
  const n = pitchers.length;

  // データなし指標を除いた有効指標を判定
  const hasData = {};
  STAT_DEFS.forEach(def => {
    hasData[def.key] = NO_DATA_KEYS.has(def.key)
      ? pitchers.some(p => p[def.key] > 0)
      : true;
  });

  // 各指標のリーグ内順位を計算（有効指標のみ）
  const rankMaps = {};
  STAT_DEFS.forEach(def => {
    if (!hasData[def.key]) return;
    const sorted = [...pitchers].sort((a,b) =>
      def.lowGood ? a[def.key] - b[def.key] : b[def.key] - a[def.key]
    );
    rankMaps[def.key] = {};
    sorted.forEach((p, i) => rankMaps[def.key][p.id] = i + 1);
  });

  // 有効指標の重み合計
  const activeWeight = Object.entries(WEIGHTS)
    .filter(([k]) => hasData[k])
    .reduce((s, [,w]) => s + w, 0);

  // スコア計算
  const scored = pitchers.map(p => {
    let score = 0;
    Object.entries(WEIGHTS).forEach(([key, w]) => {
      if (!hasData[key]) return;
      const rank = rankMaps[key][p.id];
      const pts  = (n - rank + 1) / n * 100;
      score += pts * w;
    });
    return {
      ...p,
      cyScore: Math.round(score / activeWeight * 10) / 10,
      ranks:   Object.fromEntries(
        STAT_DEFS.map(d => [d.key, rankMaps[d.key]?.[p.id] ?? null])
      ),
    };
  });

  return scored.sort((a,b) => b.cyScore - a.cyScore);
}

// ============================================================
// チップの値グレード
// ============================================================
function gradeVal(def, val) {
  if (def.lowGood) {
    const thr = {era:[2.5,3.0],fip:[2.5,3.0],whip:[0.95,1.10],bb9:[2.0,2.5]};
    const [g,ok] = thr[def.key]||[99,99];
    return val<=g?'great':val<=ok?'good':'';
  } else {
    const thr = {w:[7,5],so:[80,60],war:[2.5,1.8],k9:[11,9.5],kbb:[5,3.5],qs:[70,60]};
    const [g,ok] = thr[def.key]||[-1,-1];
    return val>=g?'great':val>=ok?'good':'';
  }
}

function rankClass(r) {
  return r===1?'r1':r===2?'r2':r===3?'r3':'rn';
}
function getRankLabel(r) {
  return r===1?'リーグ1位':r===2?'リーグ2位':r===3?'リーグ3位':`リーグ${r}位`;
}

// ============================================================
// ツールチップ
// ============================================================
function tooltipHtml(def, val, rank) {
  // 全指標でツールチップを表示
  const display = def.key === 'qs' ? val + '%' : val;
  return `
    <div class="tooltip">
      <div class="tip-label">${def.label} — ${def.name}</div>
      <div class="tip-val">この選手: ${display} &nbsp; ${getRankLabel(rank)}</div>
      ${def.desc}<br>
      <span style="color:#aaa;font-size:11px;">目安: ${def.bench}</span>
    </div>`;
}

// ============================================================
// 投手リスト描画（スコア順）+ ランク外選手
// ============================================================

// ランク外に常に表示する注目選手
const OUT_OF_RANK = {
  NL: [
    { id:808967, name:"Yoshinobu Yamamoto", team:"LAD", isJP:true  },
    { id:660271, name:"Shohei Ohtani",      team:"LAD", isJP:true  },
    { id:681911, name:"Shota Imanaga",      team:"CHC", isJP:true  },
    { id:608372, name:"Kodai Senga",        team:"COL", isJP:true  },
    { id:808963, name:"Roki Sasaki",        team:"LAD", isJP:true  },
    { id:694973, name:"Paul Skenes",        team:"PIT", isJP:false },
  ],
  AL: [
    { id:592789, name:"Gerrit Cole",        team:"NYY", isJP:false },
    { id:543037, name:"Corbin Burnes",      team:"BAL", isJP:false },
  ],
};

function buildChips(p, isRanked) {
  return STAT_DEFS.map(def => {
    const val   = p[def.key] ?? 0;
    const rank  = isRanked ? (p.ranks?.[def.key] ?? null) : null;
    const grade = gradeVal(def, val);
    const hint  = '<span class="hint-icon">?</span>';
    // 全指標でツールチップを表示（rankedの場合のみ）
    const tip   = isRanked && rank !== null ? tooltipHtml(def, val, rank) : '';
    const hasTip = tip ? ' has-tip' : '';
    const disp  = def.key === 'qs' ? val + '%' : val;
    const rkHtml = !isRanked
      ? '<div class="chip-rank rn" style="color:#ccc">参考</div>'
      : rank !== null
        ? `<div class="chip-rank ${rankClass(rank)}">${getRankLabel(rank)}</div>`
        : '<div class="chip-rank rn" style="color:#ccc">－</div>';
    return `<div class="stat-chip${hasTip}">
      <div class="chip-label">${def.label}${hint}</div>
      <div class="chip-val ${grade}">${disp}</div>
      ${rkHtml}${tip}
    </div>`;
  }).join('');
}

function buildBanner(p, rankNum, isRanked, maxScore) {
  const jaName  = PLAYER_JA[p.id];
  const abbr    = TEAM_NAME_TO_ABBR[p.team] || p.team;
  const teamJa  = TEAM_JA[abbr] || abbr;
  const jpCls   = p.isJP ? 'jp' : '';
  const badge   = p.isJP ? '<span class="jp-badge">JP</span>' : '';
  const nameDisp = jaName
    ? `${jaName}${badge}`
    : `<span style="color:var(--text)">${p.name}</span>${badge}`;
  const chips = buildChips(p, isRanked);

  const rankDisp  = isRanked ? rankNum : '－';
  const rankStyle = isRanked ? '' : 'font-size:16px;color:var(--muted)';
  const pct       = isRanked ? Math.round(p.cyScore / maxScore * 100) : 0;
  const meterHtml = isRanked
    ? `<div class="score-label-clickable">CY YOUNG SCORE</div>
       <div class="score-num">${p.cyScore}</div>
       <div class="score-bar-wrap"><div class="score-bar" style="width:${pct}%"></div></div>`
    : `<div class="score-label" style="color:var(--muted)">ランク外</div>
       <div style="font-family:'Roboto Mono',monospace;font-size:12px;color:var(--muted);margin-top:4px">参考表示</div>`;

  return `
    <div class="score-banner ${jpCls}">
      <div class="score-rank" style="${rankStyle}">${rankDisp}</div>
      <div class="score-info">
        <div class="score-name-ja">${nameDisp}</div>
        <div class="score-name-en">${jaName ? '' : p.name}</div>
        <div class="score-team">${abbr} <span class="ja">${teamJa}</span> &nbsp; ${p.ip || 0} IP${p.gs ? ' &nbsp; ' + p.gs + '先発' : ''}</div>
      </div>
      <div class="score-meter" onclick="openScoreModal()" title="クリックでスコア計算式を表示">${meterHtml}</div>
    </div>
    <div class="stat-area ${jpCls}">
      <div class="stats-grid">${chips}</div>
    </div>`;
}

function renderPitcherList(containerId, pitchers, league) {
  const el = document.getElementById(containerId);
  if (!pitchers || pitchers.length === 0) {
    el.innerHTML = `<div style="padding:40px;text-align:center;color:var(--muted);font-family:'Roboto Mono',monospace;font-size:12px;">データを取得中...</div>`;
    return;
  }

  const scored    = calcCyScore(pitchers);
  const maxScore  = scored[0].cyScore || 1;
  const rankedIds = new Set(scored.map(p => p.id));

  // ランク外: OUT_OF_RANKの定義 + data.jsonのoutOfRankPitchersで実データを補完
  const cyAll    = (DATA.cyYoung?.[league] || []);
  const cyMap    = Object.fromEntries(cyAll.map(p => [p.id, p]));
  // outOfRankPitchers: fetch_all.pyがIP不足で正規ランキングから外したJP投手の実データ
  const oorMap   = DATA.outOfRankPitchers || {};
  const outDefs  = OUT_OF_RANK[league] || [];
  const outPlayers = outDefs
    .filter(p => !rankedIds.has(p.id))
    .map(p => {
      // 優先順位: outOfRankPitchers > cyYoung > デフォルト0
      const d = oorMap[String(p.id)] || cyMap[p.id];
      return d
        ? { ...p, ...d }
        : { ...p, w:0, era:0, so:0, whip:0, ip:0, gs:0, k9:0, bb9:0, kbb:0, qs:0 };
    });

  let html = scored.map((p, i) => buildBanner(p, i + 1, true, maxScore)).join('');

  if (outPlayers.length > 0) {
    html += `<div style="padding:10px 20px 4px;font-size:10px;letter-spacing:2px;color:var(--muted);font-family:'Roboto Mono',monospace;border-top:2px solid var(--border);background:var(--surface2)">ランク外 — 注目選手</div>`;
    html += outPlayers.map(p => buildBanner(p, '－', false, maxScore)).join('');
  }

  el.innerHTML = html;
}

// ============================================================
// 指標解説グリッド
// ============================================================
function renderGlossary() {
  document.getElementById('glossary-grid').innerHTML = STAT_DEFS.map(def => `
    <div class="glossary-item ${def.advanced?'advanced':''}">
      <span class="g-tag ${def.advanced?'adv':'bas'}">${def.advanced?'ADVANCED':'BASIC'}</span>
      <div class="g-label">${def.label}</div>
      <div class="g-name">${def.name}</div>
      <div class="g-desc">${def.desc}</div>
      <div class="g-bench">目安: <b>${def.bench}</b></div>
    </div>`).join('');

  // 重みチップ
  document.getElementById('weight-chips').innerHTML = Object.entries(WEIGHTS)
    .sort((a,b)=>b[1]-a[1])
    .map(([k,w]) => `<div class="weight-chip">${k.toUpperCase()} <b>×${w}</b></div>`)
    .join('');
}

// ============================================================
// 過去5年 サイヤング賞受賞者テーブル
// ============================================================
const CY_HISTORY = [
  // 2025
  { year:2025, league:"AL", name:"Tarik Skubal",     nameJa:"T.スクーバル", team:"DET デトロイト・タイガース", w:13, era:2.21, so:241, whip:0.89, ip:195.1 },
  { year:2025, league:"NL", name:"Paul Skenes",      nameJa:"P.スキーンズ", team:"PIT パイレーツ",            w:6,  era:3.00, so:65,  whip:0.82, ip:60.0, note:"途中成績" },
  // 2024
  { year:2024, league:"AL", name:"Tarik Skubal",     nameJa:"T.スクーバル", team:"DET デトロイト・タイガース", w:18, era:2.39, so:228, whip:1.01, ip:192.0 },
  { year:2024, league:"NL", name:"Chris Sale",       nameJa:"C.セール",     team:"ATL アトランタ・ブレーブス", w:18, era:2.38, so:225, whip:0.84, ip:177.2 },
  // 2023
  { year:2023, league:"AL", name:"Gerrit Cole",      nameJa:"G.コール",     team:"NYY ニューヨーク・ヤンキース",w:15, era:2.63, so:222, whip:0.98, ip:209.0 },
  { year:2023, league:"NL", name:"Blake Snell",      nameJa:"B.スネル",     team:"SD  サンディエゴ・パドレス", w:14, era:2.25, so:234, whip:1.08, ip:180.0 },
  // 2022
  { year:2022, league:"AL", name:"Justin Verlander", nameJa:"J.バーランダー",team:"HOU ヒューストン・アストロズ",w:18, era:1.75, so:185, whip:0.83, ip:175.0 },
  { year:2022, league:"NL", name:"Sandy Alcántara",  nameJa:"S.アルカンタラ",team:"MIA マイアミ・マーリンズ",  w:14, era:2.28, so:207, whip:0.98, ip:228.2 },
  // 2021
  { year:2021, league:"AL", name:"Robbie Ray",       nameJa:"R.レイ",       team:"TOR トロント・ブルージェイズ",w:13, era:2.84, so:248, whip:1.05, ip:193.0 },
  { year:2021, league:"NL", name:"Corbin Burnes",    nameJa:"C.バーンズ",   team:"MIL ミルウォーキー・ブルワーズ",w:11,era:2.43, so:234, whip:0.94, ip:167.0 },
  // 平均行（スキーンズ途中成績除く9名）
  { year:"avg", league:"",  name:"2021-2025 Average",nameJa:"受賞者平均",   team:"過去5年（2021-2025）",       w:14.9,era:2.35,so:225, whip:0.96, ip:190.7 },
];

function renderCyHistory() {
  const tbody = document.getElementById('cy-history-body');
  if (!tbody) return;

  let prevYear = null;
  tbody.innerHTML = CY_HISTORY.map(r => {
    const isAvg = r.year === 'avg';

    // 平均行は特別スタイル
    if (isAvg) {
      const avgStyle = 'background:var(--red-light);border-top:2px solid var(--red)';
      return `<tr style="${avgStyle}">
        <td style="padding:14px 16px;font-family:'Roboto Mono',monospace;font-size:11px;letter-spacing:1px;color:var(--red);font-weight:700;white-space:nowrap">受賞者<br>平均</td>
        <td style="padding:14px 8px"></td>
        <td style="padding:14px 12px">
          <div style="font-weight:700;font-size:13px;color:var(--red)">サイヤング賞クラスの目安</div>
          <div style="font-size:11px;color:var(--muted);font-family:'Roboto Mono',monospace;margin-top:2px">2021-2025 受賞者9名平均（スキーンズ途中除く）</div>
        </td>
        <td style="padding:14px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--red);font-weight:700">${r.w}</td>
        <td style="padding:14px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--red);font-weight:700">${r.era}</td>
        <td style="padding:14px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--red);font-weight:700">${r.so}</td>
        <td style="padding:14px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--red);font-weight:700">${r.whip}</td>
        <td style="padding:14px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:14px;color:var(--red);font-weight:700">${r.ip}</td>
        <td style="padding:14px 12px"></td>
      </tr>`;
    }

    const isNewYear = r.year !== prevYear;
    prevYear = r.year;
    const yearCell = isNewYear
      ? `<td rowspan="2" style="padding:12px 16px;vertical-align:middle;font-family:'Bebas Neue',sans-serif;font-size:28px;color:var(--text);border-bottom:1px solid var(--border)">${r.year}</td>`
      : '';
    const lBadge = r.league === 'AL'
      ? `<span style="background:var(--red-light);color:var(--red);font-family:'Roboto Mono',monospace;font-size:10px;padding:2px 6px;border-radius:2px;font-weight:700">AL</span>`
      : `<span style="background:#f0f6ff;color:var(--jp);font-family:'Roboto Mono',monospace;font-size:10px;padding:2px 6px;border-radius:2px;font-weight:700">NL</span>`;
    const borderStyle = 'border-bottom:1px solid var(--border)';
    const noteHtml = r.note ? `<span style="font-size:10px;color:var(--muted);margin-left:6px">(${r.note})</span>` : '';
    const eraColor  = r.era <= 2.0 ? 'color:var(--red);font-weight:700' : r.era <= 2.5 ? 'color:var(--green)' : '';
    const whipColor = r.whip <= 0.90 ? 'color:var(--red);font-weight:700' : r.whip <= 1.05 ? 'color:var(--green)' : '';
    return `<tr>
      ${yearCell}
      <td style="padding:12px 8px;${borderStyle}">${lBadge}</td>
      <td style="padding:12px 12px;${borderStyle}">
        <div style="font-weight:700;font-size:14px">${r.nameJa}</div>
        <div style="font-size:11px;color:var(--muted);font-family:'Roboto Mono',monospace;margin-top:2px">${r.name}${noteHtml}</div>
        <div style="font-size:11px;color:var(--muted);margin-top:2px">${r.team}</div>
      </td>
      <td style="padding:12px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:22px;${borderStyle}">${r.w}</td>
      <td style="padding:12px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:22px;${eraColor};${borderStyle}">${r.era}</td>
      <td style="padding:12px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:22px;${borderStyle}">${r.so}</td>
      <td style="padding:12px 10px;text-align:center;font-family:'Bebas Neue',sans-serif;font-size:22px;${whipColor};${borderStyle}">${r.whip}</td>
      <td style="padding:12px 10px;text-align:center;font-family:'Roboto Mono',monospace;font-size:13px;color:var(--text2);${borderStyle}">${r.ip}</td>
      <td style="padding:12px 12px;font-size:12px;color:var(--muted);${borderStyle}">${r.team.split(' ')[0]}</td>
    </tr>`;
  }).join('');
}

// ============================================================
// モックデータ
// ============================================================
const DATA = {
  updatedAt:"2026-05-25",
  cyYoung:{
    AL:[
      {id:808967,name:"Yoshinobu Yamamoto",team:"LAD",isJP:true, w:7,era:1.98,so:89,whip:0.87,fip:2.14,war:3.1,k9:11.2,bb9:1.8,kbb:6.2,qs:78,ip:81.2},
      {id:660271,name:"Shohei Ohtani",     team:"LAA",isJP:true, w:6,era:2.31,so:84,whip:0.95,fip:2.44,war:2.7,k9:10.8,bb9:2.1,kbb:5.1,qs:71,ip:74.0},
      {id:543037,name:"Corbin Burnes",     team:"BAL",isJP:false,w:6,era:2.54,so:76,whip:1.01,fip:2.71,war:2.4,k9:10.1,bb9:2.3,kbb:4.4,qs:68,ip:78.1},
      {id:592789,name:"Gerrit Cole",       team:"NYY",isJP:false,w:5,era:2.89,so:71,whip:1.08,fip:2.95,war:2.1,k9:9.8, bb9:2.5,kbb:3.9,qs:62,ip:72.0},
      {id:605400,name:"Kevin Gausman",     team:"TOR",isJP:false,w:5,era:3.12,so:68,whip:1.12,fip:3.21,war:1.9,k9:9.4, bb9:2.8,kbb:3.4,qs:58,ip:69.1},
    ],
    NL:[
      {id:681911,name:"Shota Imanaga",  team:"CHC",isJP:true, w:7,era:2.12,so:82,whip:0.91,fip:2.28,war:2.9,k9:10.9,bb9:1.6,kbb:6.8,qs:75,ip:79.1},
      {id:477132,name:"Zack Wheeler",   team:"PHI",isJP:false,w:6,era:2.44,so:78,whip:0.98,fip:2.55,war:2.6,k9:10.4,bb9:2.0,kbb:5.2,qs:70,ip:77.0},
      {id:669373,name:"Spencer Strider",team:"ATL",isJP:false,w:6,era:2.67,so:92,whip:1.02,fip:2.41,war:2.8,k9:11.8,bb9:2.4,kbb:4.9,qs:65,ip:74.2},
      {id:608566,name:"Blake Snell",    team:"SFG",isJP:false,w:5,era:2.98,so:74,whip:1.09,fip:2.87,war:2.2,k9:10.2,bb9:3.1,kbb:3.3,qs:60,ip:68.0},
      {id:641154,name:"Freddy Peralta", team:"MIL",isJP:false,w:5,era:3.22,so:69,whip:1.15,fip:3.31,war:1.8,k9:9.6, bb9:2.9,kbb:3.3,qs:55,ip:66.2},
    ]
  }
};

// ============================================================
// モーダル開閉
// ============================================================
function openScoreModal() {
  document.getElementById('score-modal').classList.add('open');
}
function closeModal(e) {
  if (e.target === document.getElementById('score-modal')) {
    document.getElementById('score-modal').classList.remove('open');
  }
}
// ESCキーで閉じる
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') document.getElementById('score-modal').classList.remove('open');
});

// ============================================================
// タブ切り替え
// ============================================================
function switchTab(name, btn) {
  document.querySelectorAll('.tab-panel').forEach(e=>e.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(e=>e.classList.remove('active'));
  document.getElementById('tab-'+name).classList.add('active');
  btn.classList.add('active');
  if(name==='trend') renderCyHistory();
}

// ============================================================
// ============================================================
// 初期化 / 本番データ読み込み
// ============================================================
function init() {
  document.getElementById('last-updated').textContent = DATA.updatedAt;
  renderPitcherList('al-list', DATA.cyYoung.AL, 'AL');
  renderPitcherList('nl-list', DATA.cyYoung.NL, 'NL');
  renderGlossary();
}

fetch('/mlb-tracker/data.json')
  .then(r => r.json())
  .then(d => { Object.assign(DATA, d); init(); })
  .catch(() => init()); // fetch失敗時はモックデータで表示
</script>
</body>
</html>
