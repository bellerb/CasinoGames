from playingCards import cards
from cardGames import games

players = [{'Name':'Ben','Score':0}]
deck = cards.deck()
games().blackJack(players,deck)
