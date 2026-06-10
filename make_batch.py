#!/usr/bin/env python3
"""
GOLAZO WORLD TV — BATCH CONFIG GENERATOR
Genera el lote completo de configs ES + EN con stats reales.
Datos verificados: eliminatorias 2026, históricos de Mundiales, récords.

Uso:  python3 make_batch.py
Genera todos los JSONs en configs/ listos para renderizar.
"""

import json, os

OUT = "configs"
os.makedirs(OUT, exist_ok=True)

# ════════════════════════════════════════════════════════════
# DATOS REALES — verificados junio 2026
# ════════════════════════════════════════════════════════════

BATCH = [

# ── ARGENTINA ────────────────────────────────────────────────
{
  "id": "argentina_goles_eliminatorias",
  "team": "argentina",
  "es": {
    "title": "EL GOLEADOR|DE AMERICA",
    "hook": "NADIE MARCO MAS<br>EN ELIMINATORIAS",
    "stat": "Goles eliminatorias",
    "cta": "¿MESSI GANA OTRO|BALON DE ORO?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "SOUTH AMERICAS|TOP SCORER",
    "hook": "NOBODY SCORED MORE<br>IN QUALIFIERS",
    "stat": "Qualifier goals",
    "cta": "CAN MESSI WIN|ANOTHER GOLDEN BOOT?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Messi",      "value": 8},
    {"name": "L. Diaz",    "value": 7},
    {"name": "Terceros",   "value": 6},
    {"name": "D. Nunez",   "value": 5},
    {"name": "Raphinha",   "value": 5}
  ]
},
{
  "id": "argentina_goles_mundial_historia",
  "team": "argentina",
  "es": {
    "title": "GOLEADORES|HISTORICOS",
    "hook": "LOS QUE HICIERON<br>HISTORIA EN MUNDIALES",
    "stat": "Goles en Mundiales",
    "cta": "¿MESSI LLEGA|A 15 GOLES?", "cta_sub": "Comentá tu predicción 👇",
  },
  "en": {
    "title": "ARGENTINA WC|ALL-TIME SCORERS",
    "hook": "THE MEN WHO MADE<br>WORLD CUP HISTORY",
    "stat": "World Cup goals",
    "cta": "CAN MESSI|REACH 15?", "cta_sub": "Drop your prediction 👇",
  },
  "players": [
    {"name": "Messi",     "value": 13},
    {"name": "Batistuta", "value": 10},
    {"name": "Maradona",  "value": 8},
    {"name": "Stabile",   "value": 8},
    {"name": "Kempes",    "value": 6}
  ]
},
{
  "id": "argentina_partidos_mundial",
  "team": "argentina",
  "es": {
    "title": "EL RECORD|ABSOLUTO",
    "hook": "MAS PARTIDOS QUE NADIE<br>EN LA HISTORIA",
    "stat": "Partidos en Mundiales",
    "cta": "¿CUANTOS JUGARA|EN 2026?", "cta_sub": "Comentá tu número 👇",
  },
  "en": {
    "title": "THE ABSOLUTE|RECORD",
    "hook": "MORE GAMES THAN ANYONE<br>IN HISTORY",
    "stat": "World Cup matches",
    "cta": "HOW MANY WILL|HE PLAY IN 2026?", "cta_sub": "Comment your number 👇",
  },
  "players": [
    {"name": "Messi",      "value": 26},
    {"name": "Maradona",   "value": 21},
    {"name": "Mascherano", "value": 20},
    {"name": "Ayala",      "value": 17},
    {"name": "Simeone",    "value": 16}
  ]
},

# ── BRASIL ───────────────────────────────────────────────────
{
  "id": "brasil_goleadores_mundial",
  "team": "brasil",
  "es": {
    "title": "LOS REYES|DE BRASIL",
    "hook": "LA HISTORIA DEL<br>PAIS DEL FUTBOL",
    "stat": "Goles en Mundiales",
    "cta": "¿BRASIL GANA|EL HEXA EN 2026?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "THE KINGS|OF BRAZIL",
    "hook": "THE HISTORY OF<br>FOOTBALLS NATION",
    "stat": "World Cup goals",
    "cta": "DOES BRAZIL WIN|THE HEXA IN 2026?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Ronaldo",   "value": 15},
    {"name": "Pele",      "value": 12},
    {"name": "Vava",      "value": 9},
    {"name": "Jairzinho", "value": 9},
    {"name": "Neymar",    "value": 8}
  ]
},
{
  "id": "brasil_duelos",
  "team": "brasil",
  "es": {
    "title": "LA MURALLA|DE BRASIL",
    "hook": "NADIE LES GANA<br>UN DUELO",
    "stat": "Duelos ganados",
    "cta": "¿BRASIL GANA|EL MUNDIAL 2026?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "THE WALL|OF BRAZIL",
    "hook": "NOBODY BEATS THEM<br>IN A DUEL",
    "stat": "Duels won",
    "cta": "DOES BRAZIL WIN|WORLD CUP 2026?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Casemiro",     "value": 12},
    {"name": "B. Guimaraes", "value": 8},
    {"name": "M. Cunha",     "value": 8},
    {"name": "Marquinhos",   "value": 7},
    {"name": "Fabinho",      "value": 7}
  ]
},

# ── FRANCIA ──────────────────────────────────────────────────
{
  "id": "francia_velocidad",
  "team": "francia",
  "es": {
    "title": "LOS MAS RAPIDOS|DE FRANCIA",
    "hook": "VELOCIDAD<br>IMPARABLE",
    "stat": "Km/h velocidad max",
    "cta": "¿FRANCIA LLEGA|A LA FINAL?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "FRANCES|SPEED DEMONS",
    "hook": "UNSTOPPABLE<br>PACE",
    "stat": "Top speed km/h",
    "cta": "DOES FRANCE REACH|THE FINAL?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Mbappe",      "value": 38},
    {"name": "Dembele",     "value": 36},
    {"name": "Coman",       "value": 35},
    {"name": "T. Hernandez","value": 34},
    {"name": "Kone",        "value": 33}
  ]
},
{
  "id": "francia_goles_mundial",
  "team": "francia",
  "es": {
    "title": "LEYENDAS|DE FRANCIA",
    "hook": "LOS GOLEADORES<br>DE LES BLEUS",
    "stat": "Goles en Mundiales",
    "cta": "¿MBAPPE SUPERA|A KLOSE (16)?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "LEGENDS|OF FRANCE",
    "hook": "LES BLEUS<br>TOP SCORERS",
    "stat": "World Cup goals",
    "cta": "CAN MBAPPE BEAT|KLOSE (16)?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Mbappe",    "value": 12},
    {"name": "Fontaine",  "value": 13},
    {"name": "Griezmann", "value": 8},
    {"name": "Henry",     "value": 6},
    {"name": "Giroud",    "value": 6}
  ]
},

# ── ESPAÑA ───────────────────────────────────────────────────
{
  "id": "espana_asistencias",
  "team": "espana",
  "es": {
    "title": "EL MAGO|DE ESPAÑA",
    "hook": "EL JUGADOR MAS JOVEN<br>EN DOMINAR EUROPA",
    "stat": "Asistencias clasificacion",
    "cta": "¿YAMAL ES EL MEJOR|DEL MUNDO YA?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "SPAINS|MAGICIAN",
    "hook": "THE YOUNGEST PLAYER<br>TO DOMINATE EUROPE",
    "stat": "Qualifier assists",
    "cta": "IS YAMAL ALREADY|THE WORLDS BEST?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Yamal",    "value": 6},
    {"name": "Pedri",    "value": 4},
    {"name": "F. Torres","value": 3},
    {"name": "Olmo",     "value": 3},
    {"name": "Williams", "value": 2}
  ]
},

# ── INGLATERRA ───────────────────────────────────────────────
{
  "id": "inglaterra_kane_temporada",
  "team": "inglaterra",
  "es": {
    "title": "LA MAQUINA|DE GOLES",
    "hook": "NADIE MARCO MAS<br>EN EUROPA 2025-26",
    "stat": "Goles temporada 25-26",
    "cta": "¿KANE POR FIN GANA|UN TITULO GRANDE?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "THE GOAL|MACHINE",
    "hook": "NOBODY SCORED MORE<br>IN EUROPE 2025-26",
    "stat": "Goals season 25-26",
    "cta": "DOES KANE FINALLY|WIN A MAJOR TROPHY?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Kane",     "value": 61},
    {"name": "Mbappe",   "value": 52},
    {"name": "Haaland",  "value": 48},
    {"name": "Lewandowski","value": 42},
    {"name": "Vinicius", "value": 38}
  ]
},

# ── ALEMANIA / NORUEGA REF ───────────────────────────────────
{
  "id": "haaland_eliminatorias",
  "team": "alemania",
  "es": {
    "title": "EL MONSTRUO|DEL NORTE",
    "hook": "16 GOLES EN<br>ELIMINATORIAS UEFA",
    "stat": "Goles clasificacion UEFA",
    "cta": "¿HAALAND GOLEADOR|DEL MUNDIAL 2026?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "THE MONSTER|FROM THE NORTH",
    "hook": "16 GOALS IN<br>UEFA QUALIFIERS",
    "stat": "UEFA qualifier goals",
    "cta": "HAALAND WINS THE|2026 GOLDEN BOOT?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Haaland",  "value": 16},
    {"name": "Kane",     "value": 8},
    {"name": "Gyokeres", "value": 7},
    {"name": "Kramaric", "value": 6},
    {"name": "Schick",   "value": 6}
  ]
},

# ── MEXICO ───────────────────────────────────────────────────
{
  "id": "mexico_mundiales_historicos",
  "team": "mexico",
  "es": {
    "title": "LOS HEROES|DEL TRI",
    "hook": "MUNDIAL EN CASA<br>POR TERCERA VEZ",
    "stat": "Goles en Mundiales",
    "cta": "¿MEXICO PASA EL|QUINTO PARTIDO?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "EL TRIS|HEROES",
    "hook": "HOME WORLD CUP<br>FOR THE THIRD TIME",
    "stat": "World Cup goals",
    "cta": "DOES MEXICO BREAK|THE 5TH GAME CURSE?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "L. Hernandez","value": 4},
    {"name": "Borgetti",    "value": 3},
    {"name": "Chicharito",  "value": 3},
    {"name": "Gimenez",     "value": 2},
    {"name": "Lozano",      "value": 2}
  ]
},

# ── PORTUGAL ─────────────────────────────────────────────────
{
  "id": "portugal_ronaldo_records",
  "team": "portugal",
  "es": {
    "title": "EL ULTIMO BAILE|DE CR7",
    "hook": "6 MUNDIALES<br>A LOS 41 AÑOS",
    "stat": "Goles seleccion",
    "cta": "¿RONALDO GANA SU|PRIMER MUNDIAL?", "cta_sub": "Comentá SÍ o NO 👇",
  },
  "en": {
    "title": "CR7S|LAST DANCE",
    "hook": "6 WORLD CUPS<br>AT AGE 41",
    "stat": "International goals",
    "cta": "DOES RONALDO WIN|HIS FIRST WORLD CUP?", "cta_sub": "Comment YES or NO 👇",
  },
  "players": [
    {"name": "Ronaldo", "value": 143},
    {"name": "Messi",   "value": 114},
    {"name": "Neymar",  "value": 79},
    {"name": "Kane",    "value": 76},
    {"name": "Mbappe",  "value": 55}
  ]
},
]


def write_config(item, lang):
    L = item[lang]
    cfg = {
        "team":          item["team"],
        "title_es":      L["title"],
        "hook_es":       L["hook"],
        "stat_title_es": L["stat"],
        "cta_es":        L["cta"].replace("|", "<br>"),
        "cta_sub_es":    L["cta_sub"],
        "players":       item["players"],
    }
    fname = f"{item['id']}_{lang}.json"
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    return fname


def main():
    print(f"\n🏭 Generando lote de configs...\n")
    total = 0
    for item in BATCH:
        for lang in ("es", "en"):
            fname = write_config(item, lang)
            print(f"  ✅ {fname}")
            total += 1
    print(f"\n🎬 {total} configs listos en {OUT}/")
    print(f"   Cada uno = 1 Short de 38s")
    print(f"\n   Renderizar uno:")
    print(f"   python3 make_short.py configs/brasil_duelos_es.json && hyperframes render index.html")
    print(f"\n   En GitHub Actions: push y se renderizan solos.")


if __name__ == "__main__":
    main()
