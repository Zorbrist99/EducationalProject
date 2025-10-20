"""
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    },
    "_meta": {
        "powered_by": "🚀 ReqRes - Deploy backends in 30 seconds",
        "upgrade_url": "https://app.reqres.in/upgrade",
        "docs_url": "https://reqres.in",
        "template_gallery": "https://app.reqres.in/templates",
        "message": "This API is powered by ReqRes. Deploy your own backend in 30 seconds!",
        "features": [
            "30 Second Backend Templates",
            "Custom API Endpoints",
            "Data Persistence",
            "Real-time Analytics"
        ],
        "upgrade_cta": "Upgrade to Pro for unlimited requests, custom endpoints, and data persistence"
    }
}
"""
from typing import List

from pydantic import BaseModel, Field

class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class Meta(BaseModel):
    powered_by: str
    upgrade_url: str
    docs_url: str
    template_gallery: str
    message: str
    features: List[str]
    upgrade_cta: str

"""
Это главная (корневая) модель, которая описывает всю структуру JSON-ответа целиком, а не отдельные его части.
Валидировать ответ я буду как раз через этот класс
"""
class GetSingleUserResponse(BaseModel):
    data: Data
    support: Support
    "В JSON поле называется _meta, а в Python-модели я хочу обращаться к нему как meta"
    meta: Meta = Field(alias='_meta')
