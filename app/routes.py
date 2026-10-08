from alembic.autogenerate import render
from flask import request, render_template
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from app.forms import LoginForm
from app.models import Usuario


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    
    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    usuario = db.session.execute(
        select(Usuario).where(
            Usuario.username == form.username.data
        )        
    )

    if not check_password_hash(usuario.senha, form.senha.data):
        return render_template('login.html', form=form)

    # usar função de login...
    

