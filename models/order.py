from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy import Integer, ForeignKey, Date, Boolean
from flask_bcrypt import Bcrypt
from config import db

bcrypt = Bcrypt()


class Order(db.Model, SerializerMixin):
    __tablename__ = 'order'  
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    storage_slot_id = db.Column(db.Integer, db.ForeignKey('storage_slot.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    is_picked_up = db.Column(Boolean)
    is_delivered = db.Column(Boolean)