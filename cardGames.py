"""
 * @file cardGames.py
 * @authors Ben Bellerose
 * @date May 23 2019
 * @modified May 23 2019
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
       Output: list of dictionaries containing player name and hand"""
    def dealHand(self,deck,hand):
        if len(deck) > 0:
            hand.append(deck[0])
            del deck[0]
        return [deck,hand]

    """Input: hand - list containing dictionaries of playing cards
       Function: determine the total value of the cards in players hand
       Output: integer containing value of player hand"""
    def calcTotal(self,hand):
        values = []
        for card in hand:
            if card['Value'] == 'King' or card['Value'] == 'Queen' or card['Value'] == 'Jack':
                value = 10
            else:
                value = int(card['Value'])
            values.append(value)
        total = sum(values)
        return total

    """Input: players - list containing dictionary with player name and score
              deck - list of dictionaries containing the playing cards values
       Function: full round of black jack
       Output: list of dictionaries containing player name and hand"""
    def blackJack(self,players,deck):
        #Initalize
        deck = cards.shuffle(deck)
        names = list({p['Name'] for p in players}) #Find names of players
        table = self.setTable(names)

        #Deal inital hand
        for x in range(2):
            for player in table:
                deck,player['Hand'] = self.dealHand(deck,player['Hand'])

        #Ask player what they want to do
        options = ['HIT','STAY']
        for player in table:
            pt = self.calcTotal(player['Hand'])
            print("It is {}'s turn to play.\n".format(player['Name']))
            print(pd.DataFrame(player['Hand']))
            print('Total hand value = {}\n'.format(pt))
            while pt <= 21:
                userinput = input('What would you like to do? (Hit/Stay)\n')
                if userinput.upper() == 'HIT':
                    deck,player['Hand'] = self.dealHand(deck,player['Hand'])
                    pt = self.calcTotal(player['Hand'])
                    print(pd.DataFrame(player['Hand']))
                    print('Total hand value = {}\n'.format(pt))
                if userinput.upper() == 'STAY':
                    break
        return players
