"""
Models generated from the TVDb API v3 Swagger spec:
https://api.thetvdb.com/swagger
"""

from pydantic import BaseModel


class Auth(BaseModel):
    apikey: str


class Token(BaseModel):
    token: str