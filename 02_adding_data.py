from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user = User(name="David Vera", age=39)
user_2 = User(name="Simon Vera", age=34)
user_3 = User(name="Alejandra Saldaña", age=39)
user_4 = User(name="David Vera", age=16)

session.add(user)
session.add(user_2)
session.add_all([user_3, user_4])

session.commit()
