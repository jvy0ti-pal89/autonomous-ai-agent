from app.agent.planner import create_plan
from app.agent.executor import execute_task
from app.agent.reflector import reflect
from app.tools.doc_generator import create_document
from app.llm.groq_client import GroqClient

client = GroqClient()


def run_agent_workflow(user_request: str):

    plan = create_plan(user_request)

    tasks = plan["tasks"]

    document_type = plan["document_type"]

    results = []

    for task in tasks:
        results.append(execute_task(task, user_request))

    reflection = reflect(results)

    context = "\n\n".join(item["content"] for item in results)

    final_prompt = f"""
You are a Senior Business Consultant.

User Request:
{user_request}

Document Type:
{document_type}

Collected Information:
{context}

Generate the FINAL professional document.

Requirements:

- Produce the finished document only.
- Do not mention planning.
- Do not mention tasks.
- Do not mention workflow.
- Make reasonable assumptions where needed.
- Use professional headings.
- Return plain text only.
"""

    final_document = client.generate(final_prompt)

    document_path = create_document(
        final_document, title=document_type.replace("_", " ").title()
    )

    return {
        "status": reflection["status"],
        "document_type": document_type,
        "plan": tasks,
        "summary": reflection["feedback"],
        "document_path": document_path,
    }
