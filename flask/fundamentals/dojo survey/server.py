from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/')
def index():
    
    return render_template("index.html")
@app.route('/', methods=['POST'])
def get():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
    return redirect("/show")
        
@app.route('/show')
def show():
    return render_template("show.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return render_template('index.html')








if __name__ == '__main__':
    app.run()