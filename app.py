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
    def get(self):
        # Implement the logic to retrieve all orders
        orders = [
            {'id': 1, 'customer': 'John Doe', 'items': ['Item 1', 'Item 2']},
            {'id': 2, 'customer': 'Jane Smith', 'items': ['Item 3', 'Item 4']}
        ]
        return orders, 200

    def post(self):
        # Implement the logic to create a new order
        data = request.get_json()
        new_order = {
            'id': len(orders) + 1,
            'customer': data['customer'],
            'items': data['items']
        }
        orders.append(new_order)
        return new_order, 201

class OrderResource(Resource):
    def get(self):
        # Implement the logic to retrieve all orders
        orders = [
            {'id': 1, 'customer': 'John Doe', 'items': ['Item 1', 'Item 2']},
            {'id': 2, 'customer': 'Jane Smith', 'items': ['Item 3', 'Item 4']}
        ]
        return orders, 200

    def post(self):
        # Implement the logic to create a new order
        data = request.get_json()
        new_order = {
            'id': len(orders) + 1,
            'customer': data['customer'],
            'items': data['items']
        }
        orders.append(new_order)
        return new_order, 201

class OrderByID(Resource):
    def get(self, order_id):
        # Implement the logic to retrieve a specific order by ID
        order = next((o for o in orders if o['id'] == order_id), None)
        if order:
            return order, 200
        else:
            return {'message': 'Order not found'}, 404

    def put(self, order_id):
        # Implement the logic to update a specific order by ID
        data = request.get_json()
        order = next((o for o in orders if o['id'] == order_id), None)
        if order:
            order['customer'] = data['customer']
            order['items'] = data['items']
            return order, 200
        else:
            return {'message': 'Order not found'}, 404

    def delete(self, order_id):
        # Implement the logic to delete a specific order by ID
        order = next((o for o in orders if o['id'] == order_id), None)
        if order:
            orders.remove(order)
            return {}, 204
        else:
            return {'message': 'Order not found'}, 404

class DeliveryResource(Resource):
    def get(self):
        # Implement the logic to retrieve all deliveries
        deliveries = [
            {'id': 1, 'order_id': 1, 'status': 'Shipped'},
            {'id': 2, 'order_id': 2, 'status': 'Delivered'}
        ]
        return deliveries, 200

    def post(self):
        # Implement the logic to create a new delivery
        data = request.get_json()
        new_delivery = {
            'id': len(deliveries) + 1,
            'order_id': data['order_id'],
            'status': 'Pending'
        }
        deliveries.append(new_delivery)
        return new_delivery, 201

class DeliveryByID(Resource):
    def get(self, delivery_id):
        # Implement the logic to retrieve a specific delivery by ID
        delivery = next((d for d in deliveries if d['id'] == delivery_id), None)
        if delivery:
            return delivery, 200
        else:
            return {'message': 'Delivery not found'}, 404

    def put(self, delivery_id):
        # Implement the logic to update a specific delivery by ID
        data = request.get_json()
        delivery = next((d for d in deliveries if d['id'] == delivery_id), None)
        if delivery:
            delivery['status'] = data['status']
            return delivery, 200
        else:
            return {'message': 'Delivery not found'}, 404

    def delete(self, delivery_id):
        # Implement the logic to delete a specific delivery by ID
        delivery = next((d for d in deliveries if d['id'] == delivery_id), None)
        if delivery:
            deliveries.remove(delivery)
            return {}, 204
        else:
            return {'message': 'Delivery not found'}, 404
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
