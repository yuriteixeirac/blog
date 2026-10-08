from flask import redirect, render_template, url_for
from flask_login import login_user
from sqlalchemy import select
from werkzeug.security import check_password_hash

from app import app, db
from app.forms import LoginForm
from app.models import Usuario


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    usuario = db.session.scalar(
        select(Usuario).where(
            Usuario.username == form.username.data
        )        
    )
    
    if not usuario:
        return render_template('login.html', form=form)

    if not check_password_hash(usuario.senha, form.senha.data):
        return render_template('login.html', form=form)

    login_user(usuario)

    return redirect(url_for('home'))
   
