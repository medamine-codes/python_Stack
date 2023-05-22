from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/play')                           
def hello_world():
    return render_template('index.html')

@app.route('/play/<int:x>/<string:color>')                           
def display(x,color):
    return render_template('index.html',x=x,color=color)












if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)


