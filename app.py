from flask import request,session,jsonify,make_response
from flask_restful import Resource
from config import app, db, api
from models.delivery import Delivery
from models.order import Order
from models.storage_slot import Storage_slot
from models.user_role import UserRole


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class ClearSession(Resource):
    def delete(self):
        session.clear()
        return {}, 204

class OrderResource(Resource):
   
        pass
    
   
class OrderByID(Resource):
   
        pass

class DeliveryResource(Resource):
    
        pass

class DeliveryByID(Resource):
        pass

class Storage_SlotResource(Resource):
  
        pass

class Storage_SlotByID(Resource):
    pass

class Login(Resource):
    def post(self):
        # Implement login functionality
        pass

class Signup(Resource):
    def post(self):
        # Implement signup functionality
        pass

class Logout(Resource):
    pass

class CheckSession(Resource):
    def get(self):
        # Implement checking session functionality
        pass

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(OrderResource, '/orders')
api.add_resource(OrderByID, '/orders/<int:id>')
api.add_resource(DeliveryResource, '/deliveries')
api.add_resource(DeliveryByID, '/deliveries/<int:id>')
api.add_resource(Storage_SlotResource, '/storage_slots')
api.add_resource(Storage_SlotByID, '/storage_slots/<int:id>')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
