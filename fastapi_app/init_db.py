from models import User, Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

db = SessionLocal()
if User.select().count() == 0:
    for i in range(1000):
        db.add(User(name=f"User{i}", email=f"user{i}@test.com"))
    db.commit()
db.close()
