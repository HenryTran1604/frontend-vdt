from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)
client = MongoClient(os.environ.get('MONGO_URL', 'mongodb://localhost:27017'))
# print(os.environ.get('MONGO_URL', 'mongodb://localhost:27017'))
db = client['midterm']