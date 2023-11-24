import sqlite3

# Function to check if a username exists in the database
def username_exists(username):
    # Connect to the database (replace 'database.db' with your database file)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute a query to check if the username exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return True if the username exists, False otherwise
    return result is not None

# Example usage:
if __name__ == "__main__":
    # Replace 'test_user' with the username you want to check
    username_to_check = "test_user"
    exists = username_exists(username_to_check)

    if exists:
        print(f"The username '{username_to_check}' exists in the database.")
    else:
        print(f"The username '{username_to_check}' does not exist in the database.")