from flask import Flask
from flask_restful import Api

from api.felica import FeliCaAPI
from api.message import Message

app = Flask(__name__)
api = Api(app)

api.add_resource(FeliCaAPI, '/api/v1/nfc')
api.add_resource(Message, '/api/v1/message')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
