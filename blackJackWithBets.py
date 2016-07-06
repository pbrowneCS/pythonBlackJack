# Required dependencies
from random import shuffle

# Deck of cards
class Card(object):
    def __init__(self, suit, value, image=None):
        self.suit = suit
        self.value = value
        self.image = image

class Deck(object):
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.deck = []
        self.buildDeck()

    def buildDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))
        self.shuffle()
        return self

    def shuffle(self):
        shuffle(self.deck)
        return self

    def deal(self):
        if self.deck: # empty lists return as False
            # removes and returns card from deck, shuffled or not
            return self.deck.pop()
        else:
            print "No more cards"

    def returnCard(self, card, reShuffle = False):
        self.deck.append(card)
        if reShuffle:
            self.shuffle()
        return self

    def resetDeck(self):
        self.deck = []
        self.buildDeck()
        return self

# get hand (2 cards)
# if hand > 21 AND card"1" in hand
    #card"1" points = 1 (changed from 11)
# if hand point total < 21
    #give player option "hit" / "stay"


#FUNCTIONS
def firstHands():
    draw = deck.deck.pop()
    player.append(draw.value)
    draw = deck.deck.pop()
    dealer.append(draw.value)
    draw = deck.deck.pop()
    player.append(draw.value)
    draw = deck.deck.pop()
    dealer.append(draw.value)
    faceCardCheck(player)
    faceCardCheck(dealer)
    aceCheck(player)
    aceCheck(dealer)

def playerHandCount(x):
    handSum = 0
    for c in range(len(x)):
        if x[c]=="j" or x[c]=="q" or x[c]=="k":
            x[c] = 10
        if x[c]=="a":
            x[c] = 1
        if x[c]=="A":
            x[c] = 11
    for i in range(len(x)):
        handSum += x[i]
    print "Your hand is:", x
    print "Your hand totals to:", handSum
    return handSum

def hit():
    draw = deck.deck.pop()
    player.append(draw.value)
    faceCardCheck(player)
    aceCheck(player)

def choiceCheck():
    global stayFlag
    global playerSum
    global dealerSum
    choice = raw_input("You gonna hit? Y / N")
    if choice == 'y':
        hit()
        playerSum = playerHandCount(player)
        dealerSum = dealerHandCount(dealer)
    else:
        stayFlag = True
        playerSum = playerHandCount(player)
        dealerSum = dealerHandCount(dealer)

def dealerHandCount(x):
    handSum = 0
    for c in range(len(x)):
        if x[c]=="j" or x[c]=="q" or x[c]=="k":
            x[c] = 10
        if x[c]=="a":
            x[c] = 1
        if x[c]=="A":
            x[c] = 11
    for i in range(len(x)):
        handSum += x[i]
    print "The Dealer's hand is:", x
    print "The Dealer's hand totals to:", handSum
    return handSum

def dealerHit():
    print "The dealer draws a card."
    draw = deck.deck.pop()
    dealer.append(draw.value)
    faceCardCheck(dealer)
    aceCheck(dealer)

def aceCheck(x):
    ace = -1
    sumC = 0
    for i in range(len(x)):
        if x[i]==1:
            ace = i
        sumC += x[i]
    if sumC<=11:    
        x[ace]="A"
    if sumC>21:
        x[ace]="a"


def faceCardCheck(x):
    for i in xrange(len(x)):
        if x[i]>9:
            x[i]=10

def keepPlaying():
    global playing
    choice = raw_input("Play another hand? Y/N")
    if choice != 'y':
        playing = False

#PLAYERS HERE
wallet = 200
bet = 5
playing = True
dealer = []
player = []
stayFlag = False
playerSum = 0
dealerSum = 0
#TABLE HERE
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A",2,3,4,5,6,7,8,9,10,"j","q","k"]
deck = Deck(suits, values)

#GAME HERE
deck.buildDeck()
deck.shuffle()
while playing:
    dealer = []
    player = []
    stayFlag = False
    print "Your wallet total is $", wallet
    firstHands()
    playerSum = playerHandCount(player)
    dealerSum = dealerHandCount(dealer)
    if playerSum == 21:
        print "BLACKJACK!!"
        stayFlag = True
    else:
        choiceCheck()
    while stayFlag == False:
        if playerSum == 21:
            stayFlag = True
            break
        if playerSum > 21 and 1 in player:
            playerSum - 10
        if playerSum > 21:
            print "Bust!!"
            wallet = wallet - bet
            break
        choiceCheck()
    while dealerSum < 17 and dealerSum <= 21 and playerSum < 22:
        dealerHit()
        dealerSum = dealerHandCount(dealer)
        if dealerSum > 21:
            print "Dealer Bust! YOU WIN!!"
            wallet = wallet + bet
    if dealerSum <= 21 and playerSum <= 21:
        if dealerSum > playerSum:
            print "Dealer Wins! YOU LOSE!!"
            wallet = wallet - bet
        if dealerSum == playerSum:
            print "It's a push!"
        if dealerSum < playerSum:
            print "You WIN!!"
            wallet = wallet + bet
    print "Player final score:", playerSum
    print "Dealer final score:", dealerSum
    print "Your wallet total is $", wallet
    print "\n"
    keepPlaying()
print "Thanks for playing!"