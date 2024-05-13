#!/usr/bin/env python3

# Standard library imports
from random import randint,choice as rc
from datetime import datetime, timedelta

# Remote library imports
from faker import Faker

# Local imports
from app import app, db
from models import User, StorageSlot, Order, Delivery

def seed_storage_slots(num_slots=20):
    slot_sizes = ["small", "medium", "large"]
    slots = []
    for _ in range(num_slots):
        slot = StorageSlot(
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
    slots = StorageSlot.query.all()
    orders = []
    for _ in range(num_orders):
        start_date = datetime.now() - timedelta(days=randint(1, 30))  # Random start date within the last 30 days
        end_date = start_date + timedelta(days=randint(1, 30))  # Random end date within 30 days from start date
        order = Order(
            user=rc(users),
            storage_slot=rc(slots),
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
        delivery = Delivery(
            order=rc(orders),
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
        StorageSlot.query.delete()
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
