import json

#Iterate through the players based on the given order and play
def start(order):

    #Run through place order in order
    for each in order:
        if each.name == 'Diana'
            dianaSettlements(each)
        else:
            placeSettlements(each)

    #Snake back through the order
    for each in reversed(order):
        if each.name == 'Diana'
            dianaSettlements(each)
        else:
            placeSettlements(each)

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
        for path in cities[location]['paths']
            print path ,
            openPaths.append(path)
        print

        #Get the player road choice
        pathLoc = raw_input('Path Location: ')

        #Add the path
        if pathLoc in openPaths:
            turn.roads.append(pathLoc)
            placed = True

    return

def dianaSettlements(diana):


    getResources(diana, location)
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
