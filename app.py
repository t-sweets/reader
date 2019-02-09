import os
from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


if __name__ == '__main__':
    app.run()
