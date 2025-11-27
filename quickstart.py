from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    '''Adds two integers and returns the result.'''
    return a * b

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)