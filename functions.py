import json
import os
import requests

APP_ID = '1c3u7ib9k2' # os.getenv('APP_ID')
APP_KEY = 'uQLYgW5zay6z53r4BV4bk3fAS2S7dRlt7WGsFcHU' # os.getenv('APP_KEY')
HASH_TOKEN = 'MWMzdTdpYjlrMnx1UUxZZ1c1emF5Nno1M3I0QlY0YmszZkFTMlM3ZFJsdDdXR3NGY0hV' # os.getenv('HASH_TOKEN')
EXPIRATION_DATE = '2022-11-27T20:05:09.645Z' # os.getenv('EXPIRATION_DATE')
BASE_URL = 'https://api.iq.inrix.com/' # os.getenv('BASE_URL')

def getToken():
    headers = {}

    tokenRequestString = BASE_URL + 'auth/v1/appToken?appId=' + APP_ID + '&hashToken=' + HASH_TOKEN
    tokenResponseObj = json.loads(requests.get(tokenRequestString, headers=headers).text)

    return tokenResponseObj['result']['token']

#wp = waypoint
def getRoutes(token, wp1, wp2):
    headers = {'Authorization': 'Bearer' + token}

    routeRequestString = BASE_URL + 'findRoute?wp_1=' + wp1 + '&wp_2=' + wp2 + '&maxAlternates=0&useTraffic=true&routeOutputFields=ALL&format=json'
    routeResponseObj = json.loads(requests.get(routeRequestString, headers=headers).text)

    return routeResponseObj['result']['trip']['routes']

def getLots(token, point, radius):
	headers = {'Authorization': 'Bearer' + token}

	point = format(point)
	lotsRequestString = BASE_URL + 'lots/v3?point=' + str(point) + '&radius=' + str(radius)
	lotsResponseObj = json.loads(requests.get(lotsRequestString, headers=headers).text)

	return lotsResponseObj['result']

def simplifyLot(parkingDict):

	return parkingDict

def simplifyRoute(routeDict):
    del routeDict['result']['trip']['routes']['routeSpeedBuckets']
    return routeDict

def format(str1):
    str = str1.replace(',','%7C')
    return str