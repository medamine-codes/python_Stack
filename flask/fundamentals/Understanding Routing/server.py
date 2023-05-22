from flask import Flask
app =Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return "hi " + name

@app.route('/repeat/<int:times>/<word>')
def repeat(times,word):
    return (word+"<br>")*times










if __name__=="__main__":
    app.run(debug=True)