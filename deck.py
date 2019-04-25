import random
class Deck:

    '''
    
    A deck of card can be created using start value, end value, and the number of suit. This class object is used in
    NotFreeCell to construct a deck for the game.
    
    '''

    def __init__(self, start_value, end_value, number_of_suit):

        '''
        ---------
        Propose
        ---------
        Create a list to hold all the cards in the deck

        ---------
        Algorithm
        ---------
        1. Use slicing to get the indices of the values
        2. If using less than 4 suits to create a deck, randomly choose the desired number of suits
        3. Combine suit and value together to create a card
        4. Add all the cards to the list


        '''


        self.deck = []
        suit = ['S', 'H', 'D', 'C']
        value = ['A'] + list(map(str, range(2,11))) + ['J', 'Q', 'K']
        self.card_colour = ['R', 'B']
        self.start = start_value
        self.end = end_value
        self.n = number_of_suit
        self.suit = random.sample(suit, self.n)
        self.value = value[self.start-1:self.end]


        # algorithm 3
        for s in self.suit:
            for n in self.value:
                card = n + s
                self.deck.append(card)

    def __str__(self):
        return str(self.deck)

    def __len__(self):
        return len(self.deck)

    def is_in_deck(self, card):

        '''
        ---------
        Propose
        ---------
        Check if the card is in the deck

        '''

        if card in self.deck:
            return True
        else:
            return False

    def shuffle(self):

        '''
        ---------
        Propose
        ---------
        Randomly shuffle the deck

        '''

        random.shuffle(self.deck)

    def add_card(self, card):
        '''
        ---------
        Propose
        ---------
        Add a card to the end of the deck

        '''
        return self.deck.append(card)

    def draw_card(self):

        '''
        ---------
        Propose
        ---------
        Draw the last card in the deck

        '''

        self.deck.pop()

    def get_card_from_deck(self, index1, index2):
        return self.deck[index1:index2]
