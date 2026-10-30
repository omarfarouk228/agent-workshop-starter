"""Les trois outils du workshop : une base locale, une API distante, une recherche."""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import httpx

DB_PATH = Path(__file__).resolve().parent.parent / "notes.db"
GEO = "https://geocoding-api.open-meteo.com/v1/search"
METEO = "https://api.open-meteo.com/v1/forecast"
WIKI = "https://fr.wikipedia.org/w/api.php"
HEADERS = {"User-Agent": "AgentWorkshopStarter/1.0 (https://github.com/omarfarouk228/agent-workshop-starter)"}


def _connect() -> sqlite3.Connection:
    db = sqlite3.connect(DB_PATH)
    db.execute(
        "CREATE TABLE IF NOT EXISTS notes ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, created_at TEXT)"
    )
    return db


# Module 2 : outil local
def save_note(title: str, content: str) -> dict:
    """Sauvegarde une note (titre + contenu) dans la base locale."""
    with _connect() as db:
        cur = db.execute(
            "INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, datetime.now(timezone.utc).isoformat()))
    return {"id": cur.lastrowid, "status": "saved"}


# Module 2 : outil distant
async def get_weather(city: str) -> dict:
    """Météo actuelle d'une ville : température (°C) et vent (km/h)."""
    async with httpx.AsyncClient(timeout=10) as http:
        geo = (await http.get(GEO, params={"name": city, "count": 1})).json()
        if not geo.get("results"):
            return {"error": f"Ville introuvable : {city}"}
        place = geo["results"][0]
        r = await http.get(METEO, params={
            "latitude": place["latitude"], "longitude": place["longitude"],
            "current": "temperature_2m,wind_speed_10m"})
    now = r.json()["current"]
    return {"city": place["name"], "temp_c": now["temperature_2m"],
            "wind_kmh": now["wind_speed_10m"]}


# Bonus : recherche (Wikipédia FR, gratuit et sans clé)
async def search_web(query: str) -> dict:
    """Recherche des informations factuelles sur Wikipédia (français)."""
    async with httpx.AsyncClient(timeout=10, headers=HEADERS) as http:
        r = await http.get(WIKI, params={
            "action": "query", "list": "search", "srsearch": query,
            "srlimit": 3, "format": "json"})
    hits = r.json()["query"]["search"]
    return {"results": [
        {"title": h["title"],
         "snippet": h["snippet"].replace('<span class="searchmatch">', "").replace("</span>", ""),
         "url": "https://fr.wikipedia.org/wiki/" + h["title"].replace(" ", "_")}
        for h in hits]}
