"""
{
    "success": true,
    "data": [
        {
            "id": "8a6a2a7a-62f8-463b-b88e-5951669f6f3e",
            "name": "Работа"
        }
    ],
    "notifications": [
        {
            "type": "NEW_STUFF",
            "data": {
                "title": "LAST CHANCE FOR GLIDING GHOUL SET AND CURRENT TIME TRAVELERS' SELECTIONS"
            },
            "seen": true,
            "id": "7a15d95b-4853-452c-89c4-5aa9130bf2f8"
        }
    ],
    "userV": 289,
    "appVersion": "5.41.5"
}
"""
from typing import List

from pydantic import BaseModel


class Data(BaseModel):
    id: str
    name: str


class DataNotifications(BaseModel):
    title: str


class Notifications(BaseModel):
    type: str
    data: DataNotifications
    seen: bool
    id: str


class GetAllTagsResponse(BaseModel):
    success: bool
    data: List[Data]
    notifications: List[Notifications]
    userV: int
    appVersion: str
