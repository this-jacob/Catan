import json, player, trade, develop, build

def main():

    #Create the players and trackers
    player1 = player.Player('Player One')
    player2 = player.Player('Player Two')
    player3 = player.Player('Player Three')
    diana = player.Player('Diana')

    order = [player1, player2, player3, diana]

    roll = 0

    while True:
        for turn in order:
            print '\n\n', turn.name

            #Get the roll
            roll = raw_input('Input Roll: ')
            #Testing if to exit with exit
            if roll == 'exit':
                return 0
            #DON'T FORGET TO REMOVE THE PREVIOUS LINE BEFORE FINAL!

            #MAIN LOOP BELOW
            #All Players
            genResources(roll, order)

            #AI Split
            if turn.name == 'Diana':
                #Run AI Code
                runDiana()
            else:
                #Run Human Code
                runPlayer(turn, order)

    return 0

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
            print 'b to build, p to play a development card, t to trade'
            print 'Building: s for settlement, c for city, r for road, d for development'
            print 'Playing Developments: k for knight, v for victory point, r for roadbuilding, m for monopoly, y for year of plenty'  #TODO Put in development cards
            print 'Trading: enter t-help for a list of instructions.'
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

if __name__ == '__main__':
    main()
