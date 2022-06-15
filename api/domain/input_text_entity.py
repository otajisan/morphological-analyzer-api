from pydantic import BaseModel


class InputTextEntity(BaseModel):
    text: str
