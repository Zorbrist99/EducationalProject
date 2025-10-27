"""
{
    "text": "Update Habitica API Documentation - Tasks",
    "type": "type",
    "alias": "hab-api_tests-tasks",
    "notes": "Update the tasks api_tests on GitHub",
    "tags": [
        "ed427623-9a69-4aac-9852-13deb9c190c3"
    ],
    "checklist": [
        {
            "text": "read wiki",
            "completed": true
        },
        {
            "text": "write code"
        }
    ],
    "priority": 2
}
"""
from typing import Optional, List

from pydantic import BaseModel, Field


class PostCreatNewTaskUserRequest(BaseModel):
    text: str
    "Такое ограничение работает только со строками"
    type: str = Field(..., pattern='^(habit|daily|todo|reward)$')
    "Таким образом можно указать варианты, которые могут вернуться, иначе ошибка"
    frequency: str = Field(..., pattern="^(daily|weekly|monthly|yearly)$")
    "Таким образом можно указать, что поле не обязательное"
    alias: Optional[str] = None
    notes: Optional[str] = None
    daysOfMonth: List[int]
    weeksOfMonth: List[int]
