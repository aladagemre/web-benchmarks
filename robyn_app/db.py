from pony.orm import Database
import os

db = Database()
db.bind(
    provider="postgres",
    user=os.getenv("POSTGRES_USER", "robynuser"),
    password=os.getenv("POSTGRES_PASSWORD", "robynpass"),
    host=os.getenv("POSTGRES_HOST", "postgres"),
    database=os.getenv("POSTGRES_DB", "robyn_db")
)
