"""
Models generated from the TVDb API v3 Swagger spec:
https://api.thetvdb.com/swagger
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class Episode(BaseModel):
    absolute_number: Optional[int] = Field(None, alias="absoluteNumber")
    aired_episode_number: Optional[int] = Field(None, alias="airedEpisodeNumber")
    aired_season: Optional[int] = Field(None, alias="airedSeason")
    airs_after_season: Optional[int] = Field(None, alias="airsAfterSeason")
    airs_before_episode: Optional[int] = Field(None, alias="airsBeforeEpisode")
    airs_before_season: Optional[int] = Field(None, alias="airsBeforeSeason")
    director: Optional[str]
    directors: Optional[List[str]]
    dvd_chapter: Optional[float] = Field(None, alias="dvdChapter")
    dvd_discid: Optional[str] = Field(None, alias="dvdDiscid")
    dvd_episode_number: Optional[float] = Field(None, alias="dvdEpisodeNumber")
    dvd_season: Optional[int] = Field(None, alias="dvdSeason")
    episode_name: Optional[str] = Field(None, alias="episodeName")
    filename: Optional[str]
    first_aired: Optional[str] = Field(None, alias="firstAired")
    guest_stars: Optional[List[str]] = Field(None, alias="guestStars")
    id: Optional[int]
    imdb_id: Optional[str] = Field(None, alias="imdbId")
    last_updated: Optional[int] = Field(None, alias="lastUpdated")
    last_updated_by: Optional[str] = Field(None, alias="lastUpdatedBy")
    overview: Optional[str]
    production_code: Optional[str] = Field(None, alias="productionCode")
    series_id: Optional[str] = Field(None, alias="seriesId")
    show_url: Optional[str] = Field(None, alias="showUrl")
    site_rating: Optional[float] = Field(None, alias="siteRating")
    site_rating_count: Optional[int] = Field(None, alias="siteRatingCount")
    thumb_added: Optional[str] = Field(None, alias="thumbAdded")
    thumb_author: Optional[int] = Field(None, alias="thumbAuthor")
    thumb_height: Optional[str] = Field(None, alias="thumbHeight")
    thumb_width: Optional[str] = Field(None, alias="thumbWidth")
    writers: Optional[List[str]]


class JSONErrors(BaseModel):
    invalid_filters: Optional[List[str]] = Field(
        None, alias="invalidFilters", description="Invalid filters passed to route"
    )
    invalid_language: Optional[str] = Field(
        None,
        alias="invalidLanguage",
        description="Invalid language or translation missing",
    )
    invalid_query_params: Optional[List[str]] = Field(
        None,
        alias="invalidQueryParams",
        description="Invalid query params passed to route",
    )


class Links(BaseModel):
    first: Optional[int]
    last: Optional[int]
    next: Optional[int]
    previous: Optional[int]


class SeriesEpisodes(BaseModel):
    data: Optional[List[Episode]]
    errors: Optional[JSONErrors]
    links: Optional[Links]


class SeriesEpisodesQuery(BaseModel):
    series_id: int = Field(None, alias="id")
    page: int


class Token(BaseModel):
    token: str
