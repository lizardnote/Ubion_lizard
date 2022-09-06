from tkinter.messagebox import RETRY
from flask import flask

#__NAME__ : 파일의 이름
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
@app.route("/second")
def second():
    return "second Page"

app.run()