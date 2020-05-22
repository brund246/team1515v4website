from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/leaders')
def leaders():
    return render_template('leaders.html')


@app.route('/mentors')
def mentors():
    return render_template('mentors.html')


@app.route('/awards')
def awards():
    return render_template('awards.html')


@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')


@app.route('/divisions')
def divisions():
    return render_template('divisions.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=False)
