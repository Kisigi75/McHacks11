from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.String(20))
    weight_group = db.Column(db.Integer)
    weight_user = db.Column(db.Integer)
    complete = db.Column(db.Boolean, default=False)

@app.route('/')
def hello_world():
    tasks = Tasks.query.all()
    return render_template('base.html', tasks=tasks)

@app.route('/user_tasks')
def user_tasks():
    task_list = Tasks.query.all()
    return render_template("add_tasks.html", task_list=task_list)


@app.route('/add_task', methods = ["POST"])
def add_task():
    title = request.form.get("title")
    user_id = request.form.get("user_id")
    weight_user = request.form.get("weight", type=int)
    new_task = Tasks(title=title, weight_user=weight_user, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/user_tasks')


'''@app.route("/update/<int:task_id>", methods=["GET","POST"])
def update_task(task_id):
    task = Tasks.query.get_or_404(task_id)
    if request.method == 'POST':
        task.complete = True
        db.session.commit()
        return redirect('user_tasks')
    return render_template('')
'''

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
