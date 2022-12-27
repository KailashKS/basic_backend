import datetime as _dt
from pydantic import BaseModel
from typing import Optional


class _DataaiSearchBase(BaseModel):
    query_id: int
    search_query: str
    username: str


class DataaiSearchCreate(_DataaiSearchBase):
    pass


class DataaiSearch(_DataaiSearchBase):
    query_id: int
    search_query: str
    username: str
    search_pin: str
    report_pin: str
    chart_type: str
    last_modified: _dt.datetime

    class Config:
        orm_mode = True


class DataaiSearchPinUpdate(BaseModel):
    search_query: str
    username: str
    search_pin: Optional[str]
    report_pin: Optional[str]
    chart_type: Optional[str]
