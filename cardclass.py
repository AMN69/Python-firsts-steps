import random
suits = ( 'Hearts', 
          'Diamonds', 
          'Spades', 
          'Clubs' )
ranks =( 'Two', 
          'Three', 
          'Four', 
          'Five', 
          'Six', 
          'Seven', 
          'Eigth', 
          'Nine', 
          'Ten', 
          'Jack', 
          'Queen', 
          'King', 
          'Ace' )
values = { 'Two': 2, 
           'Three': 3, 
           'Four': 4, 
           'Five': 5, 
           'Six': 6, 
           'Seven': 7,
           'Eigth': 8,
           'Nine': 9,
           'Ten': 10,
           'Jack': 11,
           'Queen': 12,
           'King': 13,
           'Ace': 14 }

class Card:

    def __init__(self, suit, rank):
      self.suit = suit
      self.rank = rank
      self.value = values[rank]

    def __str__(self):
      return self.rank + " of " + self.suit

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
       random.shuffle(self.all_cards) # doens't return anything. Makes it in place.

    def deal_one(self):
       return self.all_cards.pop() # remove one card off and return it

new_deck = Deck()
new_deck.shuffle()
print(new_deck.deal_one())
print(len(new_deck.all_cards))