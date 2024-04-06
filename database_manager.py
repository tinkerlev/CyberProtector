import sqlite3
from sqlite3 import Error
import hashlib
import os


def create_connection():
    """
    Establish a connection to an SQLite database specified by the path to the database file.
    Returns a connection object if successful, or None if an error occurs.
    """
    db_file = "./my_new_database.db"
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to the database.")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None


def create_table(conn, sql):
    """
    Create a table using the provided SQL statement.
    This function takes a connection object and a string containing a SQL statement to create a table.
    It prints a success message or an error if the table cannot be created.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        print("Table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")


def hash_password(password):
    """
    Hash a password using PBKDF2-HMAC-SHA256 with a randomly generated salt.
    The function returns the salt and the hashed password concatenated together, both hex-encoded.
    """
    salt = os.urandom(32)  # Generate a random salt
    key = hashlib.pbkdf2_hmac(
        'sha256',  # Hash function
        password.encode('utf-8'),  # Password converted to bytes
        salt,  # Salt for PBKDF2
        100000  # Number of iterations
    )
    return salt.hex() + key.hex()  # Return the salt and key concatenated and hex-encoded


def add_user(conn, user):
    """
    Adds a user to the 'users' table with a hashed password.
    User data should be provided as a tuple (name, email, age, plain_text_password).
    The password is hashed before storage for security.
    """
    sql = '''INSERT INTO users (name, email, age, password) VALUES (?, ?, ?, ?)'''
    hashed_password = hash_password(user[3])
    user_data = (user[0], user[1], user[2], hashed_password)
    try:
        cursor = conn.cursor()
        cursor.execute(sql, user_data)
        conn.commit()
        print("User added successfully.")
    except Error as e:
        print(f"Error inserting user data: {e}")


def authenticate_user(conn, username, provided_password):
    """
    Authenticate a user against stored credentials.
    If the provided username and password match the stored credentials, return True, otherwise False.
    """
    sql = "SELECT password FROM users WHERE name = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (username,))
        stored_password = cursor.fetchone()
        if stored_password and validate_password(stored_password[0], provided_password):
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False
    except Error as e:
        print(f"Error during authentication: {e}")
        return False


def validate_password(stored_password, provided_password):
    """
    Validate a provided password against a stored password.
    The stored password includes a salt part and a hash part. Both are hex-encoded.
    """
    salt = bytes.fromhex(stored_password[:64])
    stored_key = bytes.fromhex(stored_password[64:])
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt,
        100000
    )
    return new_key == stored_key


def main():
    """
    Main function to demonstrate the usage of functions above.
    It creates a database connection, sets up a table, and adds a user with hashed password.
    Then, it attempts to authenticate the user.
    """
    conn = create_connection()
    if conn:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER,
            password TEXT NOT NULL
        );"""
        create_table(conn, sql_create_table)
        add_user(conn, ('Alice', 'alice@example.com', 30, 'securepassword123'))
        authenticate_user(conn, 'Alice', 'securepassword123')
        conn.close()


if __name__ == "__main__":
    main()
