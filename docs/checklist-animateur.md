# Checklist animateur

## J-7
- [ ] Repo `agent-workshop-starter` poussé et **public**
- [ ] Message de préparation envoyé (`docs/message-participants.md`)
- [ ] Vérifier que `requirements.txt` s'installe sur une machine vierge (Windows compris)

## J-1
- [ ] Rappel envoyé aux participants
- [ ] `python scripts/check_setup.py` tout vert sur la machine de démo
- [ ] Lancer les 2 démos de bout en bout (agent ADK, puis Gemini CLI et Claude Code)
- [ ] Vérifier que `gemini-2.5-flash` répond rapidement, sinon basculer sur `gemini-2.5-flash-lite` dans `agent.py`
- [ ] `notes.db` de démo vidé (`rm notes.db`) pour que la démo 1 affiche un ID propre
- [ ] `gemini` puis `/mcp` depuis la racine du repo : `demo` et `demo-dart` connectés (dossier approuvé)
- [ ] `claude` depuis la racine du repo : serveurs de `.mcp.json` approuvés, `/mcp` les montre connectés
- [ ] `mcp dev demo_mcp_server.py` depuis la racine du repo : l'Inspector s'ouvre sur le port 6274
- [ ] Repo cloné sur une clé USB avec les wheels (`pip download -r requirements.txt -d wheels/`, une fois par OS) en cas de wifi saturé

## Jour J
- [ ] Partage de connexion 4G prêt en secours
- [ ] Police du terminal et de l'éditeur à 20 pt minimum, thème clair si la salle est lumineuse
- [ ] Notifications coupées, onglets fermés, clé API **jamais** affichée à l'écran
- [ ] Premier quart d'heure : faire tourner `check_setup.py` à tout le monde, binômes pour ceux qui bloquent

## Plans B
| Problème | Plan B |
|---|---|
| Wifi saturé | `pip install --no-index --find-links wheels/ -r requirements.txt` depuis la clé USB |
| Quota Gemini dépassé (429) | Chaque participant utilise **sa propre clé** ; sinon basculer sur `gemini-2.5-flash-lite` |
| Pas de clé Google possible | Binôme avec un voisin |
| Claude Code indisponible (réseau, quota) | Démo 2 avec Gemini CLI ou `mcp dev` (MCP Inspector) |
| Pas de Node chez un participant | Binôme avec un voisin pour la partie Gemini CLI |

## Timing indicatif (2 h)
| Bloc | Durée |
|---|---|
| Intro, prérequis, LLM vs agent | 10 min |
| Module 1 : setup + ADK + exercices 1.x | 25 min |
| Module 2 : outils + démo 1 + exercices 2.x | 30 min |
| Module 3 : MCP + démo 2 + exercices 3.x | 30 min |
| Module 4 : production | 15 min |
| Questions | 10 min |
