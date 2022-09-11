"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck, Card


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the rank that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        A flush is five cards with the same suit.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_xofsamerank(self, x):
        """Returns True if the hand has at least x cards of the same rank, False otherwise.
        A pair is two cards with the same rank.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= x:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
        A pair is two cards with the same rank.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_xofsamerank(2)

    def has_twopair(self):
        """Returns True if the hand has a two pair, False otherwise.
        A two pair is two pairs of cards in which each card has the same rank as its partner.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        num_pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                num_pairs += 1
        return num_pairs >= 2

    def has_threeofakind(self):
        """Returns True if the hand has three of a kind, False otherwise.
        Three of a kind is three cards with the same rank.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_xofsamerank(3)

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.
        A straight is five cards with ranks in a sequence; aces can be high or low but the sequence is not cyclical,
        i.e. Queen-King-Ace-2-3 is not allowed.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        ranks = sorted(self.ranks.keys())

        # 1 represents 'A'; 'A' can either be chosen to be at the end or at the beginning, so for finding a sequence of
        # five, 'A' is put at the beginning and the end
        if 1 in ranks:
            ranks.append(14)

        for idx, rank in enumerate(ranks):
            sequence = ranks[idx: idx+5]
            straight = [rank+i for i in range(5)]

            if sequence == straight:
                return True

        return False

    def has_fullhouse(self):
        """Returns True if the hand has a full house, False otherwise.
        A full house has three cards with one rank, two cards with another.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()

        three_ofakind, two_ofakind = (False,) * 2

        for freq in self.ranks.values():
            if freq >= 3 and not three_ofakind:
                three_ofakind = True

            elif freq >= 2:
                two_ofakind = True

            if two_ofakind == three_ofakind == True:
                return True

        return False

    def has_fourofakind(self):
        """Returns True if the hand has four of a kind, False otherwise.
        Four of a kind is four cards with the same rank.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_xofsamerank(4)

    def rank_to_suit(self):
        """Creates a dictionary mapping each rank to suits of cards that have that rank.

        Stores the result in attribute rank_suit.
        """
        self.rank_suit = {}
        for card in self.cards:
            self.rank_suit[card.rank] = self.rank_suit.get(card.rank, ()) + (card.suit,)

    def has_straightflush(self):
        """Returns True if the hand has a straight flush, False otherwise.
        A straight is five cards with ranks in a sequence and in the same suit; aces can be high or low but the
        sequence is not cyclical, i.e. Queen-King-Ace-2-3 is not allowed.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_to_suit()

        self.rank_hist()
        ranks = sorted(self.ranks.keys())

        # 1 represents 'A'; 'A' can either be chosen to be at the end or at the beginning, so for finding a sequence of
        # five, 'A' is put at the beginning and the end
        if 1 in ranks:
            ranks.append(14)

        for idx, rank in enumerate(ranks):
            sequence = ranks[idx: idx+5]
            straight = [rank+i for i in range(5)]

            if sequence == straight:

                for suit in range(4):

                    flush = True
                    for rank in sequence:

                        if not suit in self.rank_suit[rank]:
                            flush = False
                            break

                    if flush:
                        return True

        return False

    def classify(self):
        """Computes the highest-value classification of the hand and sets the label attribute accordingly."""

        if self.has_straightflush():
            self.label = 'Straight flush'

        elif self.has_fourofakind():
            self.label = 'Four of a kind'

        elif self.has_fullhouse():
            self.label = 'Full house'

        elif self.has_flush():
            self.label = 'Flush'

        elif self.has_straight():
            self.label = 'Straight'

        elif self.has_threeofakind():
            self.label = 'Three of a kind'

        elif self.has_twopair():
            self.label = 'Two pair'

        elif self.has_pair():
            self.label = 'Pair'

def estimate_prob(num_decks: int):
    """Shuffles a deck of cards, divides it into poker hands, classifies the hands and count the number of times
    various classifications appear, then adds the result to a histogram. Does this for num_decks decks."""

    classification_histogram = {
        'Straight flush': 0,
        'Four of a kind': 0,
        'Full house': 0,
        'Flush': 0,
        'Straight': 0,
        'Three of a kind': 0,
        'Two pair': 0,
        'Pair': 0,
        '': 0,
    }

    hands_classified = 0
    for i in range(num_decks):
        deck = Deck()
        deck.shuffle()

        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)

            hand.classify()
            classification_histogram[hand.label] = classification_histogram.get(hand.label) + 1

            hands_classified += 1

    for classification in classification_histogram.keys():
        classification_histogram[classification] = f'{classification_histogram.get(classification) / hands_classified * 100} %'

    print(classification_histogram)

if __name__ == '__main__':
    # make a deck
    # deck = Deck()
    # deck.shuffle()
    #
    # card_list = [Card(2, 1), Card(3, 2), Card(3, 2), Card(3, 4), Card(3, 5)]
    # hand = PokerHand()
    # hand.cards = card_list
    # hand.classify()

    estimate_prob(1)


    # # deal the cards and classify the hands
    # for i in range(7):
    #     deck = Deck()
    #     deck.shuffle()
    #
    #     hand = PokerHand()
    #     deck.move_cards(hand, 7)
    #     hand.sort()
    #
    #     # print(hand)
    #     # print(hand.has_flush())
    #     # print(hand.has_pair())
    #     # print('')
    #
    #     if hand.has_straight():
    #         print(hand)
    #         break

    # print(hand.suits)
    # hand.rank_hist()
    # print(hand.ranks)