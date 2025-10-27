"""
{
    "success": false,
    "error": "NotFound",
    "message": "Not found."
}
"""
from pydantic import BaseModel


class GetTagIdRandomUserResponse(BaseModel):
    success: bool
    error: str
    message: str
