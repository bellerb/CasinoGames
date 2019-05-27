from playingCards import cards
from cardGames import games
from booking import book

print('****Welcome to Console Casino****\n')

while True:
    numPlayers = input('How many players are playing?\n')
    if numPlayers.isnumeric():
        numPlayers = int(numPlayers)
        print()
        break
    else:
        print('Sorry your answer must be an integer\n')

players = []
accounts = book.loadAccounts()
accountN = accounts['Name'].tolist() #Name of accounts
for x in range(numPlayers):
    while True:
        print('Player accounts:\n')
        for name in accountN:
            print('-{}'.format(name))
        print('-New\n')
        pName = input('Which account are you?\n')
        if pName in accountN:
            players.append(accounts[accounts['Name']==pName].to_dict('records')[0])
            del accountN[accountN.index(pName)]
            break
        elif pName.upper() == 'NEW':
            pName = input('\nWhat do you want your name to be?\n')
            accounts = book.newAccount(pName,50,accounts)
            book.saveScores(accounts)
            players.append(accounts[accounts['Name']==pName].to_dict('records')[0])
            break
        else:
            print('Sorry that account does not exist\n')
print()

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

if userInput.upper() == 'BLACKJACK':
    print('\n****Welcome to Black Jack****')
    while True:
        deck = cards.deck()
        players = games().blackJack(players,deck)
        accounts = book.updateScores(players,accounts)
        book.saveScores(accounts)
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
