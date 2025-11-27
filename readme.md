# Setup

once ever:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install fastmcp
```

once per session:
```
source venv/bin/activate
python3 quickstart.py
```

To iterate:
1. in vscode, ctrl/command+shift+p, then choose "MCP: Reset Cached Tools"

# What Works
* \#add will multiply numbers.  I'm intentionally doing the wrong operation to differentiate from copilot itself
* When you ask things about tailscale, it'll hit the blog post.  I can't tell if/how it uses that page.
