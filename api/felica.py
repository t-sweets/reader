from flask_restful import abort, Resource
from flask import current_app

from Queue import Queue
import time
import functools


class FeliCa(Resource):

    singleQueue = Queue(maxsize=1)

    def multiple_control(q):
        def _multiple_control(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                q.put(time.time())
                print("/// [start] critial zone")
                result = func(*args,**kwargs)
                print("/// [end] critial zone")
                q.get()
                q.task_done()
                return result

            return wrapper
        return _multiple_control

    @multiple_control(singleQueue)
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
