from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class Usuario(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(50), unique=True, nullable=False)
    senha: so.Mapped[str] = so.mapped_column(sa.String(255), nullable=True)
    postagens: so.Mapped[List['Postagem']] = so.relationship(back_populates='autor')
    artigos: so.Mapped[List['Artigo']] = so.relationship(back_populates='autor')

