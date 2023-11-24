import subprocess

# Function to check if the email exists and unsubscribe it
def check_and_unsubscribe_email(email):
    # Check if the email exists in the database (replace with your logic)
    if email_exists_in_database(email):
        # Call the PHP script to unsubscribe the email
        php_script_path = 'unsubscribe.php'  # Replace with the path to your PHP script
        result = subprocess.call(['php', php_script_path, email])

        # Check the result returned by the PHP script
        if result == 0:
            return 1
    return 0

# Function to check if the email exists in the database (replace with your logic)
def email_exists_in_database(email):
    # Add your database query logic here to check if the email exists
    # Return True if it exists, otherwise return False
    # You should replace this with your actual database query
    return False  # Replace with your database query logic

# Example usage:
if __name__ == "__main__":
    email_to_check = "example@example.com"  # Replace with the email you want to check
    result = check_and_unsubscribe_email(email_to_check)

    if result == 1:
        print(f"The email '{email_to_check}' has been successfully unsubscribed.")
    else:
        print(f"The email '{email_to_check}' was not found in the database or failed to unsubscribe.")