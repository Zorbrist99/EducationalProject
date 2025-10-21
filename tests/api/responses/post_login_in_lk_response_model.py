"""
{
    'success': True,
    'data': {
        'id': '48f4a048-3117-4ed0-84f2-94f82a2eb6ae',
        'apiToken': 'ea7a941d-3e0b-42bc-b0ea-0c805406652c',
        'newUser': False,
        'username': 'Sergey_01'
    },
    'appVersion': '5.41.4'
}
"""
from pydantic import BaseModel


class Data(BaseModel):
    id: str
    apiToken: str
    newUser: bool
    username: str


class PostLoginInLkResponse(BaseModel):
    success: bool
    data: Data
    appVersion: str
