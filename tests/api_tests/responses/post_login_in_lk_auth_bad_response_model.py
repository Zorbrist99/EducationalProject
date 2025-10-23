"""
{
   "success":false,
   "error":"BadRequest",
   "message":"Invalid request parameters.",
   "errors":[
      {
         "message":"Missing username or email.",
         "param":"username"
      },
      {
         "message":"Missing password.",
         "param":"password"
      }
   ]
}
"""
from typing import List

from pydantic import BaseModel, Field


class Errors(BaseModel):
    message: str
    param: str


class PostLoginInLkAuthBadResponse(BaseModel):
    success: bool
    error: str
    message: str
    errors: List[Errors]
