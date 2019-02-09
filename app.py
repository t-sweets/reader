import os
from flask import Flask
from flask_restful import Api

from api.felica import FeliCa
from api.message import Message
from api.led import Led

app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ.get("READER_ENV"))

api.add_resource(FeliCa, '/api/v1/nfc')
api.add_resource(Message, '/api/v1/message')
api.add_resource(Led, '/api/v1/led')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
