from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import base64

app = Flask(__name__)

# Configure the database (SQLite in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image_db.sqlite'
db = SQLAlchemy(app)

# Define the database model for storing images
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            # Read the image and convert it to base64
            image_data = image.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')

            # Get the image name from the form
            image_name = request.form['name']

            # Save the image name and base64 data in the database
            new_image = Image(name=image_name, data=image_base64)
            db.session.add(new_image)
            db.session.commit()
            return 'Image uploaded and saved in the database.'

    return render_template('upload.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)