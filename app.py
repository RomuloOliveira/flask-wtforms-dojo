#!/bin/env python

from project import app

import os

if __name__ == '__main__':
    port = int(os.environ['PORT'])
    app.run(port=port)
