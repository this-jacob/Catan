import player, actions

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
            actions.genResources(roll, order)

            #AI Split
            if turn.name == 'Diana':
                #Run AI Code
                actions.runDiana()
            else:
                #Run Human Code
                actions.runPlayer(turn, order)

    return 0

if __name__ == '__main__':
    main()
