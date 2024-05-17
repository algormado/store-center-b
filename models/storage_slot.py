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
    unit= db.Column (db.JSON,nullable = False)
    
    
    
    def __init__(self, size,  price,unit):
        self.size = size
        self.price = price
        self.unit = unit

   
