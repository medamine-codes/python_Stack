from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', all_users=users)


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')


@app.route('/users/create', methods=['POST'])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect('/')


@app.route('/users/<int:user_id>')
def one_user(user_id):
    data = {
        'id': user_id
    }
    user = User.get_one(data)
    return render_template('one_user.html', user=user)


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_one(data)
    return redirect('/')