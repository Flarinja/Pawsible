from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/comingsoon')
def comingsoon():
    return render_template('comingsoon.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)