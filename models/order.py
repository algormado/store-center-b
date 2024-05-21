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
    item = db.Column(db.String(255), nullable=False)
    deliveries = db.relationship('Delivery', backref='order')
   
    serialize_only = ('id','user_id','storage_slot_id ','start_date','end_date','is_picked_up','is_delivered','item')
    

    
    
    def __init__(self, user_id, storage_slot_id, start_date, end_date, item, ):
        self.user_id = user_id
        self.storage_slot_id = storage_slot_id
        self.start_date = start_date
        self.end_date = end_date
        self.item = item
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'storage_slot_id': self.storage_slot_id,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'is_picked_up': self.is_picked_up,
            'is_delivered': self.is_delivered,
            'item': self.item
        }
        
        
   