from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '57b9fc9bf0ebcb5de99a9c99d3423355'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
app.app_context().push()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes
