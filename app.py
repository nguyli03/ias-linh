from flask import Flask, render_template, request, Response, jsonify
import requests
import json
import hashlib
import base64
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, create_engine, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import os
import random

app = Flask(__name__)
postgresql_uri=os.environ['DATABASE_URL']
engine=create_engine(postgresql_uri)

Session = sessionmaker(bind=engine)
db = Session()

@app.route('/')
def index():
    db.execute("""CREATE table if not exists data(\
                            username text primary key,\
                            password text not null);""")
    db.commit()
    res = db.execute("""SELECT * from data;""")
    res = res.fetchall()
    if len(res) == 0:
        EX_STRING = """INSERT INTO data\
                (username, password)\
                VALUES ('%s', '%s');"""
        for i in range(0,10):
            db.execute(EX_STRING%('username'+str(i),str(random.randint(0,1000))))
            db.commit()

    return render_template('index.html')

@app.route('/check', methods = ["POST"])
def check():
    username = request.form['username']
    statement = "SELECT * from data where username = "+username
    print(statement)
    res = db.execute(statement)
    res = res.fetchall()
    print(res)
    return render_template('check.html', result = res)

if __name__=='__main__':
    app.run(debug=True)
