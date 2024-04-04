import sqlite3

def initialize_database():
    """
    Initializes the database for the CyberProtector project.
    This script creates a new SQLite database and sets up the required tables.
    """

    # Connect to SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('cyberprotector.db')
    
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Create table for login attempts
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        attempt_time TEXT NOT NULL,
        success INTEGER NOT NULL,
        ip_address TEXT NOT NULL
    );
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()


