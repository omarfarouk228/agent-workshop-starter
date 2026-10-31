# Ce qu'il faut installer avant le workshop

Comptez environ 20 minutes. Tout est gratuit.

## Obligatoire

| Outil | Version | Où le trouver |
|---|---|---|
| Python | 3.11 ou plus récent | https://www.python.org/downloads/ |
| Git | toute version récente | https://git-scm.com/downloads |
| Un éditeur de code | VS Code conseillé | https://code.visualstudio.com |
| Un compte Google | pour la clé Gemini | https://aistudio.google.com/apikey |

Vérifiez dans un terminal :

```bash
python --version     # macOS / Linux : python3 --version
git --version
```

## Pour le module 3 (MCP)

| Outil | Version | Où le trouver |
|---|---|---|
| Node.js | 20 ou plus récent (LTS) | https://nodejs.org (prenez l'installeur LTS) |
| Gemini CLI | dernière version | `npm install -g @google/gemini-cli` |

Vérifiez :

```bash
node --version
gemini --version
```

Sur macOS, si `brew install node` se met à compiler pendant des heures, arrêtez-le et prenez l'installeur `.pkg` de nodejs.org.

## Optionnel

- **Dart 3** (ou Flutter) pour la version Dart des outils : https://dart.dev/get-dart
- **Claude Code** (abonnement Claude requis) : https://claude.com/claude-code

## Ensuite : récupérer le code et la clé

```bash
git clone https://github.com/omarfarouk228/agent-workshop-starter
cd agent-workshop-starter
python -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example assistant_agent/.env   # Windows : copy .env.example assistant_agent\.env
```

Créez votre clé sur https://aistudio.google.com/apikey (« Create API key ») et collez-la dans `assistant_agent/.env`.

## Dernière vérification

```bash
python scripts/check_setup.py
```

Tout doit être ✅. Le jour J, venez avec votre ordinateur **chargé** et son chargeur.
