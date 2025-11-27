from fastmcp import FastMCP
import requests
import json


mcp = FastMCP("My MCP Server")

@mcp.tool
def greet2(name: str) -> str:
    '''Greets a person by name.'''
    return f"Hello, {name}!"

@mcp.tool
def getUserData(username: str) -> dict:
    '''Returns user data for a given username.'''
    URL = f'https://raw.githubusercontent.com/sweeneyb/mcp-playground/refs/heads/main/data/db/{username}.json'
    print(f"Fetching userdata from stdio tool... {URL}")
    response = requests.get(URL)
    response.raise_for_status()
    return json.loads(response.text)

@mcp.resource('resource://ticket_info/{id}')
def ticket_info(id: str) -> str:
    '''Fetches and returns the text of a ticket given its ID.'''
    print(f"Fetching ticket id: {id}")
    URL = f"https://raw.githubusercontent.com/sweeneyb/mcp-playground/refs/heads/main/data/issues/{id}.txt"
    print(f"Fetching ticket... {URL}")
    response = requests.get(URL)
    response.raise_for_status()
    return response.text

@mcp.prompt
def ask_about_ticket(id: str) -> str:
    """summarize a ticket and pull in data."""
    return f"Use the ticket_info resource to pull information about '{id}'.  Summarize the issue and, if it mentions a person, use tools to get and print the relevant user data"

@mcp.prompt
def ask_for_user(username: str) -> str:
    """ask for user data."""
    return f"Use the getUserData tool to pull information about user '{username}' and print it out."

if __name__ == "__main__":
    mcp.run()