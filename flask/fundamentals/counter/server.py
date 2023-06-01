from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if "visits" in session:
            session["visits"] += 1
        else:
            session["visits"] = 1

    if request.method == "POST":
        action = request.form["action"]
        if action == "increment":
            increment = int(request.form["increment"])
            session["count"] += increment

        elif action == "reset":
            session["count"] = 1
    else:
        if "count" not in session:
            session["count"] = 1

    return render_template("index.html", count=session["count"], visits=session["visits"])
    
@app.route("/destroy_session")

def clear():
    session.clear()
    return redirect("/")



@app.route('/show')

def show():
    count1=session["count"]

    return render_template("show.html",count1=count1)







if __name__ == "__main__":
    app.run(debug=True)