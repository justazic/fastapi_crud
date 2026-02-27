from sqlalchemy.orm import Session
import models, schemas

def create_computer(db: Session, computer: schemas.ComputerCreate):
    db_computer = models.Computer(**computer.model_dump())
    db.add(db_computer)
    db.commit()
    db.refresh(db_computer)
    return db_computer


def get_computers(db: Session):
    return db.query(models.Computer).all()


def get_computer(db: Session, computer_id: int):
    return db.query(models.Computer).filter(models.Computer.id == computer_id).first()


def update_computer(db: Session, computer_id: int, computer: schemas.ComputerCreate):
    db_computer = get_computer(db, computer_id)
    if db_computer:
        for key, value in computer.model_dump().items():
            setattr(db_computer, key, value)
        db.commit()
        db.refresh(db_computer)
    return db_computer


def delete_computer(db: Session, computer_id: int):
    db_computer = get_computer(db, computer_id)
    if db_computer:
        db.delete(db_computer)
        db.commit()
    return db_computer

