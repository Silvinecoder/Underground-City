from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable

from app.model.product import Product

print(CreateTable(Product.__table__).compile(dialect=postgresql.dialect()))