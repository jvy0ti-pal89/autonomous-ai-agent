from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    status: str = Field(..., description="Workflow status")
    summary: str = Field(..., description="Short summary of the outcome")
    document_path: str | None = Field(
        default=None, description="Path to generated document"
    )
    document_type: str
    plan: list[str]
