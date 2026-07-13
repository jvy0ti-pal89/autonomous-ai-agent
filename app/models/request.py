from pydantic import BaseModel, Field, field_validator


class AgentRequest(BaseModel):
    prompt: str = Field(..., min_length=3, description="User request for the agent")

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("prompt cannot be empty")
        return cleaned
