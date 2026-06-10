#!/usr/bin/env python3
"""
GOLAZO WORLD TV — GENERADOR DE STAT CARD SHORTS
Toma un JSON de configuración y genera la composición HyperFrames lista.

Uso:
  python3 make_short.py configs/brasil_duelos.json
  python3 make_short.py configs/argentina_goles.json

Cada config define: equipo, colores, textos ES/EN, jugadores y stats.
El HTML resultante se renderiza con: hyperframes render index.html
"""

import json, sys, os

# ── PALETAS POR EQUIPO ──────────────────────────────────────
TEAMS = {
    "brasil":    {"bg":"#F5D90A","accent":"#3E9B35","accent2":"#BDE8E0","txt_on_accent":"#F5D90A","val_txt":"#1d5c50","code":"BRA","dark":"#173a17"},
    "argentina": {"bg":"#9CCDEB","accent":"#1C5FA8","accent2":"#FFFFFF","txt_on_accent":"#9CCDEB","val_txt":"#1C5FA8","code":"ARG","dark":"#0d2a4a"},
    "francia":   {"bg":"#1B3C8C","accent":"#E03A3E","accent2":"#FFFFFF","txt_on_accent":"#FFFFFF","val_txt":"#1B3C8C","code":"FRA","dark":"#0a1838"},
    "espana":    {"bg":"#C8102E","accent":"#FFC400","accent2":"#FFE9A0","txt_on_accent":"#C8102E","val_txt":"#7a0a1c","code":"ESP","dark":"#3d0510"},
    "inglaterra":{"bg":"#FFFFFF","accent":"#CE1124","accent2":"#1B2A5B","txt_on_accent":"#FFFFFF","val_txt":"#1B2A5B","code":"ENG","dark":"#1B2A5B"},
    "mexico":    {"bg":"#0B6B3A","accent":"#CE1126","accent2":"#FFFFFF","txt_on_accent":"#FFFFFF","val_txt":"#0B6B3A","code":"MEX","dark":"#053019"},
    "alemania":  {"bg":"#000000","accent":"#DD0000","accent2":"#FFCE00","txt_on_accent":"#FFFFFF","val_txt":"#3a3a00","code":"GER","dark":"#1a1a1a"},
    "portugal":  {"bg":"#046A38","accent":"#DA291C","accent2":"#FFE900","txt_on_accent":"#FFFFFF","val_txt":"#046A38","code":"POR","dark":"#02371d"},
}

TEMPLATE = r"""<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=1080, height=1920" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@700;900&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    html, body {{ width:1080px; height:1920px; overflow:hidden; background:#000;
      font-family:'Anton', Impact, 'Arial Black', sans-serif; }}
    .scene {{ position:absolute; width:1080px; height:1920px; top:0; left:0; overflow:hidden; }}
    .s1-bg {{ background: radial-gradient(ellipse at 50% 35%, #1a1a1a 0%, #050505 70%); }}
    .s1-title {{ position:absolute; width:100%; top:200px; text-align:center; color:#e8e8e8;
      font-size:{title_size}px; line-height:0.95; text-transform:uppercase; letter-spacing:-2px;
      text-shadow:0 8px 30px rgba(0,0,0,0.9); }}
    .s1-title .w {{ display:block; opacity:0; }}
    .glow-pad {{ position:absolute; left:50%; top:980px; width:760px; height:760px;
      transform:translate(-50%,-50%); opacity:0;
      background: radial-gradient(circle, {glow_color}60 0%, {glow_color}1a 45%, transparent 70%); }}
    .player-row {{ position:absolute; width:100%; top:700px; display:flex;
      justify-content:center; align-items:flex-end; }}
    .cutout {{ width:330px; height:470px; border-radius:14px; background-size:cover;
      background-position:center top; position:relative; opacity:0;
      filter: drop-shadow(0 18px 40px rgba(0,0,0,0.75)); }}
    .cutout .ph {{ position:absolute; inset:0; border-radius:14px; display:flex;
      flex-direction:column; align-items:center; justify-content:flex-end; padding-bottom:26px;
      font-family:'Archivo', Arial, sans-serif; font-weight:900; }}
    .cutout .circle {{ width:195px; height:195px; border-radius:50%; display:flex;
      align-items:center; justify-content:center; font-size:88px; color:rgba(0,0,0,0.55);
      margin-bottom:18px; border:6px solid rgba(255,255,255,0.55); background:{team_bg}; }}
    .cutout .nm {{ font-size:34px; color:#fff; letter-spacing:1px; text-transform:uppercase;
      text-shadow:0 3px 10px rgba(0,0,0,0.8); }}
    .s2-bg {{ background: radial-gradient(ellipse at 50% 50%, #c40000 0%, #3d0000 55%, #0a0000 100%); }}
    .face-stack {{ position:absolute; width:100%; height:100%; display:flex; flex-direction:column; }}
    .face {{ flex:1; background-size:cover; background-position:center 20%;
      filter:grayscale(1) contrast(1.25) brightness(0.92); position:relative; opacity:0;
      border-bottom:5px solid rgba(0,0,0,0.65); }}
    .face .fph {{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center;
      font-size:200px; color:rgba(255,255,255,0.16); }}
    .s2-line {{ position:absolute; width:100%; top:46%; text-align:center; color:#fff;
      font-size:92px; text-transform:uppercase; line-height:1.02; opacity:0; z-index:5;
      text-shadow:0 0 50px rgba(255,0,0,0.9), 0 6px 22px rgba(0,0,0,0.95); }}
    .s3-bg {{ background:{team_bg}; }}
    .bg-pattern {{ position:absolute; inset:0; overflow:hidden; color:{pattern_color};
      font-size:230px; line-height:0.92; letter-spacing:8px; white-space:pre-line;
      text-align:center; user-select:none; }}
    .s3-badge {{ position:absolute; left:50%; top:130px; transform:translateX(-50%);
      background:{accent}; color:{txt_on_accent}; font-size:62px; letter-spacing:2px;
      text-transform:uppercase; padding:22px 64px; border-radius:26px;
      box-shadow:0 10px 0 rgba(0,0,0,0.18); white-space:nowrap; opacity:0; }}
    .big-num {{ position:absolute; left:50%; top:470px; transform:translateX(-50%);
      font-size:540px; line-height:0.8; color:{accent}; opacity:0;
      text-shadow:0 14px 0 rgba(0,0,0,0.12); }}
    .hero-cut {{ position:absolute; left:50%; top:330px; transform:translateX(-50%);
      width:430px; height:560px; background-size:cover; background-position:center top;
      opacity:0; z-index:4; filter:drop-shadow(0 16px 36px rgba(0,0,0,0.30));
      border-radius:0 0 24px 24px; background-color:{hero_bg}; }}
    .hero-cut .hph {{ position:absolute; inset:0; display:flex; align-items:center;
      justify-content:center; font-size:230px; color:{hero_letter}; }}
    .rank-list {{ position:absolute; width:100%; top:935px; display:flex; flex-direction:column;
      gap:26px; padding:0 110px; z-index:6; }}
    .rank-row {{ display:flex; align-items:stretch; height:112px; opacity:0; }}
    .rank-name {{ flex:1; background:{accent}; color:#fff; display:flex; align-items:center;
      justify-content:center; font-size:52px; letter-spacing:2px; text-transform:uppercase;
      border-radius:22px 0 0 22px; box-shadow:0 9px 0 rgba(0,0,0,0.16); }}
    .rank-val {{ width:170px; background:{accent2}; color:{val_txt}; display:flex;
      align-items:center; justify-content:center; font-size:58px;
      border-radius:0 22px 22px 0; box-shadow:0 9px 0 rgba(0,0,0,0.16); }}
    .s4-bg {{ background: radial-gradient(ellipse at 50% 45%, {dark} 0%, #040404 75%); }}
    .cta-main {{ position:absolute; width:100%; top:760px; text-align:center; color:{team_bg};
      font-size:96px; text-transform:uppercase; line-height:1.06; opacity:0; padding:0 70px;
      text-shadow:0 0 60px {glow_color}73, 0 6px 22px rgba(0,0,0,0.9); }}
    .cta-sub {{ position:absolute; width:100%; top:1060px; text-align:center;
      color:rgba(255,255,255,0.92); font-family:'Archivo', Arial, sans-serif; font-weight:700;
      font-size:46px; letter-spacing:1px; opacity:0; }}
    .cta-sub2 {{ position:absolute; width:100%; top:1150px; text-align:center;
      color:rgba(255,255,255,0.55); font-family:'Archivo', Arial, sans-serif; font-weight:700;
      font-size:36px; opacity:0; }}
    .flash {{ position:absolute; inset:0; background:#fff; opacity:0; z-index:90; }}
    .wm {{ position:absolute; bottom:56px; width:100%; text-align:center;
      color:rgba(255,255,255,0.55); font-family:'Archivo', Arial, sans-serif; font-weight:700;
      font-size:30px; letter-spacing:4px; z-index:80; text-shadow:0 2px 8px rgba(0,0,0,0.6); }}
    .vig {{ position:absolute; inset:0; z-index:70; pointer-events:none;
      background: radial-gradient(ellipse at 50% 50%, transparent 55%, rgba(0,0,0,0.42) 100%); }}
  </style>
</head>
<body>
<div id="main" data-composition-id="main" data-start="0" data-duration="38"
     data-width="1080" data-height="1920">

  <div id="s1" class="clip scene s1-bg" data-start="0" data-duration="6" data-track-index="1">
    <div class="s1-title" id="s1t">
      <span class="w" id="s1w1">{title_l1}</span>
      <span class="w" id="s1w2">{title_l2}</span>
    </div>
    <div class="glow-pad" id="glow1"></div>
    <div class="player-row">
      <div class="cutout" id="cut1" style="z-index:1; transform:translateX(70px) scale(0.92); {cut1_img}">
        <div class="ph"><div class="circle">{p2_initial}</div><div class="nm">{p2_name}</div></div>
      </div>
      <div class="cutout" id="cut2" style="z-index:3; {cut2_img}">
        <div class="ph"><div class="circle">{p1_initial}</div><div class="nm">{p1_name}</div></div>
      </div>
      <div class="cutout" id="cut3" style="z-index:1; transform:translateX(-70px) scale(0.92); {cut3_img}">
        <div class="ph"><div class="circle">{p3_initial}</div><div class="nm">{p3_name}</div></div>
      </div>
    </div>
  </div>

  <div id="s2" class="clip scene s2-bg" data-start="6" data-duration="7" data-track-index="1">
    <div class="face-stack">
      <div class="face" id="f1" style="background-color:#2a2a2a; {face1_img}"><div class="fph">{p1_initial}</div></div>
      <div class="face" id="f2" style="background-color:#222; {face2_img}"><div class="fph">{p2_initial}</div></div>
      <div class="face" id="f3" style="background-color:#1c1c1c; {face3_img}"><div class="fph">{p3_initial}</div></div>
    </div>
    <div class="s2-line" id="s2line">{hook_line}</div>
  </div>

  <div id="s3" class="clip scene s3-bg" data-start="13" data-duration="18" data-track-index="1">
    <div class="bg-pattern">{pattern_text}</div>
    <div class="s3-badge" id="badge3">{stat_title}</div>
    <div class="big-num" id="bignum">{top_value}</div>
    <div class="hero-cut" id="hero3" style="{hero_img}"><div class="hph">{p1_initial}</div></div>
    <div class="rank-list">
{rank_rows}
    </div>
  </div>

  <div id="s4" class="clip scene s4-bg" data-start="31" data-duration="7" data-track-index="1">
    <div class="cta-main" id="cta1">{cta_main}</div>
    <div class="cta-sub" id="cta2">{cta_sub}</div>
    <div class="cta-sub2" id="cta3">Subscribe · Golazo World TV ⚽</div>
  </div>

  <div id="flashA" class="clip flash" data-start="5.7" data-duration="0.6" data-track-index="10"></div>
  <div id="flashB" class="clip flash" data-start="12.7" data-duration="0.6" data-track-index="11"></div>
  <div id="flashC" class="clip flash" data-start="30.7" data-duration="0.6" data-track-index="12"></div>
  <div id="wm" class="clip wm" data-start="0" data-duration="38" data-track-index="20">@GOLAZOWORLDTV</div>
  <div id="vig" class="clip vig" data-start="0" data-duration="38" data-track-index="21"></div>
</div>

<script>
  window.__timelines = window.__timelines || {{}};
  const tl = gsap.timeline({{ paused: true }});

  tl.fromTo("#s1w1", {{y:-160, opacity:0, scale:1.25}},
    {{y:0, opacity:1, scale:1, duration:0.5, ease:"back.out(1.6)"}}, 0.25);
  tl.fromTo("#s1w2", {{y:-160, opacity:0, scale:1.25}},
    {{y:0, opacity:1, scale:1, duration:0.5, ease:"back.out(1.6)"}}, 0.45);
  tl.to("#glow1", {{opacity:1, duration:0.8, ease:"power2.out"}}, 0.9);
  tl.to("#glow1", {{scale:1.12, duration:4.5, ease:"sine.inOut"}}, 1.2);
  tl.fromTo("#cut2", {{y:220, opacity:0}}, {{y:0, opacity:1, duration:0.55, ease:"power3.out"}}, 1.0);
  tl.fromTo("#cut1", {{y:220, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, 1.2);
  tl.fromTo("#cut3", {{y:220, opacity:0}}, {{y:0, opacity:1, duration:0.5, ease:"power3.out"}}, 1.35);
  tl.to("#s1t", {{scale:1.04, duration:4, ease:"none", transformOrigin:"50% 0%"}}, 1.4);

  tl.fromTo("#flashA", {{opacity:0}}, {{opacity:0.9, duration:0.1}}, 5.75);
  tl.to("#flashA", {{opacity:0, duration:0.4}}, 5.88);

  tl.fromTo("#f1", {{x:-1080, opacity:0}}, {{x:0, opacity:1, duration:0.45, ease:"power4.out"}}, 6.1);
  tl.fromTo("#f2", {{x: 1080, opacity:0}}, {{x:0, opacity:1, duration:0.45, ease:"power4.out"}}, 6.3);
  tl.fromTo("#f3", {{x:-1080, opacity:0}}, {{x:0, opacity:1, duration:0.45, ease:"power4.out"}}, 6.5);
  tl.to(["#f1","#f2","#f3"], {{scale:1.07, duration:6, ease:"none", stagger:0.1}}, 6.6);
  tl.fromTo("#s2line", {{opacity:0, scale:2.4}},
    {{opacity:1, scale:1, duration:0.45, ease:"power4.in"}}, 7.3);
  tl.to("#s2line", {{scale:1.05, duration:5, ease:"sine.inOut"}}, 7.8);

  tl.fromTo("#flashB", {{opacity:0}}, {{opacity:0.9, duration:0.1}}, 12.75);
  tl.to("#flashB", {{opacity:0, duration:0.4}}, 12.88);

  tl.fromTo("#badge3", {{y:-200, opacity:0}},
    {{y:0, opacity:1, duration:0.55, ease:"bounce.out"}}, 13.2);
  tl.fromTo("#bignum", {{scale:3, opacity:0}},
    {{scale:1, opacity:1, duration:0.5, ease:"power4.in"}}, 13.8);
  tl.fromTo("#hero3", {{y:160, opacity:0}},
    {{y:0, opacity:1, duration:0.55, ease:"power3.out"}}, 14.15);

  const rows = {rows_js};
  rows.forEach((r,i)=>{{
    const fromX = i % 2 === 0 ? -1080 : 1080;
    tl.fromTo(r.row, {{x:fromX, opacity:0}},
      {{x:0, opacity:1, duration:0.5, ease:"power4.out"}}, r.t);
    const counter = {{v:0}};
    tl.to(counter, {{
      v: r.n, duration:0.8, ease:"power2.out",
      onUpdate(){{ document.querySelector(r.val).textContent = Math.round(counter.v); }}
    }}, r.t + 0.25);
  }});

  tl.to("#bignum", {{scale:1.08, duration:0.35, ease:"power2.inOut", yoyo:true, repeat:3}}, 20.5);
  tl.to("#s3 .rank-list", {{y:-8, duration:8, ease:"none"}}, 21);

  tl.fromTo("#flashC", {{opacity:0}}, {{opacity:0.9, duration:0.1}}, 30.75);
  tl.to("#flashC", {{opacity:0, duration:0.4}}, 30.88);

  tl.fromTo("#cta1", {{y:120, opacity:0, scale:0.8}},
    {{y:0, opacity:1, scale:1, duration:0.6, ease:"back.out(1.4)"}}, 31.2);
  tl.fromTo("#cta2", {{y:60, opacity:0}},
    {{y:0, opacity:1, duration:0.45, ease:"power3.out"}}, 31.8);
  tl.fromTo("#cta3", {{y:40, opacity:0}}, {{y:0, opacity:0.55, duration:0.4}}, 32.2);
  tl.to("#cta1", {{scale:1.04, duration:0.9, ease:"sine.inOut", yoyo:true, repeat:5}}, 32.8);

  tl.to("#main", {{opacity:0, duration:0.7}}, 37.2);

  window.__timelines["main"] = tl;
</script>
</body>
</html>
"""


def hexa(h, alpha_hex):
    """color + alpha en hex CSS."""
    return f"{h}{alpha_hex}"


def img_style(path):
    if path and os.path.exists(path):
        return f"background-image:url('{path}');"
    return ""


def generate(config_path: str, out_path: str = "index.html"):
    with open(config_path, encoding="utf-8") as f:
        cfg = json.load(f)

    team_key = cfg.get("team", "brasil").lower()
    team = TEAMS.get(team_key, TEAMS["brasil"])
    players = cfg["players"][:5]
    while len(players) < 5:
        players.append({"name": "—", "value": 0})

    top = players[0]
    code = team["code"]
    pattern_text = "\n".join([f"{code} {code} {code}"] * 4)

    # Filas del ranking
    rank_rows = ""
    rows_js = []
    base_t = 15.2
    for i, p in enumerate(players, 1):
        rank_rows += (
            f'      <div class="rank-row" id="r{i}">'
            f'<div class="rank-name">{p["name"]}</div>'
            f'<div class="rank-val" id="v{i}">0</div></div>\n'
        )
        rows_js.append({"row": f"#r{i}", "val": f"#v{i}",
                        "n": p["value"], "t": round(base_t + (i-1)*0.8, 1)})

    title_words = cfg.get("title_es", "LA MURALLA|DE BRASIL").split("|")
    title_l1 = title_words[0]
    title_l2 = title_words[1] if len(title_words) > 1 else ""
    # Ajustar tamaño según largo
    longest = max(len(title_l1), len(title_l2))
    title_size = 150 if longest <= 11 else (120 if longest <= 15 else 96)

    p_dir = cfg.get("players_img_dir", "assets/players")
    def pimg(idx):
        for ext in ("png","jpg","webp"):
            p = os.path.join(p_dir, f"p{idx}.{ext}")
            if os.path.exists(p):
                return img_style(p)
        return ""

    html = TEMPLATE.format(
        title_size   = title_size,
        title_l1     = title_l1,
        title_l2     = title_l2,
        glow_color   = team["bg"],
        team_bg      = team["bg"],
        accent       = team["accent"],
        accent2      = team["accent2"],
        txt_on_accent= team["txt_on_accent"],
        val_txt      = team["val_txt"],
        dark         = team["dark"],
        pattern_color= hexa(team["accent"], "29"),
        pattern_text = pattern_text,
        hero_bg      = hexa(team["accent"], "38"),
        hero_letter  = hexa(team["accent"], "8c"),
        hook_line    = cfg.get("hook_es", "NADIE LES GANA<br>UN DUELO"),
        stat_title   = cfg.get("stat_title_es", "Duelos ganados"),
        top_value    = top["value"],
        cta_main     = cfg.get("cta_es", "¿GANAN EL<br>MUNDIAL 2026?"),
        cta_sub      = cfg.get("cta_sub_es", "Comentá SÍ o NO 👇"),
        p1_initial   = players[0]["name"][0].upper(),
        p2_initial   = players[1]["name"][0].upper(),
        p3_initial   = players[2]["name"][0].upper(),
        p1_name      = players[0]["name"],
        p2_name      = players[1]["name"],
        p3_name      = players[2]["name"],
        cut1_img     = pimg(2), cut2_img = pimg(1), cut3_img = pimg(3),
        face1_img    = pimg(1), face2_img = pimg(2), face3_img = pimg(3),
        hero_img     = pimg(1) + f"background-color:{hexa(team['accent'],'38')};",
        rank_rows    = rank_rows.rstrip(),
        rows_js      = json.dumps(rows_js),
    )

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Generado: {out_path}")
    print(f"   Equipo: {team_key.upper()} · Stat: {cfg.get('stat_title_es','')}")
    print(f"   Top: {top['name']} ({top['value']})")
    print(f"\n   Preview:  hyperframes preview {out_path}")
    print(f"   Render:   hyperframes render {out_path} --output output/short.mp4")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 make_short.py configs/brasil_duelos.json [output.html]")
        sys.exit(1)
    out = sys.argv[2] if len(sys.argv) > 2 else "index.html"
    generate(sys.argv[1], out)
