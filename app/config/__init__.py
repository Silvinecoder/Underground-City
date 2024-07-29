from app.assistant.environment import env

config = {
  "database": {
    "engine": "postgresql",
    "host": env(f"UNDERGROUND_DATABASE_HOST", "localhost"),
    "port": env(f"UNDERGROUND_DATABASE_PORT", "54321"),
    "schema": env(f"UNDERGROUND_DATABASE_SCHEMA", ""),
    "database_name": env(f"UNDERGROUND_DATABASE_NAME", "underground"),
    "username": env(f"UNDERGROUND_DATABASE_USERNAME", "underground"),
    "password": env(f"UNDERGROUND_DATABASE_PASSWORD", "underground")
  },
}

def get_config_params():  # pragma: unit
    """
    Gets the version of the application.
    """
    global config
    return config