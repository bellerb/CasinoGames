from playingCards import cards
from cardGames import games

print('****Welcome to Console Casino****\n')

options = ['BLACKJACK']
while True:
    print('Options:\n')
    for i,game in enumerate(options):
        if i < len(options)-1:
            print('-{}'.format(game))
        else:
            print('-{}\n'.format(game))
    userInput = input('What game would you like to play?\n')
    if userInput.upper() not in options:
        print('Sorry invalid game\n')
    else:
        break

players = [{'Name':'Ben','Score':50.00}]
if userInput.upper() == 'BLACKJACK':
    print('\n****Welcome to Black Jack****')
    while True:
        deck = cards.deck()
        players = games().blackJack(players,deck)
        i = 0
        while i < len(players):
            if players[i]['Score'] == 0:
                print("\n{}'s out of points".format(players[i]['Name']))
                del players[i]
            else:
                qCheck = False
                while True:
                    q = input('\n{} has {} points would you like to continue playing? (Yes/No)\n'.format(players[i]['Name'],players[i]['Score']))
                    if q.upper() == 'YES':
                        qCheck = True
                        break
                    if q.upper() == 'NO':
                        break
                    else:
                        print('Sorry that is not an avalible option')
                if qCheck == False:
                    del players[i]
                else:
                    i = i + 1
        if len(players) == 0:
            break
