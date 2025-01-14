import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Gather and organize environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


class SQLConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            self.cursor = self.connection.cursor()

            return self
        except psycopg2.Error as e:
            raise e # For DEVELOPMENT purposes

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # Log the error
            # return exc_type
            raise exc_val # For DEVELOPMENT purposes

        if self.connection:
            self.connection.close()
