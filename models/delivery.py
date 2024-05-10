from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt
from config import db

bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    role = db.Column(db.String(10), nullable=False) 
    
    serialize_only = ('id', 'username', 'email')

    @validates('username')
    def validate_username(self, key, username):
        existing_user = User.query.filter(User.username == username).first()
        if existing_user:
            raise ValueError("Username already exists")
        return username

    @validates('email')
    def validate_email(self, key, email):
        existing_email = User.query.filter(User.email == email).first()
        if existing_email:
            raise ValueError("Email already exists")
        return email

    @validates('role')
    def validate_role(self, key, role):
        if role not in ['admin', 'user']:
            raise ValueError("Role must be 'admin' or 'user'")
        return role

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'
