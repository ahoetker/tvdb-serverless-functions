"""
Models generated from the TVDb API v3 Swagger spec:
https://api.thetvdb.com/swagger
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class SeriesSearchQuery(BaseModel):
    name: Optional[str] = Field(None, description="Name of the series to search for.")
    imdb_id: Optional[str] = Field(
        None, alias="imdbId", description="IMDB id of the series"
    )
    zap2it_id: Optional[str] = Field(
        None, alias="zap2itId", description="Zap2it ID of the series to search for."
    )
    slug: Optional[str] = Field(
        None,
        description="Slug from site URL of series (https://www.thetvdb.com/series/$SLUG)",
    )


class SeriesSearchResult(BaseModel):
    aliases: Optional[List[str]]
    banner: Optional[str]
    first_aired: Optional[str] = Field(None, alias="firstAired")
    id: Optional[int]
    image: Optional[str]
    network: Optional[str]
    overview: Optional[str]
    poster: Optional[str]
    series_name: Optional[str] = Field(None, alias="seriesName")
    slug: Optional[str]
    status: Optional[str]


class SeriesSearchResults(BaseModel):
    data: Optional[List[SeriesSearchResult]]


class Token(BaseModel):
    token: str