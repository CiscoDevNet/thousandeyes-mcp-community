# thousandeyes-mcp

Model Context Protocol (MCP) server for **Cisco ThousandEyes v7** — lets AI assistants **list tests** (read-only).  
**Status:** pre‑alpha. Community project; **not affiliated** with Cisco/ThousandEyes.

## Requirements
- Python **3.12+**
- ThousandEyes **API v7** bearer token

## Install
```bash
python3 -m pip install -r requirements.txt
# If Python is externally managed:
# python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

## Configure (Claude Desktop)
Add to `claude_desktop_config.json` (or Dev UI):
```json
{
  "mcpServers": {
    "thousandeyes": {
      "command": "/ABS/PATH/TO/python3",
      "args": ["/ABS/PATH/TO/repo/src/server.py"],
      "env": { "TE_TOKEN": "YOUR_OAUTH_BEARER_TOKEN" }
    }
  }
}
```
> Token is read **only** from env.

## Usage
Ask Claude:
- Use **thousandeyes** → call `te_list_tests`
- Use **thousandeyes** → call `te_list_tests` with `{ "name_contains": "prod" }`

## Tools (v0.1)
- `te_list_tests(name_contains?: string)` → returns `tests[]`

## Troubleshooting
- **ENOENT**: use absolute paths for `command` and `args`.
- **401**: invalid/missing `TE_TOKEN`.
- **ImportError**: `python3 -m pip install -r requirements.txt` (or use venv).

---

**License:** Apache-2.0  
**Maintainers:** Aditya Chellam · Kiran Kabdal
