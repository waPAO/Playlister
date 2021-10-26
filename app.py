from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''Return Homepage'''
    return render_template('home.html', msg='Flask is Cool!')


if __name__ == '__main__':
    app.run(debug=True)