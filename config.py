# ---------------------------------------------------------------------------
# Configuration for the Flask Auth App
# ---------------------------------------------------------------------------
# Update these values to match your local MySQL Community Server setup
MYSQL_HOST = "mysql-37954bda-akashdeepmitra221-0cb2.c.aivencloud.com"
MYSQL_USER = "avnadmin"                 # your MySQL userna
MYSQL_PASSWORD = "AVNS_IYlevqTSgeRhQ2yMJK8"    # your MySQL password
MYSQL_DB = "auth_app_db"            # the database created by schema.sql
MYSQL_PORT = 28772                  # default MySQL port

# Used by Flask to sign session cookies. Change this to any random string.
ssl_ca="D:/files/ca.pem"
SECRET_KEY = "aaaaa-bbbbbbb-ccccccc-ddddddd"
