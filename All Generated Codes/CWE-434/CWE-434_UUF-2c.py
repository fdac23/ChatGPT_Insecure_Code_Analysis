from flask import Flask, request, render_template
import base64

app = Flask(__name)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty part without a filename
        if file.filename == '':
            return "No selected file"

        # If the file is provided and has a filename, read and encode it using base64
        if file:
            image_data = file.read()
            encoded_image = base64.b64encode(image_data).decode()

            # Write the encoded image to a file (in this case, "encoded_image.txt")
            with open("encoded_image.txt", "w") as text_file:
                text_file.write(encoded_image)
            return "Image uploaded, encoded, and saved as encoded_image.txt"

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)