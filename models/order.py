from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy import Integer, ForeignKey, Date, Boolean
from flask_bcrypt import Bcrypt
from config import db

bcrypt = Bcrypt()

class Order(db.Model, SerializerMixin):
    __tablename__ = 'order'  
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    storage_slot_id = db.Column(Integer, ForeignKey('storage_slot.id'))
    start_date = db.Column(Date)
    end_date = db.Column(Date)  
    is_picked_up = db.Column(Boolean)
    is_delivered = db.Column(Boolean)
