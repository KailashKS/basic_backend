import datetime as _dt
from sqlalchemy import Column, Integer, String, DateTime

import database as _database


class DataaiSearch(_database.Base):
    __tablename__ = "dataai_search_history"
    query_id = Column(Integer, primary_key=True, index=True)
    search_query = Column(String, nullable=False)
    username = Column(String, nullable=False)
    search_pin = Column(String, default="N", nullable=False)
    report_pin = Column(String, default="N", nullable=False)
    chart_type = Column(String, default="table", nullable=False)
    last_modified = Column(DateTime, default=_dt.datetime.utcnow, nullable=False)
