from flask import Flask, request, Response
import os

app = Flask(__name)

@app.route('/img')
def img():
    # Get the value of the "file" parameter from the URL
    file_name = request.args.get('file')

    if file_name:
        # Define the path to the image directory
        image_directory = 'images/'

        # Construct the full path to the requested image file
        image_path = os.path.join(image_directory, file_name)

        # Check if the requested image file exists
        if os.path.exists(image_path):
            # Open and read the image file in binary mode
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
                return Response(image_data, content_type="image/jpeg")  # Adjust content type as needed
        else:
            return "Image not found", 404  # Return a 404 error if the file doesn't exist
    else:
        return "Missing 'file' parameter", 400  # Return a 400 error if 'file' parameter is missing

if __name__ == '__main__':
    app.run()