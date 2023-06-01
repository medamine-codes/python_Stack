from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.party import Party
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users/create',methods=['POST'])
def create_user():
    print(request.form)
    if(User.validate(request.form)):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            **request.form,'password':pw_hash
        }
        user_id = User.create_user(data)
        session['user_id'] = user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    parties = Party.get_all()
    return render_template("dashboard.html", user = user,parties=parties)
@app.route('/my_parties')
def my_parties():
    if not 'user_id' in session:
        return redirect('/')
    parties = Party.get_user_parties({'user_id':session['user_id']})
    user = User.get_by_id({'id':session['user_id']})
    return render_template("my_parties.html",parties=parties ,user=user)
@app.route('/users/login', methods=['POST'])
def login():
    user_from_db = User.get_by_email({'email':request.form['email']})
    if(user_from_db):
        # check password
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        # if we get False after checking the password
            flash("Invalid Password","log")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashboard')
    flash("Invalid Email","log")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')