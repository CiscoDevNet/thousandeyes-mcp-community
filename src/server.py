from mcp.server.fastmcp import FastMCP
from clients.te_client import list_tests

mcp = FastMCP("thousandeyes")

@mcp.tool()
async def te_list_tests(name_contains: str | None = None):
    tests = await list_tests()
    if name_contains:
        n = name_contains.lower()
        tests = [t for t in tests if n in str(t.get("testName", t.get("name",""))).lower()]
    return tests

if __name__ == "__main__":
    mcp.run()