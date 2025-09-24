from typing import List, Dict
from tools.echo_tool import EchoTool
from tools.http_tool import HTTPTool
from tools.email_tool import EmailTool

TOOLS = {
    "EchoTool": EchoTool(),
    "HTTPTool": HTTPTool(),
    "EmailTool": EmailTool()
}

def run_plan(plan: List[Dict]):
    logs = []
    for step in plan:
        tool_name = step["tool"]
        tool = TOOLS.get(tool_name)
        if not tool:
            logs.append({"step": step, "status": "failed", "error": "Unknown tool"})
            continue
        try:
            result = tool.run(step.get("args", {}))
            logs.append({"step": step, "status": "ok", "result": result})
        except Exception as e:
            logs.append({"step": step, "status": "error", "error": str(e)})
    return logs
