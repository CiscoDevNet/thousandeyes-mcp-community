# src/clients/te_client.py
import os, httpx

BASE = "https://api.thousandeyes.com/v7"
TOKEN = os.getenv("TE_TOKEN")
HDRS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
TIMEOUT = httpx.Timeout(connect=5.0, read=25.0, write=10.0, pool=5.0)

#Tests and Related Data
async def list_tests(aid=None):
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")
    params = {"aid": aid} if aid else None
    async with httpx.AsyncClient(
        base_url=BASE, headers=HDRS, timeout=TIMEOUT, http2=False, trust_env=True
    ) as c:
        r = await c.get("/tests", params=params)
        r.raise_for_status()
        return r.json().get("tests", [])

async def get_test_results(test_id, test_type, window=None, start=None, end=None, aid=None, agent_id=None):
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")
    params = {}
    if window:   params["window"] = window
    if start:    params["startDate"] = start
    if end:      params["endDate"] = end
    if aid:      params["aid"] = aid
    if agent_id: params["agentId"] = agent_id
    async with httpx.AsyncClient(base_url=BASE, headers=HDRS, timeout=TIMEOUT, http2=False, trust_env=True) as c:
        r = await c.get(f"/test-results/{test_id}/{test_type}", params=params)
        r.raise_for_status()
        return r.json()

async def get_path_vis(test_id, window=None, start=None, end=None, aid=None, agent_id=None, direction=None):
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")
    params = {}
    if window:     params["window"] = window
    if start:      params["startDate"] = start
    if end:        params["endDate"] = end
    if aid:        params["aid"] = aid
    if agent_id:   params["agentId"] = agent_id
    if direction:  params["direction"] = direction
    headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/json"}
    timeout = httpx.Timeout(connect=5.0, read=25.0, write=10.0, pool=5.0)
    async with httpx.AsyncClient(base_url=BASE, headers=headers, timeout=timeout, http2=False, trust_env=True) as c:
        r = await c.get(f"/test-results/{test_id}/path-vis", params=params)
        r.raise_for_status()
        return r.json()

#Dashboards and Related Data
async def list_dashboards(aid=None):
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")
    params = {"aid": aid} if aid else None
    async with httpx.AsyncClient(
        base_url=BASE, headers=HDRS, timeout=TIMEOUT, http2=False, trust_env=True
    ) as c:
        try:
            r = await c.get("/dashboards", params=params)  # common path
            r.raise_for_status()
            data = r.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                r = await c.get("/dashboard", params=params)  # alternative path
                r.raise_for_status()
                data = r.json()
            else:
                raise
    return data if isinstance(data, list) else data.get("dashboards", [])

async def get_dashboard(dashboard_id, aid=None):
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")
    params = {"aid": aid} if aid else None
    async with httpx.AsyncClient(base_url=BASE, headers=HDRS, timeout=TIMEOUT, http2=False, trust_env=True) as c:
        r = await c.get(f"/dashboards/{dashboard_id}", params=params)
        r.raise_for_status()
        return r.json()

async def get_dashboard_widget(dashboard_id, widget_id, start=None, end=None, aid=None, window=None):
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")
    params = {}
    if aid: params["aid"] = aid
    if window: params["window"] = window
    if start: params["startDate"] = start
    if end: params["endDate"] = end
    async with httpx.AsyncClient(base_url=BASE, headers=HDRS, timeout=TIMEOUT, http2=False, trust_env=True) as c:
        r = await c.get(f"/dashboards/{dashboard_id}/widgets/{widget_id}", params=params)
        r.raise_for_status()
        return r.json()
