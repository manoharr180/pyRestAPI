from flask import Flask
from pyRestAPI.router import routers

app = Flask(__name__)

routers.init_route(app)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=False)
