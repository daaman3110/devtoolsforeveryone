from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from schemas.json import JsonRequest
from services.json_formatter import json_formatter

router = APIRouter(prefix="/json", tags=["JSON Tools"])


@router.post(
    "/format",
    response_class=PlainTextResponse,
    summary="Format and Validate JSON",
    description="Formats valid JSON or returns a human-friendly error message",
)
def format_json_endpoint(payload: JsonRequest):
    """
    Receives raw JSON as a string and returns:
    - formatted JSON if valid
    - clean error message if invalid
    """
    return json_formatter(payload.raw_json)
