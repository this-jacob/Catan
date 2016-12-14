import json

#Iterate through the players based on the given order and play
def start(order):

    #Run through place order in order
    for each in order:
        if each.name == 'eko':
            print 'eko\'s thinking.'
            ekoSettlements(each, order)
        else:
            print each.name
            placeSettlements(each, order)
        print '\n\n\n'

    #Snake back through the order
    for each in reversed(order):
        if each.name == 'eko':
            print 'eko\'s thinking.'
            ekoSettlements(each, order)
        else:
            print each.name ,
            placeSettlements(each, order)

    return

#Place human settlements and check for valid locations
def placeSettlements(turn, order):

    #Logic flags
    flag = True
    placed = False

    #Loop until a valid settlement is placed
    while not placed:

        #Get location to place
        location = raw_input('Settlement Location: ')

        #Check to see if other players have played there
        for each in order:
            if location in each.settlements:
                flag = False

        #Place the settlement if there isn't one anywhere
        if flag:
            turn.settlements.append(location)
            placeRoads(turn, location)
            placed = True
        else:
            print 'Invalid location'
            flag = True

    getResources(turn, location)

    return

def placeRoads(turn, location):

    #Declare local variables
    openPaths = []
    placed = False

    #Open the cities path that contains the adjacent paths
    with open("Connections\\cities.json") as cities_data:
        cities = json.load(cities_data)

    #Continue until a legal placement is done
    while not placed:
        #Print out the adjacent paths
        print 'Valid road placements: ' ,
        for path in cities[location]['paths']:
          print path ,
          openPaths.append(path)
        print

        #Get the player road choice
        pathLoc = int(raw_input('Path Location: '))

        #Add the path
        if pathLoc in openPaths:
            turn.roads.append(pathLoc)
            placed = True

    return

def ekoSettlements(eko, order):

    resourceDict = {}
    resourceDict['wool'] = 1
    resourceDict['wheat'] = 2
    resourceDict['wood'] = 5
    resourceDict['stone'] = 3
    resourceDict['brick'] = 4
    resourceDict['dessert'] = 0

    valueDict = {}
    possibleLocations = []

    location = 0
    highestValue = -1
    value = 0
    flag = True

    #Open up the hexes json file
    with open("Connections\\hexes.json") as hexes_data:
        hexes = json.load(hexes_data)
    #Open up the cities json file
    with open("Connections\\cities.json") as cities_data:
        cities = json.load(cities_data)

    #Check each city for the one with the greatest value
    for each in cities:
        for eachHex in cities[each]['hexes']:
            value += resourceDict[hexes[str(eachHex)]['produce']]

        #Save the values of all the cities
        valueDict[each] = value
        value = 0

#Everything is proper

    #Sort the possible locations into an ordered array
    #Find the highest possible value
    for each in valueDict:
        if valueDict[each] > highestValue:
            highestValue = valueDict[each]

    #Add everything to the array witht the highest valued first to the lowest valued
    while highestValue > 0:
        for each in valueDict:
            if valueDict[each] == highestValue:
                possibleLocations.append(each)
        highestValue -= 1

    #check the valid locations
    for poss in possibleLocations:
        flag = False
        #Check through all other peoples used settlements
        for play in order:
            for sett in play.settlements:
                if sett == poss:
                    flag = True

        #Break if a correct location has been found
        if not flag:
            location = poss
            break

    #At this point the location has been chosen
    print 'eko\'s location choice: ' ,
    print location

    #Build the settlement in the world
    eko.settlements.append(location)

    #Choose a road placement
    #TODO: CHOOSE A ROAD

    getResources(eko, location)
    return

def getResources(turn, location):

    #Open up the hexes json file
    with open("Connections\\hexes.json") as hexes_data:
        hexes = json.load(hexes_data)

    #Get the resource produced by that resource
    for each in hexes:
        if location in hexes[each]['cities']:
            if not hexes[each]['produce'] == 'dessert':
                turn.resources[hexes[each]['produce']] += 1

    return
