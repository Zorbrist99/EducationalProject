"""
{
    "success": false,
    "error": "NotAuthorized",
    "message": "Your email, username, or password are incorrect. Please try again or use \"Forgot Password.\""
}
"""
from pydantic import BaseModel


class PostLoginInLkUnauthorizedResponse(BaseModel):
    success: bool
    error: str
    message: str
