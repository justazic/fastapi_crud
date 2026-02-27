from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/computers/", response_model=schemas.ComputerOut)
def create_computer(computer: schemas.ComputerCreate, db: Session = Depends(get_db)):
    return crud.create_computer(db, computer)


@router.get("/computers/", response_model=list[schemas.ComputerOut])
def read_computers(db: Session = Depends(get_db)):
    return crud.get_computers(db)


@router.get("/computers/{computer_id}", response_model=schemas.ComputerOut)
def read_computer(computer_id: int, db: Session = Depends(get_db)):
    db_computer = crud.get_computer(db, computer_id)
    if not db_computer:
        raise HTTPException(status_code=404, detail="Computer topilmadi")
    return db_computer


@router.post("/computers/{computer_id}", response_model=schemas.ComputerOut)
def update_computer(computer_id: int, computer: schemas.ComputerCreate, db: Session = Depends(get_db)):
    db_computer = crud.update_computer(db, computer_id, computer)
    if not db_computer:
        raise HTTPException(status_code=404, detail="Computer topilmadi")
    return db_computer


