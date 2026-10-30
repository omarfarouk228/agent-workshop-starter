# Message à envoyer aux participants (J-7, puis rappel J-1)

---

**Objet : Workshop Agent IA à Lomé : 20 minutes de préparation avant de venir**

Bonjour à toutes et à tous,

Merci pour votre inscription au workshop **« Construire un agent IA qui agit vraiment »** !

Pour qu'on passe nos 2 heures à coder plutôt qu'à installer, merci de préparer votre machine **avant le jour J**. Cela prend environ 20 minutes.

**1. Installer les outils**
- Python 3.11 ou plus récent : https://www.python.org/downloads/
- Git : https://git-scm.com/downloads
- Node 20 ou plus récent (recommandé pour la partie MCP) : prenez le paquet LTS sur https://nodejs.org
- Gemini CLI (optionnel) : `npm install -g @google/gemini-cli`

**2. Récupérer le code**
```
git clone https://github.com/omarfarouk228/agent-workshop-starter
cd agent-workshop-starter
python -m venv .venv
source .venv/bin/activate        (Windows : .venv\Scripts\activate)
pip install -r requirements.txt
```

**3. Créer votre clé API Gemini (gratuite)**
- Allez sur https://aistudio.google.com/apikey et connectez-vous avec un compte Google
- Cliquez sur « Create API key »
- Copiez `.env.example` en `assistant_agent/.env` et collez-y votre clé

**4. Vérifier**
```
python scripts/check_setup.py
```
Si tout est ✅, vous êtes prêts. Sinon, répondez à ce message avec une capture d'écran, on règle ça avant le workshop.

À apporter : votre ordinateur portable **chargé** et son chargeur.

À très vite,
Omar Farouk
