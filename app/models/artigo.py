from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class Artigo(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key=True)
    titulo: so.Mapped[str] = so.mapped_column(sa.String(324), nullable=False)
    corpo: so.Mapped[str] = so.mapped_column(sa.Text(), nullable=False)
    autor: so.Mapped['Usuario'] = so.relationship(back_populates='artigos')
    autor_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('usuario.id'))
    criado_em: so.Mapped[datetime] = so.mapped_column(sa.DateTime(), default=datetime.now)
    atualizado_em: so.Mapped[datetime] = so.mapped_column(sa.DateTime(), default=datetime.now, onupdate=datetime.now)
     
