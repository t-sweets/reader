from flask_restful import abort, Resource
from pilibs import rcs380


class FeliCaAPI(Resource):

    def get(self):
        try:
            result = rcs380.scan()
        except IOError:
            return abort(500, message="FeliCa Device Error")

        if result is None:
            return '', 204
        else:
            return {'idm': result}
