from sqlalchemy import Column, Integer, Date, Boolean, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Order(Base):
    _tablename_ = 'order'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    storage_slot_id = Column(Integer, ForeignKey('storage_slot.id'))
    start_date = Column(Date)
    end_date = Column(Boolean)
    is_picked_up = Column(Boolean)
    is_delivered = Column(Boolean)