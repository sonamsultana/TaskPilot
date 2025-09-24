# import os
# import requests
# import json
# from dotenv import load_dotenv

# load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

# def generate_plan(goal: str, available_tools):
#     prompt = f"""
#     You are a planner agent. Break down the user goal into a JSON plan.
#     Only use these tools: {list(available_tools)}.

#     Format:
#     {{
#       "plan": [
#         {{"id": 1, "tool": "ToolName", "args": {{...}}, "action": "What it does"}}
#       ]
#     }}

#     User goal: {goal}
#     """

#     headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
#     body = {
#         "model": "gpt-4o-mini",  # or llama3 if using Ollama locally
#         "messages": [{"role":"user","content": prompt}],
#         "max_tokens": 500
#     }

#     r = requests.post(OPENAI_API_URL, headers=headers, json=body, timeout=30)
#     data = r.json()
#     content = data["choices"][0]["message"]["content"]

#     try:
#         return json.loads(content)
#     except json.JSONDecodeError:
#         return {"plan": []}



import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

def generate_plan(goal: str, available_tools):
    """
    Calls OpenAI API to generate a structured JSON plan
    for executing the user's goal using available tools.
    """

    prompt = f"""
    You are a planner agent. Break down the user goal into a JSON plan.
    Only use these tools: {list(available_tools)}.

    The output must be strictly valid JSON.

    Format:
    {{
      "plan": [
        {{"id": 1, "tool": "ToolName", "args": {{...}}, "action": "What it does"}}
      ]
    }}

    User goal: {goal}
    """

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4o-mini",  # You can also use "gpt-4o" or "gpt-3.5-turbo"
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0  # keep deterministic for structured JSON
    }

    try:
        r = requests.post(OPENAI_API_URL, headers=headers, json=body, timeout=30)
        r.raise_for_status()
        data = r.json()
        content = data["choices"][0]["message"]["content"]

        # Try to parse JSON output
        return json.loads(content)

    except json.JSONDecodeError:
        # If the LLM output isn't valid JSON, return empty plan
        return {"plan": []}

    except Exception as e:
        print("Planner error:", str(e))
        return {"plan": []}
