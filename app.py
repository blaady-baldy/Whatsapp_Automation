from json.tool import main
from webbrowser import get
from flask import Flask, render_template, request, redirect, url_for
from main import Main
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
choice = 0

@app.route('/options',methods=['POST','GET'])
def message():
    if request.method=='POST':
        global choice
        choice=int(request.form['options'])
        print(choice)
        return render_template('form.html',choice=choice)

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method=='POST':
        print(request.form['attach_media'])
        file1 = open("details.txt",'a')

        Main(choice)

        return render_template('index.html')
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)