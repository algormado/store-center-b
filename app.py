from flask import request,session,jsonify,make_response
from flask_restful import Resource
from config import app, db, api
from models.delivery import Delivery
from models.order import Order
from models.storage_slot import Storage_slot
from models.user import User



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

class Storage_Slot(Resource):
    def get(self):
        slots = [slot.to_dict() for slot in Storage_slot.query.all()]
        return make_response(jsonify(slots), 200)
    
    def post(self):
        data = request.get_json()
        if not all(key in data for key in ['availability', 'size', 'price']):
            return make_response(jsonify({"error": "Validation error: Missing required fields."}), 400)

        try:
            slot = Storage_slot(availability=data['availability'], size=data['size'], price=data['price'])
            db.session.add(slot)
            db.session.commit()
            return make_response(jsonify({"message": "Storage slot created successfully.", "slot": slot.to_dict()}), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Failed to create storage slot.", "details": str(e)}), 400)

        
    
class Storage_SlotByID(Resource):
    def get(self, id):
        storage_slot = Storage_slot.query.filter_by(id=id).first()
        if not storage_slot:
            response_dict = {"error": "Storage slot not found"}
            return make_response(jsonify(response_dict), 404)
        
        response_data = {
            'id': storage_slot.id,
            'size': storage_slot.size,
            'availability': storage_slot.availability,
            'price': storage_slot.price
        }
        
        return make_response(jsonify(response_data), 200)

    def patch(self, id):
        storage_slot = Storage_slot.query.filter_by(id=id).first()
        if not storage_slot:
            response_dict = {"error": "Storage slot not found"}
            return make_response(jsonify(response_dict), 404)
        
        data = request.get_json()
        if 'availability' in data:
            storage_slot.availability = data['availability']
        if 'size' in data:
            storage_slot.size = data['size']
        if 'price' in data:
            storage_slot.price = data['price']
        
        try:
            db.session.commit()
            return make_response(jsonify({"message": "Storage slot updated successfully.", "slot": storage_slot.to_dict()}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Failed to update storage slot.", "details": str(e)}), 400)

    def delete(self, id):
        storage_slot = Storage_slot.query.filter_by(id=id).first()
        if not storage_slot:
            response_dict = {"error": "Storage slot not found"}
            return make_response(jsonify(response_dict), 404)
        
        try:
            db.session.delete(storage_slot)
            db.session.commit()
            return make_response(jsonify({"message": "Storage slot deleted successfully."}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Failed to delete storage slot.", "details": str(e)}), 400)

   

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')  
        user = User.query.filter(User.username == username).first()
        
        if user and user.authenticate(data['password']):
            session['user_id'] = user.id
            return user.to_dict(), 200
        
        return {}, 401
    


class Signup(Resource):
    
    def post(self):
        json = request.get_json()
        user = User(
            username=json['username'],
            email=json['email']
        )
        user.password_hash = json['password']
        db.session.add(user)
        db.session.commit()
        return user.to_dict(), 201
 
class Logout(Resource):
    def delete(self):
        session.pop('user_id',None)
        return {},204

class CheckSession(Resource):
    def get(self):
        user_id = session['user_id']
        if user_id is not None:
            user = User.query.filter(User.id == user_id).first()
            if user is not None:
                return user.to_dict()
        
        return {},204

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(OrderResource, '/orders')
api.add_resource(OrderByID, '/orders/<int:id>')
api.add_resource(DeliveryResource, '/deliveries')
api.add_resource(DeliveryByID, '/deliveries/<int:id>')
api.add_resource(Storage_Slot, '/0')
api.add_resource(Storage_SlotByID, '/storage_slots/<int:id>')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
