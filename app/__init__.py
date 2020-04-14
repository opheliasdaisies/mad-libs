from flask import Flask, session
from config import Config
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

from app import routes
