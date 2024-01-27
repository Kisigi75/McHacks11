from flask import redirect, render_template, url_for, request, session
from app import app
import string
import random

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

