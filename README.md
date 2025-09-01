# thousandeyes-mcp
Model Context Protocol (MCP) server for **Cisco ThousandEyes v7** — enabling AI assistants to **list tests**, and **enumerate agents**.  

**Status:** pre-alpha (scoping + incremental implementation). 

Community project **not affiliated** with official Cisco/ThousandEyes.

## Why
- Standardize access to ThousandEyes via MCP tools, not ad-hoc scripts.

## Scope (v0.1)
- Read-only tools:
  - `te.list_tests`
  - `te.list_agents`
- Minimal TypeScript server using MCP stdio transport.

## Tech Outline
- Language: Python3

---

**License:** Apache-2.0

**Maintainers:** Aditya Chellam, Kiran Kabdal
