from flask_restful import abort, Resource
from flask import current_app
from pilibs import rcs380


class FeliCa(Resource):

    def get(self):
        try:
            result = rcs380.scan()
        except IOError:
            if current_app.config['TESTING']:
                return {'idm': '0x00000000000000'}
            return abort(500, message="FeliCa Device Error")

        if result is None:
            return '', 204
        else:
            return {'idm': result}
