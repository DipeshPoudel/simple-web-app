import mariadb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = mariadb.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('HOST'),
            port=3306,
            database=os.getenv('DB_NAME')
        )
        return connection
    except Exception as e:
        print(f"Unable to Connect to Database: {e}")

