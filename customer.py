from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask import Blueprint
from configuration import db,ma

class Customer(db.Model):
    id_cliente = db.Column(db.String(25), primary_key=True, unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(150), primary_key=True, unique=True)
    direccion = db.Column(db.String(250))
    telefono = db.Column(db.String(25))
    mobil = db.Column(db.String(25))
    no_documento = db.Column(db.String(50))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, id_cliente, nombre,apellido,email,direccion,telefono,mobil,no_documento):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.mobil = mobil
        self.no_documento = no_documento

db.create_all()

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id_cliente', 'nombre', 'apellido','email','direccion','telefono','mobil','no_documento')


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

customer_blueprint = Blueprint('get_customer', __name__)


#  ALL RECORDS
@customer_blueprint.route('/customer', methods=['GET'])
def get_customer():
  all_customer = Customer.query.all()
  result = customers_schema.dump(all_customer)
  return jsonify(result)
# ****************************************************

# @status_blueprint.route('/status/<id_status>', methods=['GET'])
# def get_task(id_status):
#   status = Status.query.get(id_status)
#   return status_schema.jsonify(status)

# NEW RECORD
# @status_blueprint.route('/status', methods=['POST'])
# def create_status():
#   status_name = request.json['status_name']
#   status_description = request.json['status_description']
#   new_status = Status(status_name, status_description)
#   db.session.add(new_status)
#   db.session.commit()
#   return status_schema.jsonify(new_status)
# ******************************************************************

# UPDATE RECORD
# @status_blueprint.route('/status/<id_status>', methods=['PUT'])
# def update_status(id_status):
#   status = Status.query.get(id_status)
#   status_name = request.json['status_name']
#   status_description = request.json['status_description']
#   status.status_name = status_name
#   status.status_description = status_description
#   db.session.commit()
#   return status_schema.jsonify(status)
# ******************************************************************


# DELETE RECORD
# @status_blueprint.route('/status/<id_status>', methods=['DELETE'])
# def delete_status(id_status):
#   status = Status.query.get(id_status)
#   db.session.delete(status)
#   db.session.commit()
#   return status_schema.jsonify(status)
# *****************************************************


