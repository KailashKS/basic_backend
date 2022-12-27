from main import app
from sqlalchemy.orm import Session
from fastapi import Depends
import services as _services
import schemas as _schemas
from typing import List


@app.get("/recents/", response_model=List[_schemas.DataaiSearch])
def get_recent(limit: int = 15, db: Session = Depends(_services.get_db)):
    return _services.get_recent(db=db, username="sekhark", limit=limit)
