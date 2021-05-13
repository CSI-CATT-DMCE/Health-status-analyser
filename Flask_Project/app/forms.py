from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Doctor

class RegistrationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    tel = StringField('Phone Number', validators=[DataRequired(),Length(min=10,max=10)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken. Please choose a different email')

    def validate_tel(self, tel):
        user = User.query.filter_by(tel=tel.data).first()
        if user:
            raise ValidationError('Phone number already taken. Please choose a different phone number')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DocRegistrationForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    tel = StringField('Phone Number', validators=[DataRequired(),Length(min=10,max=10)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])


    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        doctor = Doctor.query.filter_by(email=email.data).first()
        if doctor:
            raise ValidationError('Email already taken. Please choose a different email')

    def validate_tel(self, tel):
        doctor = Doctor.query.filter_by(tel=tel.data).first()
        if doctor:
            raise ValidationError('Phone number already taken. Please choose a different phone number')


class DocLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


    


    

    
