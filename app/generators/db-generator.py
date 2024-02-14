import os
import sys
from sqlalchemy import create_engine, MetaData, Table

# Replace 'your_database_uri' with the actual URI for your PostgreSQL database
DATABASE_URI = ''

def snake_case_to_camelCase(text: str, capitalize_first_letter: bool = False) -> str:
    elements = text.split('_')
    first_word = elements[0].title() if capitalize_first_letter else f"{elements[0][0].lower()}{elements[0][1:]}"
    return f"{first_word}{''.join(t.title() for t in elements[1:])}"

def generate_postgres_schema(models_path="./module", module_prefix="module"):
    engine = create_engine(DATABASE_URI)
    metadata = MetaData()

    for filename in os.listdir(models_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = os.path.splitext(filename)[0]
            class_name = snake_case_to_camelCase(module_name, True)
            full_module_path = f"{module_prefix}.{module_name}"

            try:
                module = __import__(full_module_path, fromlist=[class_name])
                model_class = getattr(module, class_name)

                # Create the table schema using SQLAlchemy reflection
                table = Table(model_class.__tablename__, metadata, autoload_with=engine)
                print(f"\n-- Schema for {class_name} --\n")
                print(table.create())
            except (ImportError, AttributeError) as e:
                print(f"Error importing {module_name}: {e}")

if __name__ == "__main__":
    BASE_PATH = sys.argv[1] if len(sys.argv) > 1 else "./module"
    sys.path.append(BASE_PATH)

    generate_postgres_schema(BASE_PATH)