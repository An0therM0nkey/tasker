from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


from src.tasks.api import api as tasks_api
tasks_api.init_app(app)
