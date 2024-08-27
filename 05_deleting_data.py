from sqlalchemy.orm import sessionmaker

from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

user = session.query(User).filter_by(id=1).one_or_none()

print(user)

session.delete(user)

session.commit()
