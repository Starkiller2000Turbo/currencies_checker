from pydantic import BaseModel


class MessageSchema(BaseModel):
    """Empty response schema."""

    message: str
