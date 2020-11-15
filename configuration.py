from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask import Blueprint
from dotenv import load_dotenv
import connexion
import os


load_dotenv()
# LOAD ENV DB VAR**********************
ENV_VAR_DB_USER = os.getenv('DB_USER')
ENV_VAR_DB_HOST = os.getenv('DB_HOST')
ENV_VAR_DB_NAME = os.getenv('DB_NAME')
# *************************************

app = Flask(__name__)
mysql_url = "mysql+pymysql://"+ENV_VAR_DB_USER+"@"+ENV_VAR_DB_HOST+"/"+ENV_VAR_DB_NAME
app.config["SQLALCHEMY_DATABASE_URI"] = mysql_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)