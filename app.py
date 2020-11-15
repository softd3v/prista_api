from flask import Flask
# from configuration import db,ma


# LOCAL MODULES
from status import status_blueprint
from customer import customer_blueprint


app = Flask(__name__)
app.register_blueprint(status_blueprint)
app.register_blueprint(customer_blueprint)

