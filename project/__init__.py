#!/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

import os

app = Flask(__name__)

if 'DEVEL' in os.environ and os.environ['DEVEL']:
    app.debug = True

if 'TEST' in os.environ and os.environ['TEST']:
    app.test = True
