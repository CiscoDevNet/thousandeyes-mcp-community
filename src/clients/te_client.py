import os, httpx

BASE = "https://api.thousandeyes.com/v7"
TOKEN = os.getenv("TE_TOKEN")

async def list_tests():
    if not TOKEN:
        raise RuntimeError("TE_TOKEN is not set")

    async with httpx.AsyncClient(
        base_url = BASE,
        headers = {
            "Authorization": f"Bearer {TOKEN}", 
            "Accept": "application/json"
            },
        timeout=30,
    ) as c:
        r = await c.get("/tests")
        r.raise_for_status()
        data = r.json()

    tests = data.get("tests", [])
    return tests

