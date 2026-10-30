import 'dart:convert';
import 'dart:io' as io;

import 'package:dart_mcp/server.dart';
import 'package:dart_mcp/stdio.dart';
import 'package:dart_mcp_server/tools.dart';

void main() {
  DemoServer(stdioChannel(input: io.stdin, output: io.stdout));
}

base class DemoServer extends MCPServer with ToolsSupport {
  DemoServer(super.channel)
    : super.fromStreamChannel(
        implementation: Implementation(name: 'demo-dart', version: '1.0.0'),
        instructions: 'Outils du workshop Agent IA : notes, météo, recherche.',
      ) {
    registerTool(
      Tool(
        name: 'save_note',
        description:
            'Sauvegarde une note (titre + contenu) dans la base locale.',
        inputSchema: Schema.object(
          properties: {'title': Schema.string(), 'content': Schema.string()},
          required: ['title', 'content'],
        ),
      ),
      (req) => _result(
        saveNote(
          req.arguments!['title'] as String,
          req.arguments!['content'] as String,
        ),
      ),
    );
    registerTool(
      Tool(
        name: 'get_weather',
        description:
            "Météo actuelle d'une ville : température (°C) et vent (km/h).",
        inputSchema: Schema.object(
          properties: {'city': Schema.string()},
          required: ['city'],
        ),
      ),
      (req) async =>
          _result(await getWeather(req.arguments!['city'] as String)),
    );
    registerTool(
      Tool(
        name: 'search_web',
        description:
            'Recherche des informations factuelles sur Wikipédia (français).',
        inputSchema: Schema.object(
          properties: {'query': Schema.string()},
          required: ['query'],
        ),
      ),
      (req) async =>
          _result(await searchWeb(req.arguments!['query'] as String)),
    );
  }

  CallToolResult _result(Map<String, Object?> data) =>
      CallToolResult(content: [TextContent(text: jsonEncode(data))]);
}
