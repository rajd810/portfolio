#https://www.geeksforgeeks.org/single-page-portfolio-using-flask/
from flask import Flask, render_template, request,  url_for, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator


app = Flask(__name__)
app.secret_key = "abcd1234abcd1234"

#Declarig form input
class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
    submit = SubmitField(label="Send")

#Declaring the index page
@app.route("/", methods=["GET", "POST"])
def index():
    cform=contactForm()
    if cform.validate_on_submit():
        print(f"Name:{cform.name.data}, E-mail:{cform.email.data}, message:{cform.message.data}")
    return render_template("index.html", form=cform)
    
@app.route("/success", methods=["GET", "POST"])
def sent():
    return render_template("contact_success.html",)

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)