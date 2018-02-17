from flask import Flask
from pymongo import MongoClient
from flask import request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin_authentication')
def admin_authentication():
    return render_template('admin_authentication.html')


@app.route('/user_login')
def user_login():
    return render_template('user_login.html')


@app.route('/admin_product')
def admin_product():
    return render_template('admin_product.html')


@app.route('/add_new_product')
def add_new_product():
    return render_template('add_new_product.html')


@app.route('/update_product')
def update_product():
    return render_template('update_product.html')


@app.route('/remove_product')
def remove_product():
    return render_template('remove_product.html')


@app.route('/add_user')
def add_user():
    return render_template('add_user.html')


@app.route('/remove_user')
def remove_user():
    return render_template('remove_user.html')


@app.route('/generateScan')
def generateScan():
    return render_template('generate_scan.html')


@app.route('/generate')
def generate():
    return render_template('generate.html')


@app.route('/scan')
def scan():
    return render_template('scan.html')


if __name__ == '__main__':
    app.run(debug=True)


"""


    client = MongoClient('localhost', 27017)
    mydatabase = client.pos369
    scanner = mydatabase.posScanner

    record = {
        'title': 'abc',
        'description': 'xyz',
        'tags': ['mongodb', 'database', 'NoSQL'],
        'viewers': 369
    }
    rec = mydatabase.posScanner.insert(record)

"""