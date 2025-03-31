from pony.orm import Required
from db import db

class User(db.Entity):
    name = Required(str)
    email = Required(str)

db.generate_mapping(create_tables=True)
