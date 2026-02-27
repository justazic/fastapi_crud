from sqlalchemy import Column, Integer, String, Float
from database import Base

class Computer(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    price = Column(Float)

