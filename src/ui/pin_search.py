from sqlalchemy.orm import Session
from fastapi import Depends
import services as _services
import schemas as _schemas
from typing import List
from fastapi import APIRouter

router = APIRouter(prefix="/search")


@router.get("/get/", response_model=List[_schemas.DataaiSearch])
def get_pinned_search(limit: int = 15, db: Session = Depends(_services.get_db)):
    return _services.get_pinned(
        db=db,
        pin_type=1,
        username="gvai",
        limit=limit,
    )


@router.post("/pin/", response_model=_schemas.DataaiSearch)
def pin_search(query: str, db: Session = Depends(_services.get_db)):
    return _services.modify_pin(query=query, db=db, pin_type=1, pinned=True)


@router.post("/unpin/", response_model=_schemas.DataaiSearch)
def unpin_search(query: str, db: Session = Depends(_services.get_db)):
    return _services.modify_pin(query=query, db=db, pin_type=1, pinned=False)
