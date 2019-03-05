from flask_restful import abort, Resource
from flask import current_app
import time

class FeliCa(Resource):

    def get(self):
        try:
            time.sleep(2)
            from pilibs import rcs380
            result = rcs380.scan()
        except Exception:
            if current_app.config['TESTING']:
                return {'idm': '0x00000000000000'}
            return abort(500, message="FeliCa Device Error")

        if result is None:
            return '', 204
        else:
            return {'idm': result}
