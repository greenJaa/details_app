import os,sys
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
#from libs.ConnectionForm import ConnectionForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SECRET___--_KEY'] = '!!5S0m#wh$tVERYL0nGQWERTYpa$$W0d'
db = SQLAlchemy(app)

@app.route('/',methods=['GET', 'POST'])
def index():
#    form = ConnectionForm()
    if request.method == 'POST':
        contact_info = {'email': request.form.get('Email'), 'name': request.form.get('Name')}
        return redirect('/')
    #return render_template('index.html', form=form)
    return render_template('index.html')