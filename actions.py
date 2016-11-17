import json, player, trade, develop, build

#Main AI loop
def runDiana():

    return

#Specifically for inputing the player's turn
def runPlayer(turn, order):

    over = false

    while not over:
        command = raw_input('|:')

        #Code For Printing the Help Menus
        if command = 'help':
            print 'b to build, p to play a development card, t to trade, o to end turn'
            print 'Building: s for settlement, c for city, r for road, d for development'
            print 'Playing Developments: k for knight, v for victory point, r for roadbuilding, m for monopoly, y for year of plenty'  #TODO Put in development cards
            print 'Trading: enter t-help for a list of instructions.''
        elif command == 't-help':
            print 'Trading Help: First enter the desired player. If the player is Diana a prompt will appear.'
            print 'Enter in the resources to be sent from the active player.'
            print 'Then enter the resources to be recieved from the object player.'

        #Building Code
        elif command == 'b':
            building = raw_input('Build: ')
            intersection = raw_input('Location: ')

            if building == 's':
                build.settlement(turn, intersection, order)
            elif building == 'c':
                build.city(turn, intersection)
            elif building == 'r':
                build.road(turn, intersection, order)
            elif building == 'd':
                build.development(turn)

        #Development card code
        elif command == 'p':
            card = raw_input('Card Code')

            if card == 'k':
                knight()
            elif card == 'v':
                turn.vps += 1
            elif card == 'r':
                develop.roadBuilding()
            elif card == 'm':
                develop.monopoly()
            elif card == 'y':
                develop.yearOfPlenty()

        #Trading Code
        elif command == 't':
            target = raw_input('Trading Target: ')

            if not target == 'd':
                trade.playerTrade(turn, order, target)
            else:
                trade.dianaTrade()

        #End turn code
        elif command == 'o':
            over = true

    return

#Pass in the players and the roll
#Adds resources to all adjacent towns
def genResources(roll, order):

    #Open the hexes json file into the location 'hexes'
    with open('Connections\\hexes.json') as hexes_data:
        hexes = json.load(hexes_data)

    #Check through each of the hexes for a production on a roll
    for each in hexes:
        if hexes[each]['roll'] == int(roll):
            #When a hex is found, check through the players to see if they have a building there
            for player in order:
                #Give resources for each setlement
                for town in player.setlements:
                    if town in hexes[each]['cities']:
                        player.resources[hexes[each]['produce']] += 1
                #Give resources for each city
                for city in player.cities:
                    if city in hexes[each]['cities']:
                        player.resources[hexes[each]['produce']] += 2
    return
