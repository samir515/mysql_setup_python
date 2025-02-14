import mysql.connector
DB_CONFIG={
    "host":"localhost",
    "user":"root",
    "password":"Localhost@123",
    "database":"firstdatabase"
}
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)