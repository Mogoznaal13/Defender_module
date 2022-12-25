from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, Query
from ..db_handler import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    serial_number = Column(String, unique=True, nullable=False)
    role = Column(String)


Base.metadata.create_all(bind=engine)


def getAllUsers():
    with Session(autoflush=True, bind=engine) as db:
        users = db.query(User).all()

    result = list()
    for user in users:
        result.append({
            'id': user.id,
            'name': user.name,
            'role': user.role,
            'serial_number': user.serial_number
        })
    return result


def getUserById(userId: int):
    with Session(autoflush=True, bind=engine) as db:
        user = db.query(User).filter(User.id == userId).first()

    result = {
        'id': user.id,
        'name': user.name,
        'role': user.role,
        'serial_number': user.serial_number
    }

    return result


def getUserByName(name: str):
    with Session(autoflush=True, bind=engine) as db:
        user = db.query(User).filter(User.name == name).first()

    return user


def getUsersByRole(role: str):
    with Session(autoflush=True, bind=engine) as db:
        users = db.query(User).filter(User.role == role).all()

    return users


def getUsersBySerialNumber(serialNumber: str):
    with Session(autoflush=True, bind=engine) as db:
        users = db.query(User).filter(User.serial_number == serialNumber).first()

    return users


def createUser(user: dict):
    user = User(name=user['name'], serial_number=user['serial_number'], role=user['role'])

    with Session(autoflush=True, bind=engine) as db:
        db.add(user)
        db.commit()

    return user


def updateUser(userId: int, attributes: dict):
    with Session(autoflush=True, bind=engine) as db:
        user = db.get(User, userId)

        if user is not None:
            user.name = attributes['name']
            user.serial_number = attributes['serial_number']
            user.role = attributes['role']
        else:
            user = False

    return user


def deleteUser(userId: int):
    with Session(autoflush=True, bind=engine) as db:
        user = db.get(User, userId)
        if user is not None:
            db.delete(user)
            db.commit()
        else:
            user = False

    return user
