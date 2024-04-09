import sqlite3

def create_table(db_path):
    """
    Create a 'login_attempts' table in the specified SQLite database to track user login attempts.

    Parameters:
    db_path (str): The file path to the SQLite database file.
    """
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Execute SQL command to create the table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        attempt_time TEXT NOT NULL,
        success INTEGER NOT NULL,
        ip_address TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

# Example usage
# db_path = 'path_to_your_database_file.db'
# create_table(db_path)
