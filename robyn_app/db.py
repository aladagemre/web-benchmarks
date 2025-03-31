from pony.orm import Database

db = Database()
db.bind(provider="sqlite", filename="test.db", create_db=True)
