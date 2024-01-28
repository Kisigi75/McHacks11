from flask import redirect, render_template, url_for, request, session, flash
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app import db
from .forms import LoginForm, CreateAccountForm
from app.models import User, Tasks

import sqlalchemy as sa
import string
import random
from datetime import datetime

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('dashboard'))

    return render_template('login.html', title="Login", form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/create_account', methods=('GET', 'POST'))
def create_account():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = CreateAccountForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!')

        return redirect(url_for('login'))

    return render_template('create_account.html', title='Create Account', form=form)

@login_required
@app.route('/dashboard')
def dashboard():
    tasks = Tasks.query.all()
    return render_template('dashboard.html', title="Dashboard", tasks=tasks)

@app.route('/add_task', methods = ["POST"])
def add_task():
    title = request.form.get("title")
    deadline_str = request.form.get("deadline")
    deadline = datetime.strptime(deadline_str,'%Y-%m-%d') if deadline_str else None
    weight_user = request.form.get("weight", type=int)
    new_task = Tasks(title=title, weight_user=weight_user, deadline=deadline,complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:task_id>")
def update(task_id):
    task = Tasks.query.filter_by(id=task_id).first()
    if task:
        task.complete = not task.complete
        db.session.commit()
    return redirect('/')