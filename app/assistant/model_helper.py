import re
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def camel_to_snake(name):
    """Convert CamelCase to snake_case as Javascript needs snake case."""
    return re.sub("([A-Z])", "_\\1", name).lower()


def from_json(cls, json_data):
    """
    Create an instance of a SQL model class from JSON data.
    And Maps camelCase JSON keys to snake_case SQL model fields.
    """
    model_fields = {column.name for column in cls.__table__.columns}
    filtered_data = {
        camel_to_snake(key): value
        for key, value in json_data.items()
        if camel_to_snake(key) in model_fields
    }
    return cls(**filtered_data)
