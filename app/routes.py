from flask import redirect, render_template, url_for, request, session
from app import app
import string
import random

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    if request.method == "POST":
        creator_name = request.form["creator_name"]
        session["creator_name"] = creator_name
        # generate random code
        random_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        session["random_code"] = random_code

        return redirect(url_for("dashboard"))
    
    return render_template('create_group.html')

@app.route('/join_group', methods=['GET', 'POST'])
def join_group():
    if request.method == "POST":
        user_name = request.form["user_name"]
        entered_code = request.form["entered_code"]
        session["user_name"] = user_name
        session["entered_code"] = entered_code
        return redirect(url_for('dashboard'))

    return render_template('join_group.html')


@app.route('/dashboard')
def dashboard():
    if "creator_name" in session:
        creator_name = session["creator_name"]
        random_code = session["random_code"]

    return render_template("dashboard.html", creator_name=creator_name, random_code=random_code)