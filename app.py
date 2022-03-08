from webbrowser import get, open_new
from threading import Timer
from flask import Flask, render_template, request, redirect, url_for
from main import Main

app = Flask(__name__)

choice = 0
choice_for_name = 0

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        global choice
        choice=int(request.form['options'])
        if choice in [1,4,5]:
            return render_template('options.html')
        else:
            return render_template('form.html',choice=choice,choice_for_name=choice_for_name)
    else:
        return render_template('index.html')

def open_browser():
      open_new('http://127.0.0.1:5000/')

@app.route('/options',methods=['POST','GET'])
def message():
    if request.method=='POST':
        global choice_for_name
        choice_for_name=int(request.form['choices'])
        return render_template('form.html',choice=choice,choice_for_name=choice_for_name)

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method=='POST':
        print(choice)
        print(choice_for_name)
        
        # Writing all the filepaths in a text file for now
        excel_filepath = request.form['excel_file']
        excel_filename = request.form['worksheet_name']
        column_name_of_contacts = request.form['contact_name']
        message = ""
        media_filepath = ""
        pdf_filepath = ""
        column_name_of_names_stored = ""

        if choice in [1,4,5]:
            message = request.form['message']
        if choice in [2,4]:
            media_filepath = request.form['attach_media']
        if choice in [3,5]:
            pdf_filepath = request.form['attach_pdf']
        if choice_for_name == 1:
            column_name_of_names_stored = request.form['name_name']
        
        # Writing in the text file
        f = open("details.txt","w+")
        f.write("\nmedia_filepath = "+media_filepath)
        f.write("\npdf_filepath = "+pdf_filepath)
        f.write("\nmessage = "+message)
        f.write("\nexcel_filepath = "+excel_filepath)
        f.write("\nexcel_filename = "+excel_filename)
        f.write("\ncolumn_name_of_contacts = "+column_name_of_contacts)
        f.write("\ncolumn_name_of_names_stored = "+column_name_of_names_stored)
        f.close()
        print(request.form)
        Main(choice,choice_for_name)

        return render_template('index.html')
    else:
        return render_template('form.html')

if __name__ == "__main__":
    Timer(1, open_browser).start();
    app.run(port=5000)
    app.run(debug=True)