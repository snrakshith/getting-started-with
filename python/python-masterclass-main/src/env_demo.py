import snowflake.connector
import os 
from dotenv import load_dotenv

load_dotenv()

#Configure the Connections
conn = snowflake.connector.connect(
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    account=os.getenv("ACCOUNT"),
    warehouse="COMPUTE_WH",
    database="DEMO_DB",
    schema="PUBLIC"
)

#Open a Cursor
cursor = conn.cursor()

#Execute a Query
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER,
    amount INTEGER,
    country STRING
    )
    """
)

#Insert a record
try:
    cursor.execute(
        """
        INSERT INTO orders(order_id, amount, country)
        VALUES (%s, %s, %s)
        """,
        (3, 100, "IN")
    )
    print("Insert successful")
except Exception as e:
    print("Insert failed:", e)

#Select Data from table
cursor.execute(
    "SELECT order_id, amount, country FROM orders"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

#Close Cursor
cursor.close()
conn.close()