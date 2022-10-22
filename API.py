import pandas as pd
import sklearn as sk
import flask
from flask import Flask, request
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app)