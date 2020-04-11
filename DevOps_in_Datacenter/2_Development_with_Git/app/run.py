import flask
from flask import jsonify


app = flask.Flask(__name__)

@app.route("/")
def index():
    """
        Initial page to return on "/" path
    :return:
    """
    return jsonify({
        "status": "ok",
        "page": "index"
    })


@app.route("/user/get/<int:id>",methods=["GET"])
def get_by_id(id):
    """
        URI to return data about the user for the given ID
    :param id: user_id
    :return:
    """
    return jsonify({
        "status": "ok",
        "requested_id": id
    })

if __name__ == '__main__':
    app.run("0.0.0.0",9000)