from app.db.db_connection import create_session
from app.model.category import Category
from app.model.product import Product

session = create_session()

# create the tables
Category.metadata.create_all(session.bind)
Product.metadata.create_all(session.bind)

# Define the category name
category_name = "Meat"

# Get or create the category
category = Category.get_or_create(session, category_name)

# Create two product instances with the same category
product1 = Product(product_name="Beef", product_category=category)
product2 = Product(product_name="Chicken", product_category=category)

# Add the product instances to the session
session.add_all([product1, product2])

# Commit the changes to the database
session.commit()

# Query the database to verify the category count
category_count = session.query(Category).filter_by(category_name=category_name).count()
print(f"Number of categories with name '{category_name}': {category_count}")

# Close the session
session.close()
