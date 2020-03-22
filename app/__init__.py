from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from colour import Color

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def colorgradient(value):
    red = Color("#008000")
    colors = list(red.range_to(Color("#ff0000"), 101))
    pos = int(value)
    return colors[pos]


app.jinja_env.globals.update(colorgradient=colorgradient)

from app import routes, models
