from enum import Enum


class Suite(Enum):
    Spades, Clubs, Diamonds, Hearts


class FaceValue(Enum):
    Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King


class CardDeck:
    def __init__(self, standardDeckCount):
        self.StandardDeckCount = standardDeckCount
        pass


class Card:
    def __init__(self, suite, faceValue):
        self.Suite = suite
        self.FaceValue = faceValue
