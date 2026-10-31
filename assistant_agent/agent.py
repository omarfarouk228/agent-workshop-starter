from google.adk.agents import Agent

from .tools import get_weather, save_note, search_web

root_agent = Agent(
    name="assistant_agent",
    model="gemini-3.5-flash-lite",
    description="Assistant personnel",
    instruction="Tu es un assistant utile. "
                "Utilise tes outils quand c'est pertinent.",
    tools=[save_note, get_weather, search_web],
)
