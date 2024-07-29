from sqlalchemy import text
from app.db.db_connection import create_session

session = create_session()
query = session.execute(text("select * from product"))
result = query.fetchall()
print(result)
session.close()