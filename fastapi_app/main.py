from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Base, engine, SessionLocal, User

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    count = db.query(User).count()
    return {"count": count}
