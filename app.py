import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api.felica import FeliCa
from api.message import Message
from api.led import Led

#
# def initialize():
#     from pilibs.sc1602 import SC1602
#     import socket
#     lcd = SC1602()
#     lcd.string("Reader is Ready", 1)
#     lcd.string(socket.gethostbyname(socket.gethostname()), 2)
#     lcd.cleanup()


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config.from_object(os.environ.get("READER_ENV"))

api.add_resource(FeliCa, '/api/v1/card')
api.add_resource(Message, '/api/v1/message')
api.add_resource(Led, '/api/v1/led')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
