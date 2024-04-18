# Import the sqlite3 library to work with SQLite databases
import sqlite3
# Import the Error class from the sqlite3 module for error handling
from sqlite3 import Error

# Import the re library for regular expression operations
import re
# Import defaultdict for using dictionaries with default values
from collections import defaultdict
# Import datetime and timedelta for handling date and time calculations
from datetime import datetime, timedelta

def create_connection(db_file):
    """
    Establish a connection to a SQLite database.
    Creates the database file if it does not exist.
    """
    conn = None  # Initialize the connection variable to None
    try:
        # Attempt to connect to the SQLite database specified by db_file
        conn = sqlite3.connect(db_file)
        return conn  # Return the connection object if successful
    except Error as e:
        print(e)  # Print any error that occurs during the connection attempt
    return conn  # Return None if connection was unsuccessful

def create_table(conn, create_table_sql):
    """
    Execute a SQL statement to create a table according to the provided SQL command.
    """
    try:
        c = conn.cursor()  # Create a cursor object using the connection
        c.execute(create_table_sql)  # Execute the SQL command to create a table
    except Error as e:
        print(e)  # Print any error that occurs during table creation

def email_exists(conn, email):
    """
    Check if an email already exists in the database to prevent duplicates.
    """
    cur = conn.cursor()  # Create a cursor object
    # Execute SQL to check if an email exists in the 'users' table
    cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE email=? LIMIT 1)", (email,))
    return cur.fetchone()[0]  # Return True if exists (1), False otherwise (0)

def insert_user(conn, user):
    """
    Insert a new user into the database if the email does not already exist.
    """
    if not email_exists(conn, user[2]):  # Check if the user's email already exists
        sql = '''INSERT INTO users(name, age, email) VALUES(?,?,?)'''  # SQL command for inserting a new user
        cur = conn.cursor()
        cur.execute(sql, user)  # Execute the insertion command
        conn.commit()  # Commit the changes to the database
    else:
        print(f"Error: Email {user[2]} already exists.")  # Print an error if the email exists

def update_user(conn, user_id, new_email):
    """
    Update a user's email if it does not already exist and the user is found.
    """
    if not email_exists(conn, new_email):  # Check if the new email already exists
        sql = '''UPDATE users SET email = ? WHERE id = ?'''  # SQL command to update the user's email
        cur = conn.cursor()
        cur.execute(sql, (new_email, user_id))  # Execute the update command
        conn.commit()  # Commit the changes to the database
        if cur.rowcount == 0:
            print(f"No user found with ID {user_id}")  # Print an error if no user is found
        else:
            print(f"User ID {user_id} updated with new email {new_email}")  # Confirm the update
    else:
        print(f"Error: Email {new_email} already exists.")  # Print an error if the email exists

# Example usage of the functions within the module, establishing database connection, creating tables, and manipulating user data.
