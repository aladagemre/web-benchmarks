import json
from robyn import Robyn, Config
from pony.orm import db_session, select
from models import User
from db import db

config = Config()
config.workers = 1
app = Robyn(__file__, config=config)

@app.get("/users")
@db_session
def get_users(request):
    count = User.select().count()
    return json.dumps({"count": count})
    

@app.get("/")
def root():
    return "Robyn + PonyORM is alive 🚀"

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8002)
