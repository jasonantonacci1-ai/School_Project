import logging
from flask import Flask
from flask_cors import CORS, cross_origin

from database.db import connect_db
from handlers.employee import (
    add_employee,
    get_employees,
    delete_employee,
    update_employee,
)

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

connect_db()
logging.info("Employee Service initialized successfully")


@cross_origin()
@app.route("/add-employee", methods=["POST"])
def add_employee_route():
    return add_employee()


@cross_origin()
@app.route("/employees", methods=["GET"])
def get_employees_route():
    return get_employees()


@cross_origin()
@app.route("/delete-employee", methods=["DELETE"])
def delete_employee_route():
    return delete_employee()


@cross_origin()
@app.route("/update-employee", methods=["PUT"])
def update_employee_route():
    return update_employee()


if __name__ == "__main__":
    logging.info("Employee Service running on port 5003")
    app.run(host="0.0.0.0", port=5003)
