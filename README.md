# FlaskZipLookupApiExample
An example web service API implemented in Python using Flask framework.

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
