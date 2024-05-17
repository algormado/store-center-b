#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from datetime import datetime, timedelta

# Remote library imports
from faker import Faker

# Local imports
from app import app, db
from models.delivery import Delivery
from models.order import Order
from models.storage_slot import Storage_slot
from models.user import User

def seed_storage_slots(num_slots=50):
    slot_sizes = {
        "small": ["5'x5'", "5'x10'", "5'x15'"],
        "medium": ["10'x10'", "10'x15'", "10'x20'",],
        "large": ["15'x15'", "20'x20'", "20'x25'",]
    }
    slots = []
    for _ in range(num_slots):
        size = rc(list(slot_sizes.keys()))
        slot = Storage_slot(
            size=size,
            price=randint(50, 200),
            unit=slot_sizes[size]
        )
        slots.append(slot)
        db.session.add(slot)
    db.session.commit()
    return slots

def seed_users(num_users=50):
    fake = Faker()
    users = []
    for _ in range(num_users):
        role = rc(["admin", "client", "employee"])
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            role=role
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
        user = rc(users)
        storage_slot = rc(slots)
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
    fake = Faker()
    orders = Order.query.all()
    deliveries = []
    for _ in range(num_deliveries):
        delivery_date = datetime.now() + timedelta(days=randint(1, 30))
        order = rc(orders)
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
        Delivery.query.delete()
        Order.query.delete()
        Storage_slot.query.delete()
        User.query.delete()

        print("Starting seed...")

        print("Seeding storage slots...")
        storage_slots = seed_storage_slots()

        print("Seeding users...")
        users = seed_users()

        print("Seeding orders...")
        orders = seed_orders()

        print("Seeding deliveries...")
        deliveries = seed_deliveries()

        print("Seed completed successfully!")
