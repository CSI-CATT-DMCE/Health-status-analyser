from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Doctor
#CAN USE ABOVE IMPORTS OR OTHER IF PARTICIPANTS WANT 

class RegistrationForm(FlaskForm):
    #FULL NAME,EMAIL,TELEPHONE,PASSWORD
    

class LoginForm(FlaskForm):
    #LOGIN WITH EMAIL,PASSWORD
   

class DocRegistrationForm(FlaskForm):
    #FULL NAME,EMAIL,TELEPHONE,PASSWORD
    


class DocLoginForm(FlaskForm):
    #LOGIN WITH EMAIL,PASSWORD
    


    


    

    
