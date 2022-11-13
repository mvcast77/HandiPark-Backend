from flask import Flask,request
from dotenv import load_dotenv

import json
import requests
import os
from functions import *
from script import *

load_dotenv()

app = Flask(__name__)

APP_ID = '1c3u7ib9k2' # os.getenv('APP_ID')
APP_KEY = 'uQLYgW5zay6z53r4BV4bk3fAS2S7dRlt7WGsFcHU' # os.getenv('APP_KEY')
HASH_TOKEN = 'MWMzdTdpYjlrMnx1UUxZZ1c1emF5Nno1M3I0QlY0YmszZkFTMlM3ZFJsdDdXR3NGY0hV' # os.getenv('HASH_TOKEN')
EXPIRATION_DATE = '2022-11-27T20:05:09.645Z' # os.getenv('EXPIRATION_DATE')
BASE_URL = 'https://api.iq.inrix.com/' # os.getenv('BASE_URL')

@app.route('/viola', methods = ['GET'])
def viola():
	startCoords = request.args.get('startCoords', default = '37.857,-122.4951334', type = str)
	destCoords = request.args.get('destCoords', default = '37.730904,-122.401962', type = str)
	totalTime = request.args.get('totalTime', default = 60, type = int)

	return run(startCoords, destCoords, totalTime)