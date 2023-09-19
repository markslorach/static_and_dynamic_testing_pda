import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 2)
        self.card3 = Card("Diamonds", 3)
   
    def test_check_for_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))
        self.assertEqual(False, CardGame.check_for_ace(self, self.card2))
        self.assertEqual(False, CardGame.check_for_ace(self, self.card3))
        
    def test_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))
        self.assertEqual(self.card3, CardGame.highest_card(self, self.card2, self.card3))
        self.assertEqual(self.card3, CardGame.highest_card(self, self.card1, self.card3))

    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3]
        self.assertEqual("You have a total of 6", CardGame.cards_total(self, cards))
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 3", CardGame.cards_total(self, cards))
        cards = [self.card1]
        self.assertEqual("You have a total of 1", CardGame.cards_total(self, cards))
        cards = []
        self.assertEqual("You have a total of 0", CardGame.cards_total(self, cards))