#!/bin/env python

from project import app

@app.route('/')
def index():
    return 'Hello, Flask', 200
