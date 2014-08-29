all: clean build

clean:
	# Remove compiled, temp files, etc.
	find -name '*.pyc' -print0 | xargs --no-run-if-empty -0 rm -v

lint:
	# Checks code style
	flake8 --exclude='build/*,venv/*,./project/worker/example_data.py' --max-line-length=120 --ignore=E302,F403 .

configure:
	# Configures environment
	./bin/configure.sh

build: clean lint configure
	# Install dependencies, compile, link and build
	pip install -r requirements.txt

tests: export ENV=test
tests: build
	# Start tests

.PHONY: tests build
