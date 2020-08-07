from flask import Flask
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object('config')

# db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

from project import views, models
