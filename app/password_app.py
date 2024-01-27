from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/password')
def welcome():
    return render_template('welcome.html')

@app.route('/get_password', methods=['POST', 'GET'])
def get_password():
    if request.method == 'POST':
        password = request.form['password']
        return render_template('display_password.html', password=password)
    return render_template('display_password.html')

if __name__ == '__main__':
    app.run(debug=True)

