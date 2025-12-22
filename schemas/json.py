from pydantic import BaseModel


class JsonRequest(BaseModel):
    raw_json: str
