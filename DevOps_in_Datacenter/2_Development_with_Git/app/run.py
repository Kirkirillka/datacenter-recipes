import json

import flask

from flask import jsonify, request
from pymongo import MongoClient

app = flask.Flask(__name__)

client = MongoClient("localhost", 27017)

db = client["python-microservice"]
collection = db['userdata']


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

    doc = collection.find_one({"id": id})

    sanitized_doc = json.dumps(doc, default=str)

    return jsonify({
        "status": "ok",
        "requested_id": id,
        "data": sanitized_doc
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

    user_data['id'] = id

    entry_id = collection.insert_one(user_data).inserted_id

    return jsonify({
        "status": "ok",
        "message": "Data saved",
        "doc_id": str(entry_id)
    })


if __name__ == '__main__':
    app.run("0.0.0.0", 9000)
