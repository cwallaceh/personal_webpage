from datetime import datetime

from flask import render_template #, flash, redirect, request, Response, g, url_for
# from flask_login import login_required, login_user, logout_user, current_user

from project import app #, login_manager

# from .models import User


# @app.route('/admin', methods=['GET', 'POST'])
# @login_required
# def admin():
#     pass


@app.route('/')
def index():
    # user = g.user
    return render_template("index.html",
                           title='Home',
                           # user=user,
                           year=datetime.now().year)


@app.route('/map')
def map():
    return render_template("map.html",
                           title='Map',
                           year=datetime.now().year)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')

#     username = request.form['username']
#     password = request.form['password']
#     remember_me = False
#     if 'remember_me' in request.form:
#         remember_me = True
#     registered_user = User.query.filter_by(username=username,
#                                            password=password).first()
#     if registered_user is None:
#         flash('Username or Password is invalid', 'error')
#         return redirect(url_for('login'))
#     login_user(registered_user, remember=remember_me)
#     flash('Logged in successfully')
#     return redirect(request.args.get('next') or url_for('index'))


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


# @app.errorhandler(401)
# def page_not_found(e):
#     return Response('<p>Login failed</p>')


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))


# @app.before_request
# def before_request():
#     g.user = current_user
