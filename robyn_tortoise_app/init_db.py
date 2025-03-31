import asyncio
from tortoise import Tortoise
from models import User
from tortoise_config import TORTOISE_ORM

async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    if await User.all().count() == 0:
        await User.bulk_create([
            User(name=f"User{i}", email=f"user{i}@test.com") for i in range(1000)
        ])
    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(init())
