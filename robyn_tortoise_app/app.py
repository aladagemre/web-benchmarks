from robyn import Robyn
from tortoise import Tortoise, run_async
from models import User
from tortoise_config import TORTOISE_ORM
import json

app = Robyn(__file__)

@app.get("/")
def home():
    return "Robyn + TortoiseORM + PostgreSQL ✅"

@app.get("/users")
async def get_users(request):
    count = await User.all().count()
    return json.dumps({"count": count})

async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())  # tam async bağlanma, havuz hatası çözülür
    app.start(port=8003, host="0.0.0.0")
