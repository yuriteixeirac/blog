from datetime import datetime

from flask import redirect, render_template, request, url_for
from flask_login import login_required, login_user, current_user, logout_user
from sqlalchemy import select
from werkzeug.security import check_password_hash

from app import app, db
from app.forms import LoginForm, PostagemForm
from app.models import Usuario
from app.models.postagem import Postagem


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        postagens = db.session.scalars(
            select(Postagem)
        ).all()[::-1]

        return render_template('index.html', postagens=postagens, usuario=current_user)

    postagem = Postagem(
        corpo=request.form.get('corpo'),
        autor=current_user
    )

    db.session.add(postagem)
    db.session.commit()

    return redirect(url_for('home'), )

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
   

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
