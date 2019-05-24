"""
 * @file playingCards.py
 * @authors Ben Bellerose
 * @date May 23 2019
 * @modified May 23 2019
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
        values = [1,2,3,4,5,6,7,8,9,10]
        special = ['King','Queen','Jack']
        jokers = [{'Suit':'Special','Value':'Joker'}]*2

        #Creat numbered cards
        cards = []
        for s in suits:
            for v in values:
                cards.append({'Suit':s,'Value':v})
            for sv in special:
                cards.append({'Suit':s,'Value':sv})

        #Add jokers to the deck
        if len(arg) > 0:
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
