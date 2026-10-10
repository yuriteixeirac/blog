from flask_wtf import FlaskForm
import wtforms

class LoginForm(FlaskForm):
    username = wtforms.StringField(validators=[
        wtforms.validators.DataRequired(), 
        wtforms.validators.Length(max=50)
    ])
    senha = wtforms.PasswordField(validators=[
        wtforms.validators.DataRequired(), 
        wtforms.validators.Length(min=8)
    ])


class PostagemForm(FlaskForm):
    corpo = wtforms.StringField(validators=[wtforms.validators.DataRequired(), wtforms.validators.Length(1, 324)])

