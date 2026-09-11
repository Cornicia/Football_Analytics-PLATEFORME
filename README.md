# Football Analytics

Application FastAPI de collecte et d'analyse de donnees football.

## Fonctionnalites

- Matchs historiques via StatsBomb Open Data.
- Matchs des saisons 2025/2026 et 2026/2027 via API-Football.
- Pronostics et cotes actuelles via The Odds API.
- Dashboard, recherche, simulation et indicateurs de performance.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuration

Definir les cles dans le terminal avant de lancer l'application :

```powershell
$env:API_FOOTBALL_KEY="votre_cle_api_football"
$env:THE_ODDS_API_KEY="votre_cle_the_odds_api"
```

Ne jamais committer les vraies cles. Le fichier `.env.example` contient uniquement les noms attendus.
Les cles doivent rester dans les variables d'environnement locales ou dans un gestionnaire de secrets.
Les fichiers `.env`, `*.key`, `*.pem`, `secrets/` et `.secrets/` sont ignores par Git.

Sources :

- API-Football : https://dashboard.api-football.com/
- The Odds API : https://the-odds-api.com/
- StatsBomb Open Data : https://github.com/statsbomb/open-data

## Lancement

```powershell
python app.py
```

- Dashboard : http://127.0.0.1:8000/
- Documentation API : http://127.0.0.1:8000/docs
- Performance : http://127.0.0.1:8000/performance
- Recherche : http://127.0.0.1:8000/recherche

## API principales

- `GET /api/competitions`
- `GET /api/matches/{competition_id}/{season_id}`
- `GET /api/dashboard`
- `GET /api/performance`

## Regle de maintenance

Chaque push doit inclure un README a jour lorsque les fonctionnalites, les sources de donnees, les variables d'environnement ou les commandes changent.
