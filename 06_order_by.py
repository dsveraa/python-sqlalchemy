from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

""" 
# add random info to the database based on lists

import random

names = ["Juan Pablo", "Paul Colignon", "David Vera", "Alejandra Saldaña", "Sergio Morales", "Juan Contreras"]
ages = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

for x in range(20):
    user = User(name=random.choice(names), age=random.choice(ages))
    session.add(user)
    
session.commit() 

"""

print('\nQuery all users sorted by age:')
users = session.query(User).order_by(User.age).all()

for user in users:
    print(f'User age: {user.age}, name: {user.name}, id: {user.id}')
    

print('\nQuery all users sorted by age (descending):')
users = session.query(User).order_by(User.age.desc()).all()

for user in users:
    print(f'User age: {user.age}, name: {user.name}, id: {user.id}')

print('\nQuery all users sorted by age and name:')
users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print(f'User age: {user.age}, name: {user.name}, id: {user.id}')
    