import json


def json_formatter(raw_json: str) -> str:
    """
    Formats JSON if valid
    Returns formatted JSON string on success
    Returns a clean, human-friendly error message on failure
    """
    try:
        # Incoming JSON
        incoming_json = json.loads(raw_json)
        # Formatted JSON
        formatted_json = json.dumps(incoming_json, indent=2)
        return formatted_json

    except json.JSONDecodeError as e:
        # Build a beginner friendly error message
        explanation = _explain_error(e.msg)

        return (
            f"Oops!! Your JSON is invalid.\n"
            f"Reason: {explanation}\n"
            f"Location: line {e.lineno}, column {e.colno}\n"
            f"Tip: Check the syntax around the marked location"
        )


def _explain_error(raw_msg: str) -> str:
    """Converts cryptic JSON error into beginner friendly explanations"""

    if "Expecting ',' delimiter" in raw_msg:
        return "Missing a comma or closing brace"

    if "Expecting value" in raw_msg:
        return "A value is missing (string, number, true, false, null)"

    if "Unterminated string" in raw_msg:
        return "A string is missing a closing quote"

    if "Extra data" in raw_msg:
        return "Multiple JSON values found; only one root object is allowed"

    # Fallback
    return raw_msg
