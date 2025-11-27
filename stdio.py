from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet2(name: str) -> str:
    '''Greets a person by name.'''
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()