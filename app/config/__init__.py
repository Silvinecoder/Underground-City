from app.assistant.environment import env

config = {
  "database": {
    "engine": "postgres",
    "host": env(f"UNDERGROUND_DATABASE_HOST", "localhost"),
    "port": env(f"UNDERGROUND_DATABASE_PORT", "5432"),
    "database_name": env(f"UNDERGROUND_DATABASE_NAME", "underground"),
    "schema": env(f"UNDERGROUND_DATABASE_SCHEMA", "public"),
    "username": env(f"UNDERGROUND_DATABASE_USERNAME", "underground"),
    "password": env(f"UNDERGROUND_DATABASE_PASSWORD", "underground")
  },
}