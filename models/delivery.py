from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt
from config import db


class Delivery(db.Model):
    __tablename__ = 'delivery'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    delivery_address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Delivery id={self.id}, booking_id={self.booking_id}, delivery_date={self.delivery_date}, delivery_address={self.delivery_address}>"
 