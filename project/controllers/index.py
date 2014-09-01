#!/bin/env python

from project import app

from flask import request, render_template
from project.forms.index import IndexForm

@app.route('/', methods=['POST', 'GET'])
def index():
    form = IndexForm(request.form)

    if form.validate_on_submit():
        return '', 200

    return render_template('index.html', form=form, errors=form.errors)
