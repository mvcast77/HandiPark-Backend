import json
import os
import requests

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
HASH_TOKEN = os.getenv('HASH_TOKEN')
EXPIRATION_DATE = os.getenv('EXPIRATION_DATE')
BASE_URL = os.getenv('BASE_URL')

def getToken():
    headers = {}

    tokenRequestString = BASE_URL + 'auth/v1/AppToken?appId=' + APP_ID + '&hashToken=' + HASH_TOKEN
    tokenResponseObj = json.loads(requests.get(tokenRequestString, headers=headers).text)

    return tokenResponseObj['result']['token']

#wp = waypoint
def getRoutes(token, wp1, wp2):
    headers = {'Authorization': 'Bearer' + token}

    routeRequestString = BASE_URL + 'findRoute?wp_1=' + wp1 + 'findRoute?wp_2=' + wp2 + \
                         '&maxAlternates=3&useTraffic=true&routeOutputFields=ALL&format=json'
    routeResponseObj = json.loads(requests.get(routeRequestString, headers=headers).text)

    return routeResponseObj['result']['trip']['routes']

def getLots(token, point, radius):
	headers = {'Authorization': 'Bearer' + token}

	lotsRequestString = BASE_URL + 'lots/v3?point=' + point + 'lots/v3?radius=' + radius
	lotsResponseObj = json.loads(requests.get(lotsRequestString, headers=headers).text)

	return lotsResponseObj['result']

def simplifyLot(parkingDict):

	return parkingDict

def simplifyRoute(routeDict):

	return routeDict