from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
UPLOAD_FOLDER = './app/static/uploads'
app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uvobyvmjzdcail:f436aea1af4e83541523bcb31aed27bae0f007b6893b794110e1a5cccf8a7b5e@ec2-54-204-44-140.compute-1.amazonaws.com:5432/d3nbtcjglkvj5e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
filefolder = app.config['UPLOAD_FOLDER']
app.debug= True
from app import views
