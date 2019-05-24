"""
 * @file playingCards.py
 * @authors Ben Bellerose
 * @date May 23 2019
 * @modified May 24 2019
 * @modifiedby BB
 * @brief class with useful playing card functions for creating card games
 */
 """
import random
import pandas as pd

class cards():
    """Input: none
      Function: cards in a playing deck
      Output: list of dictionaries containing playing cards"""
    def deck(**arg):
        suits = ['Spade','Club','Diamonds','Hearts']
        values = [2,3,4,5,6,7,8,9,10]
        special = ['King','Queen','Jack','Ace']
        jokers = [{'Suit':'Special','Value':'Joker'}]*2

        #Creat numbered cards
        cards = []
        for s in suits:
            for v in values:
                cards.append({'Suit':s,'Value':v})
            for sv in special:
                cards.append({'Suit':s,'Value':sv})

        #Add jokers to the deck
        if 'jokers' in arg:
            if arg['jokers'] == True:
                for j in jokers:
                    cards.append(j)
        return cards

    """Input: deck - list containing dictionary with card values
      Function: shuffle playing card deck
      Output: list of dictionaries containing playing cards"""
    def shuffle(deck):
        random.shuffle(deck)
        return deck

    """Input: hand - list containing dictionaries of playing cards
       Function: determine the total value of the cards in players hand
       Output: integer containing value of player hand"""
    def calcTotal(hand):
        values = []
        for card in hand:
            if card['Value'] == 'King' or card['Value'] == 'Queen' or card['Value'] == 'Jack':
                value = 10
            elif card['Value'] == 'Ace':
                value = 11
            else:
                value = int(card['Value'])
            values.append(value)
        total = sum(values)
        return total
