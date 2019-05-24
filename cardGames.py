"""
 * @file cardGames.py
 * @authors Ben Bellerose
 * @date May 23 2019
 * @modified May 24 2019
 * @modifiedby BB
 * @brief class full of playing card games
 */
 """
import pandas as pd
from playingCards import cards

class games():
    """Input: names - list of dictionaries with player name and hand
       Function: set up playing table for players
       Output: list of dictionaries containing player name and hand"""
    def setTable(self,names):
        table = []
        for name in names:
            table.append({'Name':name,'Hand':[]})
        return table

    """Input: deck - list of dictionaries containing card values
              hand - list containing dictionaries of playing cards
       Function: deal a card to the users at the table
       Output: list containing remaining cards in deck and list of dictionaries containing player name and hand"""
    def dealHand(self,deck,hand):
        if len(deck) > 0:
            hand.append(deck[0])
            del deck[0]
        return [deck,hand]

    """Input: player - dictionary containing player name and score
       Function: place a bet for individual player
       Output: list of dictionaries containing player name and hand"""
    def makeBet(self,player,**arg):
        while True:
            if 'bet' in arg:
                bet = arg['bet']
            else:
                bet = input("\n{}'s turn how much do you want to bet? (Funds:{})\n".format(player['Name'],player['Score']))
            try:
                bet = float(bet)
                if float(bet) <= float(player['Score']):
                    bet = float(bet)
                    player['Score'] = player['Score'] - bet
                    break
                else:
                    if 'bet' in arg:
                        bet = float(player['Score'])
                        player['Score'] = player['Score'] - bet
                        break
                    else:
                        print('Desired bet to big select smaller amount')
            except:
                print('Invalid entry bet must be a number')
        return [player,bet]

    """Input: players - list containing dictionary with players name and score
              deck - list of dictionaries containing the playing cards values
       Function: full round of black jack for multiple players
       Output: list of dictionaries containing player name and hand"""
    def blackJack(self,players,deck):
        #Initalize
        deck = cards.shuffle(deck) #Shuffle cards
        deck = cards.shuffle(deck) #Shuffle cards
        names = list({p['Name'] for p in players}) #Find names of players
        table = self.setTable(names) #Set table for players

        #Deal inital hand
        dealer = []
        for x in range(2):
            for player in table:
                deck,player['Hand'] = self.dealHand(deck,player['Hand']) #Deal card to players
            deck,dealer = self.dealHand(deck,dealer) #Deal card to dealer

        #Deal for players
        i = 0
        bets = []
        while i < len(table):
            pBets = [x['Name'] for x in bets] #List of all players who have placed a bet
            if table[i]['Name'] not in pBets:
                pi = [players.index(a) for a in players if a['Name'] == table[i]['Name']][0] #Player score index
                p = players[pi] #Return player from player bank
                players[pi],bet = self.makeBet(p) #Make bet for player
                bets.append({'Name':table[i]['Name'],'Amount':bet})
            print('\nDealers Hand')
            print('{}\n'.format(pd.DataFrame(dealer).head(1))) #Show one of dealers cards
            pt = cards.calcTotal(table[i]['Hand'])
            print("It's {}'s turn to play.\n".format(table[i]['Name']))
            print(pd.DataFrame(table[i]['Hand']))
            while pt < 21:
                if len(table[i]['Hand']) == 2 and table[i]['Hand'][0]['Value'] == table[i]['Hand'][1]['Value']: #Split only alowed when first turn and same cards delt
                    userinput = input('\nWhat would you like to do? (Hit/Stay/Double/Surrender/Split)\n')
                else:
                    userinput = input('\nWhat would you like to do? (Hit/Stay/Double/Surrender)\n')
                if userinput.upper() == 'HIT':
                    deck,table[i]['Hand'] = self.dealHand(deck,table[i]['Hand'])
                    pt = cards.calcTotal(table[i]['Hand'])
                    print('\n{}'.format(pd.DataFrame(table[i]['Hand'])))
                elif userinput.upper() == 'STAY':
                    print()
                    break
                elif userinput.upper() == 'DOUBLE': #Double inital bet and take card as last card
                    pi = [players.index(a) for a in players if a['Name'] == table[i]['Name']][0] #Player score index
                    p = players[pi] #Return player from player bank
                    bi = [bets.index(a) for a in bets if a['Name'] == player['Name']][0] #Player bet index
                    b = bets[bi] #Return player from bet bank
                    players[pi],bet = self.makeBet(p,bet=b['Amount']) #Make bet for player
                    bets[bi]['Amount'] = bets[bi]['Amount'] + bet
                    deck,table[i]['Hand'] = self.dealHand(deck,table[i]['Hand'])
                    print('{}\n'.format(pd.DataFrame(table[i]['Hand'])))
                    break
                elif userinput.upper() == 'SURRENDER':
                    table[i]['Hand'] = [{'Suit':'Special','Value':999}]
                    print()
                    break
                elif userinput.upper() == 'SPLIT' and len(table[i]['Hand']) == 2 and table[i]['Hand'][0]['Value'] == table[i]['Hand'][1]['Value']:
                    for x,card in enumerate(table[i]['Hand']):
                        table.insert(i+x+1,{'Name':'{}-{}'.format(table[i]['Name'],x+1),'Hand':[card]})
                        bi = [bets.index(a) for a in bets if a['Name'] == table[i]['Name']][0] #Player bet index
                        b = bets[bi] #Return player from bet bank
                        bets.insert(i+x+1,{'Name':'{}-{}'.format(table[i]['Name'],x+1),'Amount':b['Amount']/2})
                    del table[i]
                    i = i - 1
                    break
                else:
                    print('Sorry that is not a command\n')
            i = i + 1

        #Deal for dealer
        check = [True for a in table if cards.calcTotal(a['Hand']) > 21] #Check to make sure all players didn't bust
        if len(check) != len(table):
            print('Dealers Hand')
            print('{}\n'.format(pd.DataFrame(dealer)))
            dt = cards.calcTotal(dealer)
            while dt < 17:
                deck,dealer = self.dealHand(deck,dealer)
                print('Dealers Hand')
                print('{}\n'.format(pd.DataFrame(dealer)))
                dt = cards.calcTotal(dealer)

        #Determine which players won
        for player in table:
            win = False
            pt = cards.calcTotal(player['Hand'])
            if pt == 999:
                win = True #Even though player lost set to true
                print('{} SURRENDERED DEALER WINS'.format(player['Name'].upper()))
            elif pt > 21:
                print('BUST {} LOSES DEALER WINS'.format(player['Name'].upper()))
            elif pt == 21:
                win = True
                print('21 {} WINS'.format(player['Name'].upper()))
            elif dt > 21:
                win = True
                print('DEALER BUSTED {} WINS'.format(player['Name'].upper()))
            elif dt > pt:
                print('{} LOSES DEALER WINS'.format(player['Name'].upper()))
            elif dt == pt:
                print('PUSH {} LOSES DEALER WINS'.format(player['Name'].upper()))
            elif dt < pt and pt < 21:
                win = True
                print('{} WINS'.format(player['Name'].upper()))
            if win == True:
                pi = [players.index(a) for a in players if a['Name'] == player['Name']] #Player score index
                if len(pi) > 0:
                    pi = pi[0]
                else:
                    pi = [players.index(a) for a in players if a['Name'] == player['Name'].split('-')[0]][0] #Player score index
                p = players[pi] #Return player from player bank
                bi = [bets.index(a) for a in bets if a['Name'] == player['Name']][0] #Player bet index
                b = bets[bi] #Return player from bet bank
                if pt == 999:
                    p['Score'] = p['Score'] + (b['Amount']/2) #When you surrender you get half your bet back
                else:
                    p['Score'] = p['Score'] + (b['Amount']*2)
        return players
