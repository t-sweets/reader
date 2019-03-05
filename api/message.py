# -*- coding: utf-8 -*-
from flask_restful import abort, Resource, reqparse
from flask import current_app

parser = reqparse.RequestParser()
parser.add_argument('line_1', type=str, required=True)
parser.add_argument('line_2', type=str, required=True)


class Message(Resource):

    def post(self):
        args = parser.parse_args()

        try:
            from pilibs.sc1602 import SC1602
            lcd = SC1602()
        except Exception:
            if current_app.config['TESTING']:
                return args, 201
            return abort(500, message="Lcd Module Error")

        lcd.string(args['line_1'], 1)
        lcd.string(args['line_2'], 2)
        lcd.cleanup()

        return args, 201
