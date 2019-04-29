from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class PostForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    text = TextAreaField('Text',validators=[Required()])
    submit = SubmitField('Submit',validators=[Required()])

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')