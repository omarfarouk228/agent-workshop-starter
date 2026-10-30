from mcp.server.mcpserver import MCPServer

from assistant_agent.tools import get_weather, save_note  # les fonctions du module 2

mcp = MCPServer("demo")
mcp.add_tool(save_note)
mcp.add_tool(get_weather)


@mcp.tool()
def ping() -> str:
    """Vérifie que le serveur répond."""
    return "pong"


if __name__ == "__main__":
    mcp.run()  # transport stdio par défaut
