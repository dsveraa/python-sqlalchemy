from sqlalchemy import and_, not_, or_
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


users = session.query(User).where(User.age >= 30).all()

for user in users:
    print(f'age: {user.age}')
print('\n')

users = session.query(User).where(User.age <= 40, User.name == 'David Vera').all() # and

for user in users:
    print(f'name: {user.name}, age: {user.age}')
print('\n')

users = session.query(User).where(or_(User.age <= 20, User.name == 'David Vera')).all() # or

for user in users:
    print(f'name: {user.name}, age: {user.age}')
print('\n')

users = session.query(User).where(or_(User.age <= 20, User.name == 'David Vera')).all() # or

for user in users:
    print(f'name: {user.name}, age: {user.age}')
print('\n')

users = session.query(User).where((User.age <= 20) | (User.name == 'David Vera')).all() # or

for user in users:
    print(f'name: {user.name}, age: {user.age}')
print('\n')

users = session.query(User).where(not_(User.name == 'Juan Pablo')).all() # not

for user in users:
    print(f'name: {user.name}, age: {user.age}')
print('\n')

users = session.query(User).where(not_(User.name == 'Juan Pablo')).all() # not

for user in users:
    print(f'name: {user.name}, age: {user.age}')
print('\n')

users = session.query(User).where(
    and_(
        not_(User.name == 'Juan Contreras'),
        and_(
            User.age >= 30, 
            User.age < 40)
    )
).all()

for user in users:
    print(f'{user.name} - {user.age}')
print('\n')
