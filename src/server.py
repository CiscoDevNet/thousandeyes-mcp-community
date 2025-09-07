# Copyright 2025 Cisco Systems, Inc. and its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

# src/server.py
from mcp.server.fastmcp import FastMCP
from clients.te_client import list_tests, get_test_results, get_path_vis
from clients.te_client import list_dashboards, get_dashboard, get_dashboard_widget 
from clients.te_client import get_account_groups

mcp = FastMCP("thousandeyes")

@mcp.tool()
async def te_list_tests(aid: str | None = None,
                        name_contains: str | None = None,
                        test_type: str | None = None):
    tests = await list_tests(aid)
    if test_type:
        tt = str(test_type).lower()
        tests = [t for t in tests if str(t.get("type","")).lower() == tt]
    if name_contains:
        n = str(name_contains).lower()
        tests = [t for t in tests if n in str(t.get("testName", t.get("name",""))).lower()]
    return tests

@mcp.tool()
async def te_get_test_results(test_id: str,
                              test_type: str,
                              window: str | None = None,
                              start: str | None = None,
                              end: str | None = None,
                              aid: str | None = None,
                              agent_id: str | None = None):
    return await get_test_results(test_id, test_type, window, start, end, aid, agent_id)

@mcp.tool()
async def te_get_path_vis(test_id: str,
                          window: str | None = None,
                          start: str | None = None,
                          end: str | None = None,
                          aid: str | None = None,
                          agent_id: str | None = None,
                          direction: str | None = None):
    return await get_path_vis(test_id, window, start, end, aid, agent_id, direction)

@mcp.tool()
async def te_list_dashboards(aid: str | None = None,
                             title_contains: str | None = None):
    dashboards = await list_dashboards(aid)
    if title_contains:
        n = str(title_contains).lower()
        dashboards = [d for d in dashboards if n in str(d.get("title","")).lower()]
    return dashboards


@mcp.tool()
async def te_get_dashboard(dashboard_id: str, aid: str | None = None):
    return await get_dashboard(dashboard_id, aid)

@mcp.tool()
async def te_get_dashboard_widget(dashboard_id: str,
                                  widget_id: str,
                                  start: str | None = None,
                                  end: str | None = None,
                                  aid: str | None = None,
                                  window: str | None = None):
    return await get_dashboard_widget(dashboard_id, widget_id, start, end, aid, window)

@mcp.tool()
async def te_get_account_groups():
    return await get_account_groups()

if __name__ == "__main__":
    mcp.run()
