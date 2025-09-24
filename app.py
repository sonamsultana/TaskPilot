from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from planner import generate_plan
from orchestrator import run_plan

app = FastAPI()

db = {}

class TaskRequest(BaseModel):
    goal: str

@app.post("/tasks")
def create_task(req: TaskRequest):
    task_id = str(uuid.uuid4())
    plan = generate_plan(req.goal, ["EchoTool", "HTTPTool", "EmailTool"])
    logs = run_plan(plan.get("plan", []))
    db[task_id] = {"goal": req.goal, "plan": plan, "logs": logs}
    return {"task_id": task_id}

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    return db.get(task_id, {"error": "Task not found"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
