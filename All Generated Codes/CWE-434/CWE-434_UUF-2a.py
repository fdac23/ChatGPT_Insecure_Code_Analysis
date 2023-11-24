import mysql.connector
from mysql.connector import Error
from tkinter import filedialog
import tkinter as tk
from PIL import Image

# Create a MySQL database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to insert an image into the database
def insert_image(connection, image_path):
    try:
        with connection.cursor() as cursor:
            # Read the image file as binary data
            with open(image_path, 'rb') as file:
                image_data = file.read()

            # Insert the image data into the database
            query = "INSERT INTO images (image_data) VALUES (%s)"
            cursor.execute(query, (image_data,))
            connection.commit()
            print("Image inserted into the database")
    except Error as e:
        print(f"Error: {e}")

# Function to select and open an image file using a file dialog
def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an image file")
    return file_path

def main():
    connection = create_connection()
    if connection:
        image_path = select_image_file()
        if image_path:
            insert_image(connection, image_path)
        connection.close()

if __name__ == "__main__":
    main()
