from enum import Enum


class Suite(Enum):
    Spades = 0
    Clubs = 1
    Diamonds = 2
    Hearts = 3


class FaceValue(Enum):
    Ace = 0
    Two = 1
    Three = 2
    Four = 3
    Five = 4
    Six = 5
    Seven = 6
    Eight = 7
    Nine = 8
    Ten = 9
    Jack = 10
    Queen = 11
    King = 12


class CardDeck:
    def __init__(self, standardDeckCount: int):
        self.StandardDeckCount = standardDeckCount
        pass


class Card:
    def __init__(self, suite, faceValue):
        self.Suite = suite
        self.FaceValue = faceValue
