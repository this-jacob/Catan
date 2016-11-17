def road(turn, location, order):

    #Check through players and make sure that the location isn't in use
    for each in order:
        if location in each.cities:
            print 'Already Occupied.'
            return

    #Pay for the build
    if turn.resources['wood'] >= 1:
        turn.resources['wood'] -= 1
    else:
        print 'Not enough wood.'
        return

    if turn.resources['brick'] >= 1:
        turn.resources['brick'] -= 1
    else:
        print 'Not enough brick.'
        return

    #Build the road
    turn.road.append(location)

    return

def settlement(turn, location, order):

    #Check through players and make sure that the location isn't in use
    for each in order:
        if location in each.settlements:
            print 'Already Occupied.'
            return

    #MAKE SURE THAT THERE ARE NO ADJACENT BUILDS!

    #Pay for the Build
    if turn.resources['wood'] >= 1:
        turn.resources['wood'] -= 1
    else:
        print 'Not enough wood.'
        return

    if turn.resources['brick'] >= 1:
        turn.resources['brick'] -= 1
    else:
        print 'Not enough brick.'
        return

    if turn.resources['wheat'] >= 1:
        turn.resources['wheat'] -= 1
    else:
        print 'Not enough wheat.'
        return

    if turn.resouces['wool'] >= 1:
        turn.resources['wool'] -= 1
    else:
        print 'Not enough wool.'
        return

    #Build the settlement
    turn.settlements.append(location)

    return

def city(turn, location):

    #Make sure that the player has a settlement to upgrade
    if not location in turn.settlements:
        print 'Invalid Location'
        return

    #Pay for the city
    if turn.resources['wheat'] >= 2:
        turn.resources['wheat'] -= 2
    else:
        print 'Not enough wheat.'
        return

    if turn.resources['stone'] >= 3:
        turn.resources['stone'] -= 3
    else:
        print 'Not enough stone.'
        return

    #Upgrade to the city
    turn.settlements.remove(location)
    turn.cities.append(location)

    return

def development(turn):

    #Pay for the development card
    if turn.resources['wool'] >= 1:
        turn.resources['wool'] -= 1
    else:
        print 'Not enouh wool.'
        return

    if turn.resources['wheat'] >= 1:
        turn.resources['wheat'] -= 1
    else:
        print 'Not enough wheat.'
        return

    if turn.resources['stone'] >= 1:
        turn.resources['stone'] -= 1
    else:
        print 'Not enough stone.'
        return

    #"build" the card
    cardType = raw_input('Card Type: ')
    turn.developments[cardType] += 1

    return
