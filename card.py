class Card:

    '''
    Create a set of card with 52 cards to be used in the NotFreeCell game. 
    '''

    suit = ['S', 'H', 'D', 'C']
    value = ['A'] + list(map(str, range(2,11))) + ['J', 'Q', 'K']
    value_map = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, card):
        self.card = card

    def card_suit(self):

        '''
        ---------
        Propose
        ---------
        To get the suit of the card

        ----------
        Algorithm
        ----------
        1. Turn object into string for indexing
        2. Determine if the card has a real value

        '''

        card = str(self.card)
        if not self.is_empty_string():
            suit = card[1]
            return suit
        else:
            return ''

    def card_colour(self):

        '''
        ---------
        Propose
        ---------
        To get the colour of the card

        ----------
        Algorithm
        ----------
        1. Turn object into string for indexing
        2. Map the colour to the suits accordingly

        '''

        card = str(self.card)

        colours = ['R', 'B']
        if not self.is_empty_string():

            if card[1] == 'H' or card[1] == 'C':
                card_colour = colours[0]

                return card_colour

            elif card[1] == 'S' or card[1] == 'D':
                card_colour = colours[1]

                return card_colour
        else:
            return ''

    def card_face(self):

        '''
        ---------
        Propose
        ---------
        To get the value of the card

        ----------
        Algorithm
        ----------
        1. Turn object into string for indexing
        2. Map non-numeric values to the numerical values
        3. Turn string into integer

        '''

        card = str(self.card)

        if not self.is_empty_string():
            value = card[0]
            # algorithm 2, 3
            if value in self.value_map.keys():
                value = self.value_map[value]
            return int(value)

        else:
            return ''

    def get_previous_card(self):

        '''
        ---------
        Propose
        ---------
        To get the value of the card

        ----------
        Algorithm
        ----------
        1. Turn object into string for indexing
        2. Map non-numeric values to the numerical values
        3. Subtract 1 from the value to get the value from the previous card
        4. Map 1,11,12,13 back to A,J,Q,K
        5. Combine the value and suit to create a card except when the card is A, the previous card is ''

        '''

        card = str(self.card)
        value = card[0]
        suit = card[1]

        # algorithm 2
        if value in self.value_map.keys():
            v = self.value_map[value]

        # algorithm 3
        card_value = int(v) - 1
        if card_value == 0:
            previous_card = ''
            return previous_card

        # algorithm 4
        for k, v in self.value_map.items():
            if v == card_value:
                card_value = k

        previous_card = str(card_value) + suit

        return previous_card


    def get_card(self):
        return str(self.card)

    def is_empty_string(self):

        '''
        ---------
        Propose
        ---------
        Determine if card is an empty string

        '''
        card = str(self.card)
        if card == '':
            return True
        else:
            return False

    def __str__(self):
        return str(self.card)
