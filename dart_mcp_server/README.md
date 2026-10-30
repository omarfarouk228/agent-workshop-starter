# Serveur MCP en Dart

Les trois outils du workshop (`save_note`, `get_weather`, `search_web`) réécrits en Dart et exposés en MCP avec [`dart_mcp`](https://pub.dev/packages/dart_mcp), le package officiel de l'équipe Dart.

> Pourquoi pas un agent ADK en Dart ? Google ADK n'a pas de SDK Dart officiel (Python, Java, Go, TypeScript). Grâce à MCP, ce n'est pas un problème : l'agent reste en Python et **les outils peuvent être en Dart**.

Les versions Python et Dart écrivent dans la **même** `notes.db`, à la racine du repo.

## Lancer

```bash
cd dart_mcp_server
dart pub get
dart run bin/server.dart   # serveur MCP sur stdio
```

## Claude Desktop

```json
{
  "mcpServers": {
    "demo-dart": {
      "command": "/chemin/absolu/vers/dart",
      "args": ["/chemin/absolu/agent-workshop-starter/dart_mcp_server/bin/server.dart"]
    }
  }
}
```

`which dart` donne le chemin de `dart`. Les deux serveurs (`demo` en Python et `demo-dart`) peuvent tourner côte à côte.

## Brancher sur l'agent Python ADK

Voir l'exercice 3.4 dans [EXERCICES.md](../EXERCICES.md).

## Structure

```
lib/tools.dart     # saveNote, getWeather, searchWeb
bin/server.dart    # MCPServer + ToolsSupport, enregistrement des 3 outils
```
