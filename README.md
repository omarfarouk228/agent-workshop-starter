# Agent Workshop Starter

Code du workshop **« Construire un agent IA qui agit vraiment »**, Lomé 2026.

Un agent Python construit avec [Google ADK](https://google.github.io/adk-docs/) et Gemini, avec trois outils réels, puis exposé à Gemini CLI et Claude Code via un serveur [MCP](https://modelcontextprotocol.io).

| Outil | Type | Source |
|---|---|---|
| `save_note` | local | SQLite (`notes.db`) |
| `get_weather` | distant | Open-Meteo (gratuit, sans clé) |
| `search_web` | distant | Wikipédia FR (gratuit, sans clé) |

## Installation (à faire avant le workshop)

La liste complète des outils à installer est dans [INSTALLATION.md](INSTALLATION.md). En résumé : Python 3.11+, Git, et Node 20+ pour le module 3.

```bash
git clone https://github.com/omarfarouk228/agent-workshop-starter
cd agent-workshop-starter
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example assistant_agent/.env
```

Ouvrez `assistant_agent/.env` et collez votre clé Gemini gratuite, créée sur [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

Vérifiez ensuite que tout est prêt :

```bash
python scripts/check_setup.py
```

Tout doit être ✅ avant d'arriver.

## Lancer l'agent (modules 1 et 2)

Depuis la racine du repo :

```bash
adk web          # interface de test sur http://localhost:8000
# ou
adk run assistant_agent   # dans le terminal
```

Essayez : *« Note : réunion demain 10h sur l'agent IA. Et quelle météo à Lomé ? »*

## Serveur MCP (module 3)

```bash
mcp dev demo_mcp_server.py      # MCP Inspector (nécessite Node)
```

Les serveurs MCP sont **déjà déclarés dans le repo**, avec des chemins relatifs :

- `.mcp.json` pour Claude Code
- `.gemini/settings.json` pour Gemini CLI

Ils déclarent `demo` (Python) et `demo-dart` (lancez `cd dart_mcp_server && dart pub get` une première fois). Windows : remplacez `.venv/bin/python` par `.venv\Scripts\python.exe`.

### Gemini CLI (gratuit)

```bash
npm install -g @google/gemini-cli
gemini            # depuis la racine du repo
```

Au premier lancement, **acceptez de faire confiance au dossier**. Dans un dossier non approuvé, Gemini CLI désactive tous les serveurs MCP. Tapez ensuite `/mcp` : `demo` et `demo-dart` doivent être connectés.

### Claude Code (abonnement Claude requis)

```bash
claude            # depuis la racine du repo
```

Approuvez les serveurs de `.mcp.json` quand Claude Code le propose, puis vérifiez avec `/mcp`.

### Claude Desktop (optionnel)

Éditez `~/Library/Application Support/Claude/claude_desktop_config.json` (Windows : `%APPDATA%\Claude\claude_desktop_config.json`) avec le même bloc `mcpServers`, mais en chemins **absolus**, puis redémarrez Claude Desktop.

## Version Dart

Google ADK n'a pas de SDK Dart officiel, mais grâce à MCP les outils peuvent être écrits en Dart : voir [`dart_mcp_server/`](dart_mcp_server/). L'agent Python peut les utiliser directement (exercice 3.4).

## Structure

```
assistant_agent/
  agent.py        # l'agent ADK (root_agent)
  tools.py        # save_note, get_weather, search_web
  .env            # votre clé (non versionnée)
demo_mcp_server.py  # les mêmes outils exposés en MCP
.mcp.json           # serveurs MCP pour Claude Code
.gemini/            # serveurs MCP pour Gemini CLI
dart_mcp_server/    # les outils en Dart, exposés en MCP
scripts/check_setup.py
INSTALLATION.md   # ce qu'il faut installer
EXERCICES.md      # la pratique, avec solutions
```

## Exercices

Voir [EXERCICES.md](EXERCICES.md).

## Problèmes fréquents

| Symptôme | Solution |
|---|---|
| `mcp dev` : le serveur ne démarre pas | Lancez-le depuis la racine du repo, venv activé : il réutilise `.venv` |
| Gemini CLI : serveurs MCP « Disabled » | Le dossier n'est pas approuvé : relancez `gemini` depuis la racine du repo et acceptez de lui faire confiance |
| macOS : `brew install node` compile pendant des heures | Votre macOS n'a plus de bottles Homebrew : installez le `.pkg` LTS de https://nodejs.org |
| `adk web` ne trouve pas l'agent | Lancez-le depuis la racine du repo, pas depuis `assistant_agent/` |
| `No module named 'mcp.server.fastmcp'` | mcp 2.x a renommé `FastMCP` en `MCPServer` : `from mcp.server.mcpserver import MCPServer` |
| Claude Code / Gemini CLI ne voient pas « demo » | Lancez-les depuis la racine du repo, venv créé dans `.venv` |
| Gemini répond `429` | Quota gratuit atteint : attendez une minute ou utilisez une autre clé |
| L'agent ne répond plus | Testez un autre modèle dans `agent.py` (`gemini-2.5-flash-lite`) |
