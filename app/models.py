from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app import login

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    deadline = db.Column(db.DateTime, nullable=True)
    weight_user = db.Column(db.Integer, nullable=True)
    complete = db.Column(db.Boolean, default=False)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
