from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data.encode('utf-8')  # Encode the password as bytes
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # In a real application, you would typically store the username and hashed password in a database

        flash('Registration successful!', 'success')
        return redirect(url_for('register'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)