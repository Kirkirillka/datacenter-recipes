import flask

from flask import jsonify, request

from config import *
from db import get_userdata_by_id, save_userdata_by_id


app = flask.Flask(__name__)


@app.route("/")
def index():
    """
        Initial page to return on "/" path


        Example:

        curl localhost:9000/

    :return:
    """
    return jsonify({
        "status": "ok",
        "page": "index"
    })


@app.route("/user/get/<int:id>", methods=["GET"])
def get_by_id(id):
    """
        URI to return data about the user for the given ID

        Example:

            curl localhost:9000/user/get/231


    :param id: user_id
    :return:
    """

    doc = get_userdata_by_id(id)

    return jsonify({
        "status": "ok",
        "requested_id": id,
        "data": doc
    })


@app.route("/user/add/<int:id>", methods=["POST"])
def add_by_id(id):
    """

    Example:


        curl -X POST localhost:9000/user/add/231   -H "Content-Type: application/json"  --data '{"name": "Ivan"}'

    :param id:
    :return:
    """

    user_data = request.json or {}

    entry_id = save_userdata_by_id(id, user_data)

    return jsonify({
        "status": "ok",
        "message": "Data saved",
        "doc_id": str(entry_id)
    })


if __name__ == '__main__':
    app.run(HOST, PORT)
