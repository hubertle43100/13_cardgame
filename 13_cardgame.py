import random

cardfaces = []
suits = ["Heart", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

for i in range(2,11):
    cardfaces.append(str(i))

for j in range(4):
    cardfaces.append(royals[j])

print(cardfaces)

for i in range(4):
    for j in range(13):
        cards = (cardfaces[j] + " / " + suits[i])
        deck.append(cards)

for c in range(52):
    print(deck[c])

random.shuffle(deck)
#created a deck for players to use all shuffled up (string)
