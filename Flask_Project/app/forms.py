from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Doctor
#CAN USE ABOVE IMPORTS OR OTHER IF PARTICIPANTS WANT 

class RegistrationForm(FlaskForm):
    #You can change the code below
    print("FULL NAME,EMAIL,TELEPHONE,PASSWORD")
    print("Take above parameters while registering a user")
    

class LoginForm(FlaskForm):
    #You can change the code below
    print("LOGIN WITH EMAIL,PASSWORD")
    print("Take above parameters while logging in a user")
   

class DocRegistrationForm(FlaskForm):
    #You can change the code below
    print("FULL NAME,EMAIL,TELEPHONE,PASSWORD")
    print("Take above parameters while registering a doctor")
    


class DocLoginForm(FlaskForm):
    #You can change the code below
    print("LOGIN WITH EMAIL,PASSWORD") 
    print("Take above parameters while logging in a doctor")
   
    


    


    

    
