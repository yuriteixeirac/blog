import sqlalchemy as sa
import sqlalchemy.orm as so

from datetime import datetime

from app import db


class Postagem(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key=True)
    corpo: so.Mapped[str] = so.mapped_column(sa.String(324), nullable=False)
    autor: so.Mapped['Usuario'] = so.relationship(back_populates='postagens')
    autor_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('usuario.id'))
    criado_em: so.Mapped[datetime] = so.mapped_column(sa.DateTime(), default=datetime.now)
    atualizado_em: so.Mapped[datetime] = so.mapped_column(sa.DateTime(), default=datetime.now, onupdate=datetime.now)

