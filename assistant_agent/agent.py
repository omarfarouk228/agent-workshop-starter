from google.adk.agents import Agent

from .tools import get_weather, save_note, search_web

root_agent = Agent(
    name="assistant_agent",
    model="gemini-2.5-flash",
    description="Assistant personnel",
    instruction="Tu es un assistant utile. "
                "Utilise tes outils quand c'est pertinent.",
    tools=[save_note, get_weather, search_web],
)
