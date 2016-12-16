#Atleast this isn't a financial app.
import player, actions, gamestart

def main():

    #Create the players and trackers
    player1 = player.Player('Player One')
    player2 = player.Player('Player Two')
    player3 = player.Player('Player Three')
    eko = player.Player('eko')

    order = [player1, player2, player3, eko]

    roll = 0

    gamestart.start(order)

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
            if turn.name == 'eko':
                #Run AI Code
                actions.runeko(turn)
            else:
                #Run Human Code
                actions.runPlayer(turn, order)

            if turn.vps >= 10:
                print turn.name ,
                print ' is the winner.'
                return 0

    return 0

if __name__ == '__main__':
    main()
