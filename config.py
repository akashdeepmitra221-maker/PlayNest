# ---------------------------------------------------------------------------
# Configuration for the Flask Auth App
# ---------------------------------------------------------------------------
# Update these values to match your local MySQL Community Server setup
# (the same credentials you use to log into MySQL Workbench).

MYSQL_HOST = "localhost"
MYSQL_USER = "root"                 # your MySQL username
MYSQL_PASSWORD = "Akash@12345!"    # your MySQL password
MYSQL_DB = "auth_app_db"            # the database created by schema.sql
MYSQL_PORT = 3306                   # default MySQL port

# Used by Flask to sign session cookies. Change this to any random string.
SECRET_KEY = "change-this-to-a-long-random-secret-string"
