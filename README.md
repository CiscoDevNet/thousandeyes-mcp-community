# thousandeyes-mcp

Model Context Protocol (MCP) server for **Cisco ThousandEyes v7** — lets AI assistants query **tests, agents, alerts, dashboards, widgets, and test results** (network, page-load, web-transactions, path-vis).

> Community project - **NOT affiliated** with Cisco/ThousandEyes.  
> **Status:** Alpha (MVP) read-only.

---

## Why (business value)
- **Faster troubleshooting:** Ask AI to “show outages in the last hour” or “figure out where the network traffic is getting stuck at” for super fast issues identification.

- **Consistency over scripts:** Standard MCP tools replace one-off curl snippets.

- **Safer by default:** Read-only; token is only read from env.

- **Composable workflows:** Chain tools (tests → dashboard → widget → test results).

---

## Current capabilities

| Tool | What it does | Endpoint(s) |
|---|---|---|
| `te_list_tests(aid?, name_contains?, test_type?)` | Lists tests (filter by name/type/AG) | `GET /v7/tests` |
| `te_list_agents(agent_types?, aid?)` | Lists enterprise / cloud / endpoint agents | `GET /v7/agents` |
| `te_get_test_results(test_id, test_type, window?/start?/end?/aid?/agent_id?)` | Test results (e.g., `network`, `page-load`, `web-transactions`; not `dns-server`) | `GET /v7/test-results/{testId}/{testType}` |
| `te_get_path_vis(test_id, window?/start?/end?/aid?/agent_id?/direction?)` | Path visualization data | `GET /v7/test-results/{testId}/path-vis` |
| `te_list_dashboards(aid?, title_contains?)` | Lists dashboards | `GET /v7/dashboards` |
| `te_get_dashboard(dashboard_id, aid?)` | Dashboard details incl. widget list | `GET /v7/dashboards/{dashboardId}` |
| `te_get_dashboard_widget(dashboard_id, widget_id, window?/start?/end?/aid?)` | Widget data for a dashboard | `GET /v7/dashboards/{dashboardId}/widgets/{widgetId}` |


---

## Requirements

- Python **3.12+**
- ThousandEyes **API v7** bearer token in env: `TE_TOKEN`

---

## Install

```bash
python3 -m pip install -r requirements.txt
# If Python is externally managed:
# python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
```

---

## Configure (Claude Desktop)

Add to your `claude_desktop_config.json` (or Dev UI):

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

Token is read **only** from env, never written to disk.

---

## Try it out!

- What was the network health of the Patient Portal between 13:00–14:00 CET on 1 Sep 2025?
- Which regions/agents showed elevated page-load time for the Patient Portal between 08:00–10:00 UTC today?”
- Show uptime and TTFB for the Patient Portal homepage over the last 24 hours, and call out any drops.
- Which enterprise agents had >1% packet loss to api.patient-portal.example.com this morning?”
- Open the Patient Portal dashboard and list the widgets relevant to availability and the login flow and callout any widgets reporting no data
- For test <ID>, compare network latency during 10:00–10:30 UTC vs. the prior 30 minutes.”
- Show path visualization anomalies for test <ID> around 15:30 UTC yesterday.”

---

## Security & privacy

- Read-only tools - no writes.
- No tokens or org data stored - token only via `TE_TOKEN`.
- Respect org rate limits - backoff on the roadmap.

---

## Roadmap

- Adding feature support for alerts, tags, event detection, endpoint agents, etc.
- Optional retries/backoff on 429.
- Minimal CI and examples catalog.

---

## License & attribution

- **Apache-2.0**
- “ThousandEyes” is a trademark of Cisco Systems, Inc. This project is **NOT** affiliated with Cisco/ThousandEyes.

---

## Maintainers

- Aditya Chellam · Kiran Kabdal
