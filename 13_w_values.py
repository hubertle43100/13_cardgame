#class cards:
    #def __init__(self, value, suit):
        #self.value = value
        #self.suit = suit

#card1 = cards(6, "diamond")
#print(card1.value, card1.suit)

#card2 = ["A", "heart"]
#print(card2)

cardfaces = []
suits = [0.1, 0.2, 0.3, 0.4] #Suits in order respectively ['spades', 'clubs', 'diamonds', 'hearts']
deck = []
words = []

for i in range (3,16):
    cardfaces.append(float(i))

for i in range(4):
    for j in range(13):
        cards = (cardfaces[j] + suits[i])
        deck.append(cards)

#for c in range(52):
    #print(deck[c])

#11.1 - 15.4 are all the Royals + 'A's + '2's (2 being the highest)


for c in range(52):
        if ((deck[c]-0.1)% 2 == 0 or (deck[c]-0.1)% 2 == 1 ): #doesn't work with 4.1
            print(deck[c], 'of spades')
        if ((deck[c]-0.2)% 2 == 0 or (deck[c]-0.2)% 2 == 1 ):
            print(deck[c], 'of clubs')
        if ((deck[c]-0.3)% 2 == 0 or (deck[c]-0.3)% 2 == 1 ):
            print(deck[c], 'of diamonds')
        if ((deck[c]-0.4)% 2 == 0 or (deck[c]-0.4)% 2 == 1 ):
            print(deck[c], 'of hearts')
