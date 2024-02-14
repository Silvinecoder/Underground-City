import os
import sys
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql

def generate_postgres_schema(models_path="../model") -> list:

    for filename in os.listdir(models_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = os.path.splitext(filename)[0]
            class_name = module_name.capitalize()
            full_module_path = f"app.model.{module_name}"

            print(full_module_path)

            module = __import__(full_module_path, fromlist=[class_name])
            module_class = getattr(module, class_name)
            print(f"{CreateTable(module_class.__table__).compile(dialect=postgresql.dialect())}")


if __name__ == "__main__":
    BASE_PATH = sys.argv[1] if len(sys.argv) > 1 else "../model"
    sys.path.append(BASE_PATH)

    generate_postgres_schema(BASE_PATH)