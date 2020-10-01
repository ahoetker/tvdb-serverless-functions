from fastapi import HTTPException
from requests import get
from pydantic import BaseModel
from typing import Union
from urllib.parse import urljoin

from .models import SeriesSearchQuery, SeriesSearchResults, Token

FUNCTION_NAME = 'tvdb-series-search'
FUNCTION_VERSION = '1.0.0'
FUNCTION_SUMMARY = "A function that searches for a TV series."
FUNCTION_RESPONSE_DESC = "Series search results."
TVDB_API_URL = "https://api.thetvdb.com"


# FastAPI models
class RequestModel(BaseModel):
    token: Token
    query: SeriesSearchQuery


class ResponseModel(BaseModel):
    results: SeriesSearchResults


def search(request: RequestModel) -> SeriesSearchResults:
    url = urljoin(TVDB_API_URL, f"search/series")
    response_json = get(
        url,
        headers={"Authorization": request.token.token},
        params=request.query.dict(exclude_none=True)
    ).json()
    return SeriesSearchResults(**response_json)


def handle(req: RequestModel) -> Union[ResponseModel, HTTPException]:
    try:
        results = search(req)
        res = ResponseModel(results=results)
    except Exception:
        raise HTTPException(status_code=500, detail=f"An API Error occurred")
    return res
