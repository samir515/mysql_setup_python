from database import get_db_connection

# Function to check if email or phone exists
def user_exists(email, phone):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM users WHERE email = %s OR phone = %s"
    cursor.execute(query, (email, phone))
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()
    # Returns True if email/phone already exists
    return count > 0


# Create a new user with validation
def create_user(name, email, password, age, phone):
    if user_exists(email, phone):
        return {"error": "Email or phone already exists. Please use a different one."}
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email, password, age, phone, is_active) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, email, password, age, phone, True))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created successfully"}

# Fetch users based on active status
def get_users(active_only=True):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if active_only:
        cursor.execute("SELECT * FROM users WHERE is_active = TRUE")  # Fetch only active users
    else:
        cursor.execute("SELECT * FROM users")  # Fetch all users (active & inactive)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# for updating user using his id
def update_user(user_id, name=None, email=None,age=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET name = %s, email = %s,age = %sWHERE id = %s"
    cursor.execute(query, (name, email,age,user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User updated successfully"}

# Delete (Deactivate) User
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET is_active = %s WHERE id = %s"
    cursor.execute(query, (False, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User deactivated successfully"}

