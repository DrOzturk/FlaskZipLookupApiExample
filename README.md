# FlaskZipLookupApiExample
An example web service API implemented in Python using Flask framework.
```bash
# clone this repo to local
git clone git@github.com:DrOzturk/FlaskZipLookupApiExample.git
# if you don't have python 3 as default, first do this
pipenv --three
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

## Test code in iPython
You can defines methods, run the codes and create the globals like this:
```python
exec(open('load.py').read())
# Now you can do
dict_zips['30009']
```
## Using PyCharm
If you right clicking on service.py and running in PyCharm, edit your "Run Configurations" 
and set your Working Directory to project directory, like:
`/Users/ozgurozturk/IdeaProjects/FlaskZipLookupApiExample/`

# Developer Tools
## Linting
- pycodestyle <filename>: use to check if code complies with code style guide
ex: 
```bash
pycodestyle zips/load.py
```

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

# Future
Use flask_restful:
http://flask-restful.readthedocs.io/en/latest/quickstart.html
should be something like
```python
from zips.load import state_for
from flask import Flask
from flask_restful import Resource, Api

app = Flask('__name__')
api = Api(app)
error_json = """{
    "errors": [
        {
            "type": "Missing parameter",
            "message": "Zip must be provided",
            "code": 0
        }
    ],
    "status": "BAD_REQUEST"
}"""

class Zip(Resource):
    def get(self, zipcode):
        if (not zipcode or zipcode.strip(" \"'.?!,")== ""):
            return error_json
        return state_for(zipcode)

api.add_resource(Zip,'/?zip=<string:zip>')

if __name__ == '__main__':
    app.run(debug=True)
```