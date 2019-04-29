from flask_wtf import FlaskForm
from wtforms import StringField,TextField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

