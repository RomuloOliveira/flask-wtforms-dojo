#!/bin/bash

set -e

. ./bin/lint.sh
. ./bin/configure.sh

find -name '*.pyc' -print0 | xargs --no-run-if-empty -0 rm -v

pip install -r requirements.txt