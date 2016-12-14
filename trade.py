def playerTrade(turn, order, target):

    #Determine which player is the object of the trade
    for each in order:
        if target == 1:
            trader = each
        elif target == 2:
            trader = each
        elif target == 3:
            trader = each
        else:
            print 'Error, invalid trade target.'
            return

    #Read in the sent info
    print 'Active Player'
    wool = raw_input('Wool: ')
    wheat = raw_input('Wheat: ')
    brick = raw_input('Brick: ')
    stone = raw_input('Stone: ')
    wood = raw_input('Wood: ')

    #Remove active player resources
    turn.resources['wool'] -= wool
    turn.resources['wheat'] -= wheat
    turn.resources['brick'] -= brick
    turn.resources['stone'] -= stone
    turn.resources['wood'] -= wood

    #Read in the object info
    print 'Active Player'
    wool = raw_input('Wool: ')
    wheat = raw_input('Wheat: ')
    brick = raw_input('Brick: ')
    stone = raw_input('Stone: ')
    wood = raw_input('Wood: ')

    #Remove active player resources
    trader.resources['wool'] += wool
    trader.resources['wheat'] += wheat
    trader.resources['brick'] += brick
    trader.resources['stone'] += stone
    trader.resources['wood'] += wood

    return

def ekoTrade():

    return
