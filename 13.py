import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print "{} of {}".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range (3,16):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

deck = Deck()
deck.shuffle()

player_1 = Player("MOUSE")
print('\nMOUSE:')
for i in range(13):
    player_1.draw(deck)

player_1.showHand()

player_2 = Player("HORSE")
print('\nHORSE:')
for i in range(13):
    player_2.draw(deck)

player_2.showHand()

player_3 = Player("DRAGON")
print('\nDRAGON:')
for i in range(13):
    player_3.draw(deck)

player_3.showHand()

player_4 = Player("DOG")
print('\nDOG:')
for i in range(13):
    player_4.draw(deck)

player_4.showHand()

class play(object):
    pass
