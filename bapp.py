#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

import os
import sys
from flask import send_file
from flask import Flask, session, render_template, request, redirect, url_for, flash, jsonify
from flask_bcrypt import Bcrypt
from flask_session import Session


from werkzeug.utils import secure_filename
from autocorrect import Speller
import docx2txt
import requests
import csv
import re
import time
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import matplotlib

app = Flask(__name__)

my_bot = ChatBot("Candice")
#bot.set_trainer(ListTrainer)
#bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train("chatterbot.corpus.english")

listy=ListTrainer(my_bot)
small=['hi','hello']
for i in small:
	listy.train(i)

@app.route("/")
def home():    
    return render_template("home.html")
    #return redirect(url_for('query'))

@app.route('/query', methods=['POST'])
def query():
	print()
	flash('Hey Whatshapp',"error")
	if request.method == 'POST':
            msg=request.form.get("msg").lower()
            ss=spell(msg)
            if "hey" in ss:
                flash("Gazala", "error")
                

    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
