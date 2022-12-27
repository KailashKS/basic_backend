import database as _database
from sqlalchemy.orm import Session
import schemas as _schemas
import models as _models


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_query(db: Session, whole_query: _schemas.DataaiSearchCreate):
    db_query = _models.DataaiSearch(
        search_query=whole_query.search_query, username=whole_query.username
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_pinned(db: Session, username: str, pin_type: int, limit: int = 15):
    options = [_models.DataaiSearch.report_pin, _models.DataaiSearch.search_pin]
    db_results = (
        db.query(_models.DataaiSearch)
        .filter(
            options[pin_type] == "Y",
            _models.DataaiSearch.username == username,
        )
        .order_by(_models.DataaiSearch.last_modified.desc())
        .limit(limit)
        .all()
    )
    if db_results:
        return db_results
    return []


def get_recent(db: Session, username: str, limit: int = 15):
    db_results = (
        db.query(_models.DataaiSearch)
        .filter(_models.DataaiSearch.username == username)
        .order_by(_models.DataaiSearch.last_modified.desc())
        .limit(limit)
        .all()
    )
    if db_results:
        return db_results
    return [{"message": "Results not found."}]


def get_queries(db: Session):
    return db.query(_models.DataaiSearch).all() or {"message": "Results not found."}


def modify_pin(db: Session, query: str, pin_type: int, pinned: bool):
    change_pin = (
        db.query(_models.DataaiSearch)
        .filter(
            _models.DataaiSearch.search_query == query,
            _models.DataaiSearch.username == "gvai",
        )
        .first()
    )
    if change_pin:
        if pin_type:
            change_pin.search_pin = "Y" if pinned else "N"
        else:
            change_pin.report_pin = "Y" if pinned else "N"
        db.commit()
        db.refresh(change_pin)
        return change_pin
    return {"status": "Error"}
