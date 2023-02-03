import os
from flask import Flask, render_template

app = Flask(__name__)

        
@app.route("/")
def hello_world():
    return "<html><body><p>Hello, World!</p></body></html>"

@app.route("/dynamic/raspberry.html")
def capture():
    files = os.listdir('/home/yann/stage-yann/static/captures')
    return render_template("raspberry.html", files = files)





if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")