from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask import Blueprint
from configuration import db,ma


class Status(db.Model):
    id_status = db.Column(db.Integer, primary_key=True, unique=True)
    status_name = db.Column(db.String(10), unique=True)
    status_description = db.Column(db.String(100))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, status_name, status_description):
        self.status_name = status_name
        self.status_description = status_description

db.create_all()

class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id_status', 'status_name', 'status_description','timestamp')


status_schema = StatusSchema()
status_s_schema = StatusSchema(many=True)

status_blueprint = Blueprint('get_status', __name__)


#  ALL RECORDS
@status_blueprint.route('/status', methods=['GET'])
def get_status():
  all_status = Status.query.all()
  result = status_s_schema.dump(all_status)
  return jsonify(result)
# ****************************************************

@status_blueprint.route('/status/<id_status>', methods=['GET'])
def get_task(id_status):
  status = Status.query.get(id_status)
  return status_schema.jsonify(status)

# NEW RECORD
@status_blueprint.route('/status', methods=['POST'])
def create_status():
  status_name = request.json['status_name']
  status_description = request.json['status_description']
  new_status = Status(status_name, status_description)
  db.session.add(new_status)
  db.session.commit()
  return status_schema.jsonify(new_status)
# ******************************************************************

# UPDATE RECORD
@status_blueprint.route('/status/<id_status>', methods=['PUT'])
def update_status(id_status):
  status = Status.query.get(id_status)
  status_name = request.json['status_name']
  status_description = request.json['status_description']
  status.status_name = status_name
  status.status_description = status_description
  db.session.commit()
  return status_schema.jsonify(status)
# ******************************************************************


# DELETE RECORD
@status_blueprint.route('/status/<id_status>', methods=['DELETE'])
def delete_status(id_status):
  status = Status.query.get(id_status)
  db.session.delete(status)
  db.session.commit()
  return status_schema.jsonify(status)
# *****************************************************

@status_blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'HOLA QUE TAL!'})



# if __name__ == "__main__":
#     app.run(debug=True)