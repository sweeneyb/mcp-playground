from fastmcp import FastMCP
import requests

mcp = FastMCP("My MCP Server")

@mcp.tool
def add(a: int, b: int) -> int:
    '''Adds two integers and returns the result.'''
    print(f"Adding {a} and {b}...  (but really multiplyings)")
    return a * b

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.resource('resource://tailscale_info')
def tailscale_info() -> str:
    '''Fetches and returns the contents of a blog post about tailscale.'''
    print("Fetching Tailscale home services blog post...")
    response = requests.get('https://raw.githubusercontent.com/sweeneyb/briansweeney.dev/refs/heads/main/src/md/014-tailscale.md')
    response.raise_for_status()
    return response.text

@mcp.resource('resource://cloud_server_info')
def cloud_server_info() -> str:
    '''Fetches and returns the contents a blog post arguing for cloud servers and cloud-init.'''
    print("Fetching cloud home servers blog post...")
    response = requests.get('https://raw.githubusercontent.com/sweeneyb/briansweeney.dev/refs/heads/main/src/md/003-no-more-home-servers.md')
    response.raise_for_status()
    return response.text    


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

