from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy import Integer, ForeignKey, Date, Boolean
from flask_bcrypt import Bcrypt
from config import db



class Storage_slot(db.Model,SerializerMixin):
    __tablename__ = 'storage_slot'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(10), nullable=False) 
    availability =db.Column(Boolean)
    price = db.Column(db.Integer)
    unit_details = db.Column (db.JSON,nullable = False)
    what_can_fit =db. Column(db.JSON, nullable=False)
    
    units = db.relationship("Unit", back_populates="storage_slot", cascade="all, delete-orphan")
    
    serialize_only = ('id', 'size', 'price', 'availability', 'unit_details', 'what_can_fit')

    
    def __init__(self, size,price,what_can_fit,unit_details ):
        self.size = size
        self.price = price
        self.unit_details  = unit_details 
        self.what_can_fit =  what_can_fit

   
