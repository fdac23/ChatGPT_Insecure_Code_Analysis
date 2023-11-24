import os
from flask import Flask, request, render_template, send_file
import mysql.connector

app = Flask(__name)

# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = db.cursor()

# Create an 'uploads' folder to store uploaded PDFs
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return "No file part"

    pdf = request.files['pdf']
    
    if pdf.filename == '':
        return "No selected file"

    if pdf:
        # Save the PDF to the 'uploads' folder
        pdf.save(os.path.join(UPLOAD_FOLDER, pdf.filename))

        # Save the file path in the MySQL database
        cursor.execute("INSERT INTO pdf_files (filepath) VALUES (%s)", (os.path.join(UPLOAD_FOLDER, pdf.filename),))
        db.commit()

        return "PDF file uploaded successfully"

@app.route('/download/<pdf_id>')
def download_pdf(pdf_id):
    # Retrieve the file path from the MySQL database based on pdf_id
    cursor.execute("SELECT filepath FROM pdf_files WHERE id = %s", (pdf_id,))
    result = cursor.fetchone()

    if result:
        filepath = result[0]
        return send_file(filepath, as_attachment=True)

    return "PDF file not found"

if __name__ == '__main__':
    app.run(debug=True)
