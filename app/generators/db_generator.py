import sys
from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import postgresql

def generate_postgres_schema(models_path="../model") -> list:
    table_order = [
        "attribute",
        "category",
        "product",
        "supermarket",
        "supermarket_product_pair",
        "supermarket_category_pair"
    ]

    for table_name in table_order:
            module_name = table_name.replace("_", " ").title().replace(" ", "")
            full_module_path = f"app.model.{table_name}"
            module = __import__(full_module_path, fromlist=[module_name])
            module_class = getattr(module, module_name)
            create_schema = CreateTable(module_class.__table__).compile(
                dialect=postgresql.dialect()
            )
            print(f"{create_schema};".replace("\n\n;", ";"))


if __name__ == "__main__":
    BASE_PATH = sys.argv[1] if len(sys.argv) > 1 else "../model"
    sys.path.append(BASE_PATH)
    generate_postgres_schema(BASE_PATH)