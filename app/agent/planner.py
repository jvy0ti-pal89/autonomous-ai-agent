def create_plan(user_request: str) -> dict:
    """
    Analyze the request and create an execution plan.
    """

    request = user_request.lower()

    if any(word in request for word in ["meeting", "minutes"]):
        document_type = "meeting_minutes"

    elif any(word in request for word in ["proposal", "propose"]):
        document_type = "business_proposal"

    elif "report" in request:
        document_type = "business_report"

    elif any(word in request for word in ["technical", "architecture", "design"]):
        document_type = "technical_design"

    elif "sop" in request:
        document_type = "standard_operating_procedure"

    elif any(word in request for word in ["project plan", "roadmap"]):
        document_type = "project_plan"

    else:
        document_type = "business_document"

    return {
        "document_type": document_type,
        "tasks": [
            "Analyze the request",
            "Identify assumptions",
            "Generate document content",
            "Review content",
            "Generate final document",
        ],
    }
