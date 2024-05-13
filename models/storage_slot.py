from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, DECIMAL, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class StorageSlot(Base):
    _tablename_ = 'storage_slot'

    id = Column(Integer, primary_key=True)
    size = Column(Enum('small', 'medium', 'large'))
    availability = Column(Boolean)
    price = Column(DECIMAL)