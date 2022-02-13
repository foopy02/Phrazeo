import json
import requests
import os
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

ROOT_OF_DATABASE = f'{os.path.dirname(__file__)}/database.json'
database = json.load(open(ROOT_OF_DATABASE,'r', encoding='utf-8'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/find_idioms', methods=["POST"])
def find_idioms():
    if request.method == "POST":
        word = request.form['word'].lower()
        related_idioms = [idiom for idiom in database 
                                    for word_idioms in idiom['text'].lower().replace(',',' ').replace('.',' ').split(' ') 
                                        if word == word_idioms]
        suggested_idioms = [idiom for idiom in database if word in idiom['text'].lower().replace(',',' ').replace('.',' ') and idiom not in related_idioms]
        
    return render_template("index.html", related_idioms=related_idioms, suggested_idioms=suggested_idioms, searched_word=word)



app.run(debug=True)