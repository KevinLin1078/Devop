import datetime
import os

from flask import Flask, render_template, redirect, url_for, jsonify
from forms import ItemForm
from models import Items
from database import db_session

app = Flask(__name__)
app.secret_key = 'super_duper_secret'

@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route("/success", methods=["GET"])
def success():
    results = []
    qry = db_session.query(Items)
    for i in qry:
        result ={
                    'name': i.name,
                    'quantity': i.quantity,
                    'description': i.description,
                    'date_added': i.date_added
                }
        results.append(result)
    
    return jsonify({"results" : results})
    # results = qry.all()
    # return str(results)
  

if __name__ == '__main__':
    app.run(host='0.0.0.0')
