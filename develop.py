import build

def roadBuilding(turn):

    #Build two roads
    location = raw_input('First Location: ')
    build.road(turn, location)
    location = raw_input('Second Location: ')
    build.road(turn, location)

    return

def yearOfPlenty(turn):

    #Add two resources to your player
    resource = raw_input('First Resource: ')
    turn.resources[resource] += 1
    resource = raw_input('Second Resource: ')
    turn.resources[resource] += 1

    return

def monopoly(turn, order):

    #Find resource to steal
    resource = raw_input('Resource Type: ')
    total = 0

    #Steal all the resources of one type
    for each in order:
        while each.resources[resource] > 0:
            each.resources[resource] -= 1
            total += 1

    #Give all the resources to the active player
    turn.resources[resource] += total

    return
