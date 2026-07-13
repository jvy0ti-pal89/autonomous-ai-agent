from app.llm.groq_client import GroqClient

client = GroqClient()


def execute_task(task: str, user_request: str) -> dict:
    """
    Execute one planning task.
    """

    prompt = f"""
You are an autonomous AI agent.

User Request:
{user_request}

Current Task:
{task}

Generate only the information required for this task.

Formatting Rules

- Return plain text only.
- Do NOT use Markdown.
- Do NOT use **, #, or markdown bullets.
- Do NOT invent names.
- Use role-based titles when names are unavailable.
- Include an Assumptions section whenever information is missing.
- Include a separate Key Decisions section.
Write a professional business conclusion summarizing:
- Meeting outcome
- Next steps
- Expected follow-up
Do not explain your reasoning.
Be concise and professional.
"""

    content = client.generate(prompt)

    return {"task": task, "content": content}
