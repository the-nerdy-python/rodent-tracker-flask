import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.rodentdb


@app.route('/')
def rodentapp():

    _items = db.rodentdb.find()
    items = [item for item in _items]

    return render_template('rodent.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.rodentdb.insert_one(item_doc)

    return redirect(url_for('rodentapp'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)