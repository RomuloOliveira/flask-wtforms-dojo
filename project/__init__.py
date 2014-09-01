#!/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

import os

app = Flask(__name__)

if 'DEVEL' in os.environ and os.environ['DEVEL']:
    app.debug = True

if 'TEST' in os.environ and os.environ['TEST']:
    app.test = True

app.config['CSRF_ENABLED'] = False
app.config['WTF_CSRF_ENABLED'] = False

from project.controllers import *
