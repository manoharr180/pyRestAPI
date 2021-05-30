import os
from flask import Flask
from pyRestAPI.src.router import routers

template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder=template_dir)

routers.init_route(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)
    # port = 5000, debug = True, threaded = False
