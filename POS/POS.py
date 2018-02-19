from flask import Flask
import sys
from pymongo import MongoClient
from flask import request, redirect, render_template

app = Flask(__name__)


client = MongoClient('localhost', 27017)
mydatabase = client.pos369


@app.route('/home')
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
"""
    if request.method == 'POST':
        barcodetp = request.form['barcode']
        productIDtp = request.form['productID']
        productNametp = request.form['productName']
        pricetp = request.form['price']
        record = {
            'barcode': barcodetp,
            'productID': productIDtp,
            'productName': productNametp,
            'price': pricetp
        }
        mydatabase.posScanner.insert(record)
"""
   

@app.route('/entry', methods=['GET', 'POST'])
def entry_page():
    if request.method == 'POST':
        barcodetp = request.form['barcode']
        productIDtp = request.form['productID']
        productNametp = request.form['productName']
        pricetp = request.form['price']
        record = {
            'barcode': barcodetp,
            'productID': productIDtp,
            'productName': productNametp,
            'price': pricetp
        }
        mydatabase.posScanner.insert(record)
        return "Success"
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

"""

flag = 0
    if flag == 0:
        flag = 1
        client = MongoClient('localhost', 27017)
        mydatabase = client.pos369
    #    scanner = mydatabase.posScanner
        record1 = {
            'title': 'abc',
            'description': 'xyz',
            'tags': ['mongodb', 'database', 'NoSQL'],
            'viewers': 369
        }
        rec = mydatabase.posScanner.insert(record1)
        rec1 = mydatabase.posScanner369.insert(record1)

"""