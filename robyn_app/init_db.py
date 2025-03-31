from pony.orm import db_session
from models import User
from db import db


@db_session
def populate():
    if User.select().count() == 0:
        for i in range(1000):
            User(name=f"User{i}", email=f"user{i}@test.com")
populate()
