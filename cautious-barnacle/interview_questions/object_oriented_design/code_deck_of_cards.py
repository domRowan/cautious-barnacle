from enum import Enum


class Card:
    def __init__(self, suit, type):
        # Python will name mangle member variables which start with __
        self.__privateExample = False

        self.available = True
        self.suit = suit
        # Leave this undefined as the game dictates the value
        self.value = None
        self.type = type

    def setValue(self, value):
        raise NotImplementedError

    def getValue(self):
        raise NotImplementedError

    def getSuit(self):
        return self.suit

    def isAvailable(self):
        return self.available

    def setAvailable(self, value):
        self.available = value


class Deck(Card):
    def __init__(self, cards):
        self.cards = cards
        self.numberOfCardsDealt = 0

    def shuffle(self):
        raise NotImplementedError

    def dealHand(self, sizeOfHand):
        raise NotImplementedError

    def dealCard(self):
        raise NotImplementedError

    def remainingCards(self):
        return len(self.cards) - self.numberOfCardsDealt


class Hand(Card):
    def __init__(self, cards):
        self.cards = cards

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, card):
        # Remove
        # hash map with tuple of suit and number as key
        # value is count of that card in hand
        return

    def totalValue(self):
        total = 0
        for card in self.cards:
            total += card.getValue()

        return total


class Suit(Enum):
    clubs = 1
    hearts = 2
    spades = 3
    diamonds = 4


class BlackJackHand(Hand):
    # Return the highest possible score under 21
    # Return the lowest possible score if over 21
    def totalValue(self):
        # There is no Integer.Max in python
        maxCardValue = 11
        minOver = len(self.cards) * maxCardValue
        maxUnder = -1 * minOver

        for score in self.possibleScores():
            if (score > 21 and score < minOver):
                minOver = score
            elif (score <= 21 and score > maxUnder):
                maxUnder = score
        return minOver if (maxUnder == -1 * minOver) else maxUnder

    def possibleScores(self):
        # Calculate all possible scores
        return []

    def busted(self):
        return self.totalValue > 21

    def is21(self):
        return self.totalValue == 21

    def isBlackJack(self):
        return self.is21 and len(self.cards) == 2 and self.cards[("jack", Suit.spades)]


class BlackJackCard(Card):
    def setValue(self, value):
        raise NotImplementedError

    def getValue(self):
        if self.isAce():
            return 1
        elif self.isFaceCard():
            return 10
        else:
            return self.value

    def isAce(self):
        return self.type == "ace"

    def isFaceCard(self):
        return self.type == "jack"  # ... and so on
