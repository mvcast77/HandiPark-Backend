from flask import Flask,request
from dotenv import load_dotenv

import json
import requests
import os
from functions import *
from script import *

load_dotenv()

app = Flask(__name__)

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
HASH_TOKEN = os.getenv('HASH_TOKEN')
EXPIRATION_DATE = os.getenv('EXPIRATION_DATE')
BASE_URL = os.getenv('BASE_URL')

@app.route('/viola', methods = ['GET'])
def viola():
	startCoords = request.args.get('startCoords', default = '37.857,-122.4951334', type = str)
	destCoords = request.args.get('destCoords', default = '37.730904,-122.401962', type = str)
	totalTime = request.args.get('totalTime', default = 60, type = int)

	return run(startCoords, destCoords, totalTime)