from getpass import getpass

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from app import app, db
from app.models import Usuario


if __name__ == '__main__':
    username = input("Username: ")
    if not len(username) <= 50:
        raise ValueError('Nome de usuário muito longo.')

    senha = getpass()
    if not len(senha) <= 8:
        raise ValueError('Senha de usuário muito curta.')

    with app.app_context():
        usuario = Usuario(
            username=username,
            senha=generate_password_hash(senha)
        )
        db.session.add(usuario)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print('Erro de integridade. O nome de usuário provavelmente já está em uso.')

