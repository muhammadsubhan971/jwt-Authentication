from flask import Flask, render_template, redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "this is main page"

@app.route('/user')
def user():
    return 'this is user page'

from user import *
# import user_control
