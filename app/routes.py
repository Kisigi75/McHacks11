from flask import render_template, request
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():
    if request.method == "POST":
        creator_name = request.form["creator_name"]
        return creator_name
    return render_template('create_group.html')