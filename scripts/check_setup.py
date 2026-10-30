"""Vérifie que tout est prêt pour le workshop : python scripts/check_setup.py"""
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ok = True


def check(label: str, passed: bool, hint: str = "", optional: bool = False) -> None:
    global ok
    ok &= passed or optional
    mark = "✅" if passed else ("⚠️ " if optional else "❌")
    print(f"  {mark} {label}" + ("" if passed else f"\n     → {hint}"))


def load_env() -> None:
    env = ROOT / "assistant_agent" / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


print("\nPréparation du workshop Agent IA\n")

check(f"Python {sys.version.split()[0]}", sys.version_info >= (3, 11),
      "Installer Python 3.11 ou plus récent : https://www.python.org/downloads/")
check("Environnement virtuel actif", sys.prefix != sys.base_prefix,
      "source .venv/bin/activate   (Windows : .venv\\Scripts\\activate)")
for mod, pkg in [("google.adk", "google-adk"), ("mcp", "mcp[cli]"), ("httpx", "httpx")]:
    check(f"Paquet {pkg}", importlib.util.find_spec(mod) is not None,
          "pip install -r requirements.txt")

node = shutil.which("node")
version = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip() if node else ""
check(f"Node {version or 'absent'} (module 3)",
      bool(version) and int(version.lstrip("v").split(".")[0]) >= 20,
      "Recommandé : Node 20+ (https://nodejs.org) pour le module 3 (MCP Inspector, Gemini CLI)",
      optional=True)

dart = shutil.which("dart")
check("Dart (optionnel, version Dart)", bool(dart),
      "Optionnel : https://dart.dev/get-dart pour le serveur MCP en Dart", optional=True)

load_env()
key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or ""
check("Clé API Gemini trouvée", key.startswith("AIza"),
      "cp .env.example assistant_agent/.env puis coller la clé de https://aistudio.google.com/apikey")

if ok:
    import asyncio

    import httpx

    async def network() -> None:
        async with httpx.AsyncClient(timeout=10) as http:
            try:
                r = await http.get("https://generativelanguage.googleapis.com/v1beta/models",
                                   params={"key": key, "pageSize": 1})
                check("Clé Gemini valide", r.status_code == 200,
                      f"HTTP {r.status_code} : clé invalide ou API non activée")
            except httpx.HTTPError as e:
                check("Accès à l'API Gemini", False, f"Réseau : {e}")
        sys.path.insert(0, str(ROOT))
        from assistant_agent.tools import get_weather
        try:
            w = await get_weather("Lomé")
            check(f"Outil get_weather ({w.get('temp_c')} °C à Lomé)", "temp_c" in w, str(w))
        except httpx.HTTPError as e:
            check("Accès à Open-Meteo", False, f"Réseau : {e}")

    asyncio.run(network())

print("\n🎉 Tout est prêt, à bientôt au workshop !\n" if ok
      else "\n⚠️  Corrigez les points ❌ ci-dessus avant le workshop.\n")
sys.exit(0 if ok else 1)
