from flask import Flask, request, render_template
import os

app = Flask(__name)

# Create the 'uploads' directory if it doesn't exist
os.makedirs('uploads', exist_ok=True)

# Define a list of allowed file extensions (you can customize this)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

# Function to check if the file type is safe
def file_is_safe_type(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if file and file_is_safe_type(file.filename):
            file.save(os.path.join('uploads', file.filename))
            return "File uploaded successfully"
        else:
            return "Invalid file type. Only text, PDF, and Word documents are allowed."

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)