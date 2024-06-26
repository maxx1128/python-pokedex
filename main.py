from flask import Flask, render_template

from app.api.base_api import BaseAPI

app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
def index(name=None):
    BaseAPI().test_request()
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
