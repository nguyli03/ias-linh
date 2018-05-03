from flask import Flask, render_template, request, Response, jsonify
import requests
import json
import hashlib
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def check():
    pass
if __name__=='__main__':
    app.run(debug=True)
