from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import services as _services
import schemas as _schemas

app = FastAPI()

_services.create_database()


@app.get("/")
def root():
    NotImplemented


@app.post("/getQuery/", response_model=_schemas.DataaiSearch)
def store_query(
    query: _schemas.DataaiSearchCreate,
    db: Session = Depends(_services.get_db),
):

    # Do query to SQL conversion later
    return _services.add_query(db=db, whole_query=query)


from ui.pin_report import get_pinned_report, pin_report, unpin_report
from ui.pin_search import get_pinned_search, pin_search, unpin_search
from ui.recents import get_recent
