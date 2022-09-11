import random

# Exercise 18.1:

# I have done this on lined paper. However, I cannot find a solution so I don't know if is correct or not.


# Exercise 18.2:


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                        '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, number_hands: int, cards_per_hand: int) -> list:
        """Creates nHands Hand objects, deals cardsPerHand cards per hand, and returns a list of Hands."""

        hands_list = []
        for i in range(number_hands):
            h = Hand(label=f'Hand {i+1}')
            self.move_cards(h, cards_per_hand)
            hands_list.append(h)
        return hands_list


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

# d = Deck()
# hands_list1 = d.deal_hands(5, 2)
# for hand in hands_list1:
#     print(hand)


# Exercise 18.3