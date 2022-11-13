from functions import *
# Assume startCoods, destCoords, totalTime

# radius exists
radius = 1000

def run(startCoords, destCoords, totalTime):
	token = getToken()
	LotsData = getLots(token,destCoords,radius)
	LotsFinished = []
	RoutesFinished = []
	clusters = 0

	for parkingLot in LotsData:
		if(parkingLot['handicapSpacesTotal'] > 0):
			if((int(parkingLot['handicapSpacesTotal']) * int(parkingLot['occupancy']["probability"]) / 100) >= 1):# Not Done
				parkingLot = simplifyLot(parkingLot)
				clusters = clusters + 1
				LotsFinished.append(parkingLot)

	for i in range(clusters - 1):
		parkingCoords = LotsFinished[i]['point']['coordinates']
		routingData = getRoutes(token, startCoords, parkingCoords)

		for route in routingData:
			if(route["uncongestedTravelTime"] < totalTime):
				route = simplifyRoute(route)
				route['cluster'] = i
				RoutesFinished.append(route)
	end = {}
	end['lots'] = LotsFinished
	end['routes'] = RoutesFinished

	return end