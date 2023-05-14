import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv("host"),
    database=os.getenv("database"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    port=os.getenv("port")
    )