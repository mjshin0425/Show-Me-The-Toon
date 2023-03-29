from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup
# ============

url = 'https://comic.naver.com/webtoon'
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/toon')
def review():
    return render_template('toon.html')


# ==============

@app.route("/review", methods=["GET"])
def movie_get():
    return jsonify({'msg':'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)