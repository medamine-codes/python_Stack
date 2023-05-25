from flask import Flask, render_template ,redirect , request

from user import User
app=Flask(__name__)
@app.route("/")
def index():
    users=User.get_all()
    print(users)
    return render_template('index.html',all_users=users)

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route("/users/create", methods=["POST"])
def create_user():
    print(request.form)
    User.create_user(request.form)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)