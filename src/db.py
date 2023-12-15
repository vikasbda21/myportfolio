import psycopg2 as ps
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_db():
    print("Connecting to database")

    try:
        connection = ps.connect(
            host = os.getenv("db_host"), 
            port = os.getenv("db_port"),
            database=os.getenv("db_name"),
            user = os.getenv("db_user"),
            password=os.getenv("db_password")
        )

        cursor = connection.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print("PostgreSQL version:", version)
    
    except Exception as e:
        print("Error: Unable to connect to the database.", e)

    finally:
        if connection:
            connection.close()
            print("Database connection closed")



connect_to_db()