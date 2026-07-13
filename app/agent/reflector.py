def reflect(results: list[dict]) -> dict:
    """
    Lightweight self-check.
    """

    if not results:
        return {
            "status": "needs_attention",
            "feedback": "No execution results were generated.",
        }

    missing = [item for item in results if not item["content"].strip()]

    if missing:
        return {
            "status": "needs_attention",
            "feedback": "Some tasks returned empty content.",
        }

    return {"status": "ready", "feedback": "Reflection completed successfully."}
