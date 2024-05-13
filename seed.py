#!/usr/bin/env python3

# Standard library imports
from random import randint,choice as rc
from datetime import datetime, timedelta

# Remote library imports
from faker import Faker

# Local imports
from app import app, db
from models.delivery import Delivery
from models.order import Order
from models.storage_slot import Storage_slot
from models.user import User

def seed_storage_slots(num_slots=20):
    slot_sizes = ["small", "medium", "large"]
    slots = []
    for _ in range(num_slots):
        slot = Storage_slot(
            size=rc(slot_sizes),
            availability=True,
            price=randint(50, 200)
        )
        slots.append(slot)
        db.session.add(slot)
    db.session.commit()
    return slots

def seed_users(num_users=50):
    users = []
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            role="client"  # Assuming all seeded users are clients
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()
    return users

def seed_orders(num_orders=50):
    users = User.query.all()
    slots = Storage_slot.query.all()
    orders = []
    for _ in range(num_orders):
        start_date = datetime.now() - timedelta(days=randint(1, 30))
        end_date = start_date + timedelta(days=randint(1, 30))
        # Select a random user and storage slot
        user = rc(users)
        storage_slot = rc(slots)
        # Create the order using user_id and storage_slot_id
        order = Order(
            user_id=user.id,
            storage_slot_id=storage_slot.id,
            start_date=start_date,
            end_date=end_date
        )
        orders.append(order)
        db.session.add(order)
    db.session.commit()
    return orders

def seed_deliveries(num_deliveries=20):
    orders = Order.query.all()
    deliveries = []
    for _ in range(num_deliveries):
        delivery_date = datetime.now() + timedelta(days=randint(1, 30))  # Random delivery date within the next 30 days
        # Select a random order
        order = rc(orders)
        # Create the delivery using order_id
        delivery = Delivery(
            order_id=order.id,
            delivery_date=delivery_date,
            delivery_address=fake.address()
        )
        deliveries.append(delivery)
        db.session.add(delivery)
    db.session.commit()
    return deliveries

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        print("Clearing db...")
        Storage_slot.query.delete()
        Order.query.delete()
        Delivery.query.delete()
        User.query.delete()

        print("Starting seed...")

        print("seeding storage slots...")
        storage_slots = seed_storage_slots()

        print("seeding users...")
        users = seed_users()

        print("seeding orders...")
        orders = seed_orders()

        print("seeding deliveries...")
        deliveries = seed_deliveries()

        print("Seed completed successfully!")
