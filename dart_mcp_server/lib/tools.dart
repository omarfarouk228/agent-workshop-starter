/// Les outils du workshop, version Dart : mêmes noms, mêmes contrats que tools.py.
library;

import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;
import 'package:sqlite3/sqlite3.dart';

const _geo = 'https://geocoding-api.open-meteo.com/v1/search';
const _meteo = 'https://api.open-meteo.com/v1/forecast';
const _wiki = 'https://fr.wikipedia.org/w/api.php';
const _headers = {
  'User-Agent':
      'AgentWorkshopStarter/1.0 (https://github.com/omarfarouk228/agent-workshop-starter)',
};

/// Même base que la version Python : notes.db à la racine du repo.
String get notesDbPath =>
    Platform.environment['NOTES_DB'] ??
    File.fromUri(
      Platform.script,
    ).parent.parent.parent.uri.resolve('notes.db').toFilePath();

// Module 2 : outil local
Map<String, Object?> saveNote(String title, String content) {
  final db = sqlite3.open(notesDbPath);
  try {
    db.execute(
      'CREATE TABLE IF NOT EXISTS notes ('
      'id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, created_at TEXT)',
    );
    db.execute(
      'INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)',
      [title, content, DateTime.now().toUtc().toIso8601String()],
    );
    return {'id': db.lastInsertRowId, 'status': 'saved'};
  } finally {
    db.close();
  }
}

// Module 2 : outil distant
Future<Map<String, Object?>> getWeather(String city) async {
  final geo =
      jsonDecode(
            (await http.get(
              Uri.parse(
                _geo,
              ).replace(queryParameters: {'name': city, 'count': '1'}),
            )).body,
          )
          as Map<String, dynamic>;
  final results = geo['results'] as List<dynamic>?;
  if (results == null || results.isEmpty)
    return {'error': 'Ville introuvable : $city'};
  final place = results.first as Map<String, dynamic>;
  final r = await http.get(
    Uri.parse(_meteo).replace(
      queryParameters: {
        'latitude': '${place['latitude']}',
        'longitude': '${place['longitude']}',
        'current': 'temperature_2m,wind_speed_10m',
      },
    ),
  );
  final now =
      (jsonDecode(r.body) as Map<String, dynamic>)['current']
          as Map<String, dynamic>;
  return {
    'city': place['name'],
    'temp_c': now['temperature_2m'],
    'wind_kmh': now['wind_speed_10m'],
  };
}

// Bonus : recherche (Wikipédia FR, gratuit et sans clé)
Future<Map<String, Object?>> searchWeb(String query) async {
  final r = await http.get(
    Uri.parse(_wiki).replace(
      queryParameters: {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'srlimit': '3',
        'format': 'json',
      },
    ),
    headers: _headers,
  );
  final hits =
      ((jsonDecode(r.body) as Map<String, dynamic>)['query']
              as Map<String, dynamic>)['search']
          as List<dynamic>;
  return {
    'results': [
      for (final h in hits.cast<Map<String, dynamic>>())
        {
          'title': h['title'],
          'snippet': (h['snippet'] as String)
              .replaceAll('<span class="searchmatch">', '')
              .replaceAll('</span>', ''),
          'url':
              'https://fr.wikipedia.org/wiki/${(h['title'] as String).replaceAll(' ', '_')}',
        },
    ],
  };
}
