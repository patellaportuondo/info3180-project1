from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField
from wtforms.validators import InputRequired ,Email
from flask_wtf.file import FileField , FileAllowed , FileRequired


class LoginForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired(message='First Name is required')])
    lastname = StringField('Lastname', validators=[InputRequired(message='Last Name is required')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired(message='Gender is required')])
    email = StringField('Email', validators=[InputRequired(message='Email is required'), Email(message="Only Emails")])
    location = StringField('Location', validators=[InputRequired(message='Location is required')])
    biography = TextAreaField('Biography', validators=[InputRequired(message='Location is required')])
    upload = FileField('Image', validators=[FileRequired('Please input a file'), FileAllowed(['jpg', 'png'], 'Images only!')])

