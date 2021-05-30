from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello from docker"


@app.route("/users")
def users():
    return "{ name: dockerHello from docker}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001", debug=True, threaded=False)
    # port = 5000, debug = True, threaded = False
