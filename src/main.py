import mysql.connector
# Connect to MySQL (replace 'localhost', 'root', and 'your_password' with your MySQL credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Localhost@123",
    database="firstdatabase"  # Specify your database name
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()
print("\nDatabase connected successfully!\n")

# Create a table (if it doesn’t exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)
""")

conn.commit()  # Save changes
print("Table created successfully!\n")

name = "Leo"
# Check if name exists
cursor.execute("SELECT COUNT(*) FROM users WHERE name = %s", (name,))
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    print("Inserted successfully!\n")
else:
    print("Duplicate entry detected, skipping insert of ", name, "\n")

# Fetching information from the database
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Get all rows
for row in rows:
    print(row)

# Updating information in the database
name = "samir"
id = 2
cursor.execute("UPDATE users SET name = %s WHERE id = %s", (name, id))
conn.commit()
print("\nData updated successfully!")
print("Data after successfully update becomes!")

# After updating table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Get all rows
for row in rows:
    print(row)

# Deleting data from the database (optional)
cursor.execute("DELETE FROM users WHERE id BETWEEN %s AND %s", (3, 20))
conn.commit()
print("Data deleted successfully!")

# After deleting table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # Get all rows
for row in rows:
    print(row)

print("\n")

conn.close()
x=input("enter the text")
if x == "hello":
    import second
else:
    print("something went wrong")