from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


users_all = session.query(User).all()
print(f'all users: {len(users_all)}')


users_filter = session.query(User).filter(User.age >= 25).all()
print(f'users with age >= 25: {len(users_filter)}')

users_filter = session.query(User).filter(User.age >= 25, User.name == 'David Vera').all()
print(f'users with age >= 25 and called David Vera: {len(users_filter)}')

