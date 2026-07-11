import os
from dotenv import load_dotenv

MYSQL_HOST = os.getenv("host")
MYSQL_USER = os.getenv("user")              # your MySQL username
MYSQL_PASSWORD =  os.getenv("pas")   # your MySQL password
MYSQL_DB = os.getenv("db")           # the database created by schema.sql
MYSQL_PORT =  os.getenv("port")                 # default MySQL port
SECRET_KEY = os.getenv("secret")
CA = os.getenv("file")