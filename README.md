# FlaskZipLookupApiExample
An example web service API implemented in Python using Flask framework.
```bash
# clone this repo to local
git clone git@github.com:DrOzturk/FlaskZipLookupApiExample.git
# create virtual environment with dependencies defined in Pipenv file
pipenv install
# start shell in that virtual environment
pipenv shell
# start this zip lookup service 
python3 -m zips.service
```

In postman or browser go to:
http://127.0.0.1:5000/?zip=30009
or
http://0.0.0.0:5000/?zip=30009
in commandline you can use curl
```bash 
curl http://127.0.0.1:5000/?zip=30009
```
# Developer Tools
## Linting
- pycodestyle <filename>: use to check if code complies with code style guide
ex: `pycodestyle example-package/example.py`

## Setuptools
- Command to Create the package to distribute in dist folder <ProjectName>-<version>.tar.gz (like dist/example_package-0.0.1.tar.gz)
`python setup.py sdist`
- For More info type:
`python setup.py --help-commands`

- helps in module discovery using find_packages(), so we can refer to all modules without relative import

## Unit Test Running
- Running all unit tests in the command line:
`python -m unittest -v example_package/tests/test_example.py`
- Running a specific test in a TestExample class in test_example test module:
`python -m unittest example_package.tests.test_example.TestExample.test_greater_than`
