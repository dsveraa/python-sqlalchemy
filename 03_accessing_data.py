from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

users = session.query(User).all()

# print(users)
# print(users[0])

user = users[1]

print(f'\n{user.id}')
print(user.name)
print(user.age)

print('\n')
for user in users:
    print(f'User id: {user.id}, name: {user.name}, age: {user.age}')

print('\n')

users = session.query(User).filter_by(age=39).all()
print(f'Lista:\n{users}\n')

users = session.query(User).filter_by(id=1).one_or_none()
print(f'Una o ninguna:\n{users}\n')

users = session.query(User).filter_by(id=0).one_or_none()
print(f'Una o ninguna:\n{users}\n')

#users = session.query(User).filter_by(age=39).one_or_none() # error if there are two same entries
#print(f'Una o ninguna:\n{users}\n')

user = session.query(User).filter_by(id=4).one_or_none()

print(user.name)

user.name = 'Davicito Vera' # this was David Vera before

print(user.name)

session.commit() # update database commiting changes
