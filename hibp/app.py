from flask import Flask, render_template, request, Response, jsonify
import requests
import json
import hashlib
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkEmail', methods = ['POST'])
def checkEmail():
    email = request.form['email']
    res = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/'+email)
    print(res.json())
    return render_template('resultEmail.html', res = res.json())

@app.route('/checkPassword', methods = ['POST'])
def checkPassword():
    password = request.form['password'].encode('utf-8')
    hashP = hashlib.sha1(password).hexdigest()
    res = requests.get('https://api.pwnedpasswords.com/range/'+hashP[:5])
    if res.text != '':
        pairs = res.text.split('\r\n')
        for item in pairs:
            [hashPR,time] = item.split(':')
            if hashPR == hashP[5:].upper():
                print(item)
                return render_template('resultPassword.html',res = time)
    return render_template('resultPassword.html',res='')

if __name__=='__main__':
    app.run(debug=True)
