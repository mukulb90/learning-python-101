from flask import Flask, Response
import logging
from flask_demo.users import getUsers
import json
app = Flask(__name__)


@app.route('/hello')
def hello():
    logging.info('Request received')
    return 'World'

@app.route('/users')
def users():
    users  = getUsers()
    print(users)
    return Response(json.dumps(users), content_type='application/json');

if __name__ == '__main__':
    app.run(port=8000)