from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from sqlalchemy import Integer, ForeignKey, Date, Boolean
from flask_bcrypt import Bcrypt
from config import db



class StorageSlot(db.Model,SerializerMixin):
    __tablename__ = 'storage_slot'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(10), nullable=False)  # small, medium, large
    availability = db.Column(db.Boolean, nullable=False, default=True)
    price = db.Column(db.Float, nullable=False)