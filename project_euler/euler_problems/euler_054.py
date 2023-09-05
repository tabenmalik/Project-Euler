import os




class Card:
    def __init__(self, card_str):
        self.card_str = card_str
        value = card_str[:-1]
        suit = card_str[-1]

        if value == 'T':
            value = 10
        elif value == 'J':
            value = 11
        elif value == 'Q':
            value = 12
        elif value == 'K':
            value = 13
        elif value == 'A':
            value = 14
        else:
            value = int(value)

        self.value = value
        self.suit = suit

    def __str__(self):
        return 'Card({})'.format(self.card_str)

    def __repr__(self):
        return str(self)


class Hand:
    def __init__(self, cards):
        if isinstance(cards, str):
            cards = tuple(map(Card, cards.strip().split(' ')))
        elif isinstance(cards[0], str):
            self.cards = tuple(map(Card, cards))
        else:
            self.cards = tuple(cards)

        card_ranks = [(Hand.find_royal_flush,    10), 
                      (Hand.find_straight_flush,  9),
                      (Hand.find_four_of_a_kind,  8),
                      (Hand.find_full_house,      7),
                      (Hand.find_flush,           6),
                      (Hand.find_straight,        5),
                      (Hand.find_three_of_a_kind, 4),
                      (Hand.find_two_pairs,       3),
                      (Hand.find_one_pair,        2),
                      (Hand.find_high_card,       1)]

        for rank_finder, rank in card_ranks:
            rank_cards, rank_value = rank_finder(self)

            if rank_cards is not None:
                self.rank = rank
                self.rank_value = rank_value
                self.rank_cards = rank_cards
                break    

    def card_values(self):
        return (card.value for card in self.cards)

    def card_suits(self):
        return (card.suit for card in self.cards)

    def beats(self, right_hand):
        if self.rank > right_hand.rank:
            return True
        elif self.rank < right_hand.rank:
            return False
        elif self.rank_value > right_hand.rank_value:
            return True
        elif self.rank_value < right_hand.rank_value:
            return False
        else:
            for value_1, value_2 in reversed(list(zip(sorted(self.card_values()), sorted(right_hand.card_values())))):
                if value_1 > value_2:
                    return True
                elif value_1 < value_2:
                    return False

    def rank_str(self):
        if self.rank == 10:
            return 'Royal Flush'
        elif self.rank == 9:
            return 'Straight Flush'
        elif self.rank == 8:
            return 'Four of a Kind'
        elif self.rank == 7:
            return 'Full House'
        elif self.rank == 6:
            return 'Flush'
        elif self.rank == 5:
            return 'Straight'
        elif self.rank == 4:
            return 'Three of a Kind'
        elif self.rank == 3:
            return 'Two Pairs'
        elif self.rank == 2:
            return 'One Pair'
        elif self.rank == 1:
            return 'High Card'

    def __iter__(self):
        return iter(self.cards)

    def __str__(self):
        return str(self.cards) + ', ' + str(self.rank_cards) + ', ' + self.rank_str() + ', ' + str(self.rank_value)

    def __repr__(self):
        return str(self)

    @staticmethod
    def find_royal_flush(hand):
        straight_flush, value = Hand.find_straight_flush(hand)
        
        if straight_flush is None:
            return None, None

        if max(hand.card_values()) == 14:
            return straight_flush, value

        return None, None

    @staticmethod
    def find_straight_flush(hand):
        straight, value = Hand.find_straight(hand)
        if straight is None:
            return None, None

        if len(set(hand.card_suits())) == 1:
            return straight, value

        return None, None

    @staticmethod
    def find_four_of_a_kind(hand):
        unique_card_values = set(hand.card_values())
        if len(unique_card_values) != 2:
            return None, None
        
        for unique_value in unique_card_values:
            cards = tuple(card for card in hand.cards if card.value == unique_value)
            if len(cards) == 4:
                return cards, cards[0].value

        return None, None
        

    @staticmethod
    def find_full_house(hand):
        three_of_a_kind, value1 = Hand.find_three_of_a_kind(hand)
        
        if three_of_a_kind is None:
            return None, None

        small_hand = list(hand.cards)
        small_hand.remove(three_of_a_kind[0])
        small_hand.remove(three_of_a_kind[1])
        small_hand.remove(three_of_a_kind[2])
        pair, value2 = Hand.find_one_pair(Hand(small_hand))

        if pair is None:
            return None, None

        return hand.cards, value1*3 + value2*2

    @staticmethod
    def find_flush(hand):
        if len(set(hand.card_suits())) == 1:
            return hand.cards, max(hand.card_values())
        return None, None

    @staticmethod
    def find_straight(hand):
        cards = sorted(hand.cards, key=lambda x: x.value)

        diffs = [card1.value - card2.value for card1, card2 in zip(cards[:-1], cards[1:])]

        if set(diffs) == {-1}:
            return cards, cards[-1].value

        return None, None

    @staticmethod
    def find_three_of_a_kind(hand):
        three_of_kinds = []
        for i, card1 in enumerate(hand.cards):
            for j, card2 in enumerate(hand.cards[i+1:], start=i+1):
                for card3 in hand.cards[j+1:]:
                    if card1.value == card2.value == card3.value:
                        three_of_kinds.append((card1, card2, card3))

        if len(three_of_kinds) < 1:
            return None, None

        three_of_kinds = sorted(three_of_kinds, key=lambda x: x[0].value)

        return three_of_kinds[0], three_of_kinds[0][0].value

    @staticmethod
    def find_two_pairs(hand):
        pairs = []
        for i, card1 in enumerate(hand.cards):
            for card2 in hand.cards[i+1:]:
                if card1.value == card2.value:
                    pairs.append((card1, card2))

        if len(pairs) < 2:
            return None, None

        pairs = sorted(pairs, key=lambda x: x[0].value)

        return pairs[:2], pairs[0][0].value

    @staticmethod
    def find_one_pair(hand):
        pairs = []
        for i, card1 in enumerate(hand.cards):
            for card2 in hand.cards[i+1:]:
                if card1.value == card2.value:
                    pairs.append((card1, card2))

        if len(pairs) < 1:
            return None, None

        max_pair = pairs[0]
        for pair in pairs:
            if pair[0].value > max_pair[0].value:
                max_pair = pair

        return max_pair, max_pair[0].value

    @staticmethod
    def find_high_card(hand):
        max_card = max(hand, key=lambda x: x.value)

        return (max_card,), max_card.value



def read_file():
    this_dir, _ = os.path.split(__file__)
    
    players_hands = []
    with open(os.path.join(this_dir, 'euler_054.txt')) as fhdl:
        for line in fhdl:
            cards = list(map(Card, line.strip().split(' ')))
            players_hands.append((Hand(cards[:5]), Hand(cards[5:])))

    return players_hands

def solve():
    hands = read_file()
    hands = list(filter(lambda x: x[0].beats(x[1]), hands))

    return str(len(hands))

