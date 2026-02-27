from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    price: float

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True