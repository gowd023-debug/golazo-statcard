# ⚽ GolazoWorldTV — Stat Card Shorts (100% automático)

Motion graphics estilo viral: stat cards animadas con ranking de jugadores.
**Sin metraje de partidos = sin copyright = sin clips sucios.**

## Generar un Short nuevo (3 pasos)

1. **Crear config** — copiá un JSON de `configs/` y cambiá los datos:
```json
{
  "team": "argentina",
  "title_es": "LOS GOLEADORES|DE ARGENTINA",
  "hook_es": "ELLOS DECIDEN<br>LOS PARTIDOS",
  "stat_title_es": "Goles en 2026",
  "cta_es": "¿ARGENTINA<br>BACK TO BACK?",
  "players": [
    {"name": "Messi", "value": 9},
    {"name": "Lautaro", "value": 7}
  ]
}
```

2. **Push a GitHub** → Actions renderiza solo (~5 min)

3. **Descargar el MP4** desde Artifacts → subir a YouTube/TikTok/IG

## Preview en tu Mac (sin renderizar — liviano)
```bash
npm install -g hyperframes --ignore-scripts
python3 make_short.py configs/brasil_duelos.json
hyperframes preview index.html
```

## Equipos con paleta lista
brasil · argentina · francia · espana · inglaterra · mexico · alemania · portugal

## Fotos de jugadores (opcional)
Poné PNGs recortados en `assets/players/` como `p1.png`, `p2.png`, `p3.png`
(p1 = jugador #1 del ranking). Si no hay fotos, usa placeholders con iniciales.
Fuentes de cutouts: SofaScore, Transfermarkt, futhead.

## Estructura del Short (38s)
| Escena | Tiempo | Contenido |
|---|---|---|
| 1 Intro | 0-6s | Título gigante + 3 jugadores con glow |
| 2 Hook | 6-13s | Caras B&W apiladas + fondo rojo + frase gancho |
| 3 Stat | 13-31s | Card del equipo + ranking animado + contadores |
| 4 CTA | 31-38s | Pregunta a la comunidad |
