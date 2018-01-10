from zips.load import state_for
#in iPython, above import does not run the codes to create the globals! only defines methods.
#uncomment line below, if you are running in iPython
#exec(open('carotene_helper.py').read())

from flask import Flask
from flask import request

app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def lookup():
    # if you don't care/know whether the value is in the query string or in the post data, you can use values.get
    # values is a CombinedMultiDict that combines Dicts from request.form and request.args.
    if request.mimetype == 'application/json':
        data = request.get_json()
        zip = data['zip'] if 'zip' in data else ''
    else:
        zip = request.values.get('zip', '')

    if (not zip or zip.strip(" \"'.?!,")==""):
        return """{
    "errors": [
        {
            "type": "Missing parameter",
            "message": "Zip must be provided",
            "code": 0
        }
    ],
    "status": "BAD_REQUEST"
}"""
    return state_for(zip)

app.run(host= '0.0.0.0',port=5000)