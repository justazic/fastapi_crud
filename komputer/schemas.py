from pydantic import BaseModel



class ComputerBase(BaseModel):
    brand: str
    model: str
    price: float

class ComputerCreate(ComputerBase):
    pass

class ComputerOut(ComputerBase):
    id: int

    class Config:
        from_attributes = True
