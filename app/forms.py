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


class ArtigoForm(FlaskForm):
    titulo = wtforms.StringField(validators=[
        wtforms.validators.DataRequired(),
        wtforms.validators.Length(min=1, max=324)
    ])
    corpo = wtforms.TextAreaField(
        validators=[wtforms.validators.DataRequired()]
    )

