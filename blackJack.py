import itertools
import random

class Card:
    def __init__(self, value, symbol):
        self.symbol = value
        self.suit = symbol

    def __repr__(self):
        return self.symbol + self.suit

class Deck:
    
    def __init__(self, sequence = None, suits = None):
        self.cards = []
        if (sequence is None):
            self.sequence = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        else:
            self.sequence = sequence

        if(suits is None):
            self.suits = ['♣','♦','♠','♥']
        else:
            self.symbols = symbols

        for i in itertools.product(self.suits,self.sequence):
            self.cards.append(Card(i[1],i[0]))

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        pass

    def getCards(self, amount):
        hand = []
        for x in range(amount):
            hand.append(self.cards.pop(0))
        return hand

    def showCards(self):
        print(self.cards)

#class BlackJack:
d = Deck()
d.showCards()
d.shuffle()
d.showCards()
print(d.__dict__)
