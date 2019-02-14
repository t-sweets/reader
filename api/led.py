from flask_restful import abort, Resource, reqparse
from flask import current_app

COLORS = (
    "error",
    "success",
    "waiting",
    "destroy"
)

parser = reqparse.RequestParser()
parser.add_argument("mode",
                    choices=COLORS,
                    required=True,
                    help="Bad choice: {error_msg}. please select error, success, waiting, destroy")


class Led(Resource):

    def post(self):
        args = parser.parse_args()

        try:
            from pilibs.rgb import RGB
            led = RGB()
        except Exception:
            if current_app.config['TESTING']:
                return args, 201
            return abort(500, message="Led Module Error")

        if args["mode"] == "error":
            led.red()
        elif args["mode"] == "success":
            led.green()
        elif args["mode"] == "waiting":
            led.blue()
        else:
            led.destroy()

        return args, 201
