from fastapi import HTTPException
from requests import get
from urllib.parse import urljoin
from pydantic import BaseModel
from typing import Union

from .models import SeriesEpisodes, SeriesEpisodesQuery, Token

FUNCTION_NAME = 'tvdb-series-episodes'
FUNCTION_VERSION = '1.0.0'
FUNCTION_SUMMARY = "A function that performs GET /series/<id>/episodes for TVDB API v3."
FUNCTION_RESPONSE_DESC = "Array of all Episode data for a given Series."
TVDB_API_URL = "https://api.thetvdb.com"


class RequestModel(BaseModel):
    token: Token
    query: SeriesEpisodesQuery


class ResponseModel(BaseModel):
    data: SeriesEpisodes


def fetch_episodes(request: RequestModel) -> SeriesEpisodes:
    url = urljoin(TVDB_API_URL, f"series/{request.query.series_id}/episodes")
    response_json = get(
        url,
        headers={"Authorization": request.token.token},
        params=request.query.dict(exclude={'id'}, exclude_none=True)
    ).json()
    return SeriesEpisodes(**response_json)


def handle(req: RequestModel) -> Union[ResponseModel, HTTPException]:
    try:
        result = fetch_episodes(req)
        res = ResponseModel(data=result)
    except Exception:
        raise HTTPException(status_code=500, detail=f"An API Error occurred")
    return res
