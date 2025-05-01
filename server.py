from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/work.html')
def about():
    return render_template('work.html')

@app.route('/contact.html')
def about():
    return render_template('contact.html')