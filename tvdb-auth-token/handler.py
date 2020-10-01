from fastapi import HTTPException
from pathlib import Path
from pydantic import BaseModel
from requests import post
from typing import Optional, Union
from urllib.parse import urljoin

from .models import Auth, Token

FUNCTION_NAME = 'tvdb-auth-token'
FUNCTION_VERSION = '1.0.0'
FUNCTION_SUMMARY = "Using a local TVDB API secret, return an auth JWT."
FUNCTION_RESPONSE_DESC = "TVDB Bearer auth JWT with 24-hour lifetime."
TVDB_API_URL = "https://api.thetvdb.com"


class RequestModel(BaseModel):
    pass


class ResponseModel(BaseModel):
    token: str


def get_api_secret(secret_name: str) -> Optional[str]:
    secret_file = Path("/var/openfaas/secrets") / secret_name
    if secret_file.exists():
        with secret_file.open("r") as f:
            return f.read()


def fetch_bearer_token(auth: Auth) -> Token:
    url = urljoin(TVDB_API_URL, "login")
    response_json = post(url, json=auth.dict()).json()
    return Token(**response_json)
    

def handle(req: RequestModel) -> Union[RequestModel, HTTPException]:
    """handle a request to the function
    Args:
        req (dict): request body
    """
    try:
        apikey = get_api_secret("tvdb-apikey")
        auth = Auth(apikey=apikey)
        bearer_token = fetch_bearer_token(auth)
        res = ResponseModel(token=f"Bearer {bearer_token.token}")
    except Exception:
        raise HTTPException(status_code=500, detail=f"An API Error occurred")
    return res
