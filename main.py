import json, player

def main():

    #Create the players and trackers
    player1 = player.Player('Player One')
    player2 = player.Player('Player Two')
    player3 = player.Player('Player Three')
    diana = player.Player('diana')

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

            genResources(roll, order)

    return 0

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
