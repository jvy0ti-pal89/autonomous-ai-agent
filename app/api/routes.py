from fastapi import APIRouter
from app.models.request import AgentRequest
from app.models.response import AgentResponse
from app.agent.orchestrator import run_agent_workflow

router = APIRouter(prefix="/agent", tags=["agent"])

@router.post("", response_model=AgentResponse)
def run_agent(request: AgentRequest):
    result = run_agent_workflow(request.prompt)
    return AgentResponse(**result)
