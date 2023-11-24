from flask import Flask, send_file
import os

app = Flask(__name__)

# Define the directory where image files are stored
IMAGE_DIR = 'images'

# Create a decorator for serving images
def serve_image(route):
    def decorator(func):
        def wrapper(filename):
            # Construct the full path to the image file
            file_path = os.path.join(IMAGE_DIR, filename)

            # Check if the file exists
            if os.path.exists(file_path):
                return send_file(file_path, mimetype='image/jpeg')  # Adjust the mimetype as needed
            else:
                return "File not found", 404

        app.add_url_rule(route, func.__name__, wrapper)
        return wrapper

    return decorator

@app.route('/')
def index():
    return "Hello, this is the index page."

@serve_image('/image/<filename>')
def image(filename):
    pass

if __name__ == '__main__':
    app.run(debug=True)