import random

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# group user by age
# (it takes the first row related to the age from the lower to the higher) 
users = session.query(User).group_by(User.age).all() # SELECT * FROM users GROUP BY age;

print(f'\n{users}')

# group user.age by age
# (it do the same but only showing the age data, resulting in a list of tuples of every age from the lower to the higher)
users = session.query(User.age).group_by(User.age).all() # SELECT age FROM users GROUP BY age;

print(f'\n{users}')

# using func.count you get the quantity of users who have the same age
users = session.query(User.age, func.count(User.id)).group_by(User.age).all() 

print(f'\n{users}')

# using func.count you get the quantity of users who have the same name
users = session.query(User.name, func.count(User.id)).group_by(User.name).all() 

print(f'\n{users}\n')


# chaining several parameters

""" 

SELECT age, COUNT(id)
FROM users
WHERE age > 24 AND age < 35
GROUP BY age
ORDER BY "age";

"""

users_tuple = (
    session.query(User.age, func.count(User.id)) # SELECT age, COUNT(id) FROM users
    .filter(User.age > 24) # WHERE age > 24
    .filter(User.age < 35) # AND age < 35
    .order_by(User.age) # ORDER BY "age"
    .group_by(User.age) # GROUP BY age
    .all()
)

for age, count in users_tuple:
    print(f'Age: {age} - {count} users')

# conditionals

print('\n')

only_david_vera = True
group_by_age = True

users = session.query(User)

if only_david_vera:
    users = users.filter(User.name == 'David Vera')

if group_by_age:
    users = users.group_by(User.age)
    
users = users.all()

for user in users:
    print(f'User age: {user.age}, name: {user.name}')


print('\n')
users = session.query(User).group_by(User.age).all()
    
for user in users:
    print(f'User age: {user.age}, name: {user.name}')


print('\n')
users = session.query(User).filter(User.name == 'David Vera').group_by(User.age).all()

for user in users:
    print(f'User age: {user.age}, name: {user.name}')
    