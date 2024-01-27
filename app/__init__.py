from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import routes