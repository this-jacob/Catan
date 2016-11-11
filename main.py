import json, player

def main():

    #Create the players and trackers
    player1 = player.Player('Player One')
    player2 = player.Player('Player Two')
    player3 = player.Player('Player Three')
    alicia = player.Player('Alicia')

    order = [player1, player2, player3, alicia]

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



    return 0

if __name__ == '__main__':
    main()
