from flask import abort, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, login_user, current_user, logout_user
from sqlalchemy import select
from werkzeug.security import check_password_hash

from app import app, db
from app.forms import LoginForm
from app.models import Usuario
from app.models.artigo import Artigo
from app.models.postagem import Postagem


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', usuario=current_user)


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


@app.route('/artigos')
def artigos():
    artigos = db.session.scalars(
        select(Artigo)        
    ).all()
        
    return render_template('artigos.html', artigos=artigos, usuario=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/balbuceios', methods=['POST'])
@login_required
def post_balbuceio():
    corpo = request.form.get('corpo')

    if not 1 < len(corpo) < 324:
        abort(400)

    postagem = Postagem(
        corpo=corpo,
        autor=current_user
    )

    db.session.add(postagem)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/balbuceios')
def get_balbuceios():
    balbuceios = db.session.scalars(
        select(Postagem)
    ).all()[::-1]

    return jsonify([balbuceio.to_dict() for balbuceio in balbuceios]), 200


@app.route('/artigo/<id>')
def artigo_detail(id: int):
    artigo = db.session.scalar(
        select(Artigo).where(Artigo.id == id)
    )
    return render_template('artigo-detail.html', usuario=current_user, artigo=artigo)

