"""
app.py
------
Serveur web FastAPI pour Football Analytics Bot.

Pages HTML :
  GET /            → Dashboard principal
  GET /sandbox     → Simulation Lab
  GET /performance → Performance
  GET /recherche   → Discovery / Recherche

API JSON :
  GET /api/competitions                          → liste des compétitions
  GET /api/matches/{competition_id}/{season_id}  → matchs d'une saison
  GET /api/match/{match_id}                      → stats détaillées d'un match
  GET /api/team-form                             → forme récente d'une équipe
  GET /api/dashboard                             → résumé pour le Dashboard
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from services.data_collector import (
    get_competitions,
    get_matches,
    get_match_stats,
    get_team_form,
    get_dashboard_summary,
)

app = FastAPI(title="Football Analytics Bot", version="0.1.0")

# Autoriser les requêtes cross-origin (utile pour le futur)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


# ─────────────────────────────────────────────
# PAGES HTML
# ─────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    """Dashboard principal, alimenté par des données réelles."""
    data = get_dashboard_summary()
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"data": data}
    )

@app.get("/sandbox", response_class=HTMLResponse)
async def read_sandbox(request: Request):
    """Page Simulation Lab."""
    return templates.TemplateResponse(request=request, name="sandbox.html")

@app.get("/performance", response_class=HTMLResponse)
async def read_performance(request: Request):
    """Page Performance."""
    return templates.TemplateResponse(request=request, name="performance.html")

@app.get("/recherche", response_class=HTMLResponse)
async def read_recherche(request: Request):
    """Page Discovery / Recherche."""
    competitions = get_competitions()
    return templates.TemplateResponse(
        request=request,
        name="recherche.html",
        context={"competitions": competitions}
    )


# ─────────────────────────────────────────────
# API JSON
# ─────────────────────────────────────────────

@app.get("/api/competitions")
async def api_competitions():
    """Retourne toutes les compétitions disponibles (StatsBomb Open Data)."""
    return get_competitions()


@app.get("/api/matches/{competition_id}/{season_id}")
async def api_matches(competition_id: int, season_id: int):
    """Retourne tous les matchs d'une compétition/saison donnée."""
    return get_matches(competition_id, season_id)


@app.get("/api/match/{match_id}")
async def api_match_stats(match_id: int):
    """Retourne les statistiques détaillées d'un match (tirs, xG, passes...)."""
    return get_match_stats(match_id)


@app.get("/api/team-form")
async def api_team_form(
    competition_id: int,
    season_id: int,
    team: str,
    n: int = 5
):
    """
    Retourne la forme récente d'une équipe sur ses N derniers matchs.
    Exemple : /api/team-form?competition_id=16&season_id=44&team=Real+Madrid&n=5
    """
    return get_team_form(competition_id, season_id, team, n)


@app.get("/api/dashboard")
async def api_dashboard():
    """Retourne le résumé complet pour le Dashboard (JSON brut)."""
    return get_dashboard_summary()


# ─────────────────────────────────────────────
# LANCEMENT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    print("Démarrage du serveur → http://localhost:8000")
    print("Documentation API   → http://localhost:8000/docs")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
