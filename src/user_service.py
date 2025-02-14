from database import get_db_connection
# for creating user using get_db_connection
def create_user(name,email,password,age,phone):
    conn = get_db_connection()
    cursor =conn.cursor()
    query="insert into users(name,email,password,age,phone,is_active) values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(name,email,password,age,phone,True))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message":"User created successfully"}

# for getting all user using get_db_connection
def get_users():
    conn = get_db_connection()
    cursor =conn.cursor(dictionary=True)
    cursor.execute("select * from users")
    users=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return users

# for updating user using his id
def update_user(user_id, name=None, email=None,age=None,phone=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET name = %s, email = %s,age = %s, phone = %s WHERE id = %s"
    cursor.execute(query, (name, email,age,phone, user_id))
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

