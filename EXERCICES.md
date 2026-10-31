# Exercices pratiques

Chaque exercice part du code du repo. Bloqué ? Appelez l'animateur.

---

## Module 1 · Prise en main (10 min)

### 1.1 Premier lancement

Lancez `adk web` depuis la racine du repo, ouvrez http://localhost:8000 et sélectionnez `assistant_agent`.

Posez trois questions : une qui n'a besoin d'aucun outil, une sur la météo, une qui demande de noter quelque chose. Dans l'onglet **Events**, repérez pour chaque question :

- l'appel d'outil (`functionCall`) et ses arguments ;
- la réponse de l'outil (`functionResponse`) ;
- la réponse finale du modèle.

> 🎯 Objectif : voir la boucle agentique *LLM → outil → résultat → LLM* de vos propres yeux.

### 1.2 Donner une personnalité

Modifiez `instruction` dans `assistant_agent/agent.py` pour que l'agent :

- tutoie l'utilisateur ;
- réponde en 3 phrases maximum ;
- confirme toujours l'ID quand il enregistre une note.

---

## Module 2 · Créer des outils (25 min)

### 2.1 Relire ses notes

L'agent peut écrire des notes mais pas les relire. Ajoutez un outil `list_notes` dans `tools.py` qui retourne les 5 dernières notes, puis branchez-le sur l'agent.

Test : *« Qu'est-ce que j'ai noté aujourd'hui ? »*

### 2.2 Le bug de Kara 🐛

Demandez : *« Quelle météo à Kara ? »*. Regardez la réponse de l'outil : quelle ville a-t-il trouvée ?

(Indice : ce n'est pas au Togo.)

Corrigez `get_weather` pour accepter un code pays optionnel. L'API de géocodage d'Open-Meteo accepte un paramètre `countryCode` (code ISO à 2 lettres, `TG` pour le Togo).

Puis redemandez simplement *« Quelle météo à Kara ? »* : l'agent utilise-t-il votre nouveau paramètre ? Sinon, que lui manque-t-il pour savoir que vous êtes au Togo ?

> 💡 Leçon : la docstring et les noms de paramètres **sont** le prompt de l'outil. Une docstring vague donne des appels vagues.

### 2.3 Bonus : un outil à vous

Créez un outil qui appelle une API gratuite de votre choix, par exemple :

- taux de change : `https://open.er-api.com/v6/latest/XOF`
- jours fériés : `https://date.nager.at/api/v3/PublicHolidays/2026/TG`

---

## Module 3 · Serveur MCP (25 min)

### 3.1 Inspecter le serveur

```bash
mcp dev demo_mcp_server.py
```

Dans MCP Inspector (nécessite Node) : **Connect**, onglet **Tools**, puis appelez `get_weather` à la main.

### 3.2 Exposer tous vos outils

Ajoutez `search_web` et votre `list_notes` (exercice 2.1) au serveur MCP. Relancez l'Inspector pour vérifier.

### 3.3 Brancher un vrai client

Les serveurs sont déjà déclarés dans le repo (`.gemini/settings.json` et `.mcp.json`). Depuis la racine du repo, lancez **Gemini CLI** (`gemini`, gratuit) ou **Claude Code** (`claude`, abonnement requis), acceptez de faire confiance au dossier, puis tapez `/mcp`.

Demandez ensuite : *« Note : appel client demain à 14h. Et quelle météo à Lomé ? »*

Ouvrez enfin `notes.db` (ou demandez `list_notes` à votre agent ADK) : la note écrite par Gemini CLI est là. **Deux agents différents, la même base, le même code.**

### 3.4 Bonus : un agent Python, des outils en Dart

Le dossier `dart_mcp_server/` contient les mêmes outils écrits en Dart. Branchez-les sur un agent ADK Python via `McpToolset` (`google.adk.tools.mcp_tool`), avec `StdioConnectionParams` qui lance `dart dart_mcp_server/bin/server.dart`. Lancez `cd dart_mcp_server && dart pub get` une première fois.

---

## Module 4 · Vers la production (bonus)

### 4.1 Valider les entrées

Traitez chaque sortie du LLM comme non fiable. Faites en sorte que `save_note` refuse un titre vide ou de plus de 100 caractères, et retourne une erreur lisible au lieu de lever une exception.

### 4.2 Passer en HTTP

Remplacez `mcp.run()` par `mcp.run(transport="streamable-http")`. Le serveur écoute alors en HTTP et peut être déployé sur Cloud Run.
