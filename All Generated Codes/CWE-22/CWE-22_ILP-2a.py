from flask import Flask, request, send_file

app = Flask(__name)

# Define a decorator for the /img URL
@app.route('/img/<name>')
def img(name):
    # Create the path to the image file
    file_path = f'images/{name}'

    try:
        # Open the image file and send it as a response
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True)
