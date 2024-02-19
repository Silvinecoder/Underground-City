# Import necessary modules
import logging
from app.db.db_connection import create_session, has_table_access

#Need to make this into an integration test

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a session
_SESSION = create_session()

# Test database access
table_name = "product"

if has_table_access(table_name):
    logging.info(f"Successfully accessed table: {table_name}")
else:
    logging.warning(f"Failed to access table: {table_name}")
