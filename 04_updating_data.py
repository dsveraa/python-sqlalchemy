from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user = session.query(User).filter_by(id=4).one_or_none()

print(user.name)

user.name = 'Davicito Vera' # this was David Vera before

print(user.name)

session.commit() # update database commiting changes