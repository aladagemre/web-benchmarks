TORTOISE_ORM = {
    "connections": {
        "default": "postgres://robynuser:robynpass@postgres:5432/robyn_db"
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    }
}
