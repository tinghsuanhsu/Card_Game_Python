from card import Card
from deck import Deck

class NotFreeCell:
    '''
    

    The game follows these rules:
    1. Only one card may be moved at a time.
    2. The four foundations must be built starting from the Ace of the appropriate suit, followed by the 2, then the 3 etc. until the King is placed.
    3. If a card is placed on a cascade, it must be placed of a card of the opposite colour, and of a suit that is one higher than itself.
    4. Any card may be placed in an empty cascade.
    5. Cards from the foundations may be placed back onto a cascade, or an empty cascade slot.
    6. Only one card at a time can occupy a cell slot.
    7. Victory is achieved when all four foundations are filled with their respective suits from Ace to King.
    8. A card can be placed into cascade by entering either the label name or the card which is desired to place on top of.
    9. A card can be placed into foundation and free cells by entering the label name.

    ---------------------------------------------------------------------------------------------------------------------
    Algorithm of the design:
    The program implements a dictionary of lists to keep track of all the cards. Each list has the fixed length and cards are accessed and
    replaced by using the exact location in the list. Since the cards are located by the index, a method 'locate' is used to search
    for the stack of which the card is in and then look for the index of the card in the stack. The game prints to screen by implementing
    transpose to the collection of stacks.
    ---------------------------------------------------------------------------------------------------------------------
    Global variables explained:
    1. stack_start_index: the starting index of the card in the stack
    ---------------------------------------------------------------------------------------------------------------------
    Class utilised:

    1. Card
    2. Deck

    Note: Any modification to these two packages will change the behaviour of this program.
    ---------------------------------------------------------------------------------------------------------------------

    '''

    stack_start_index = {
            '2': 1,
            '3' : 1,
            '4' : 1,
            '5': 1,
            '6': 4,
            '7' : 4,
            '8' : 4,
            '9' : 4,
            '10' : 4,
            '11' : 4,
            '12' : 4,
            '13' : 4,
            '14' : 1,
            '15' : 1,
            '16' : 1,
            '17' : 1,
        }

    def __init__(self, size, design = ''):

        '''
        ----------
        Algorithm
        ----------

        1. Initialise the object with a collection of empty lists
        2. Given the size, construct the board by adding empty strings to the list
        3. Place the labels in the board. Since all the lists will be transposed for printing outputs, the list index in the
           dictionary is the transposed of the displayed output. E.g. If a card's is displayed at [row3][column7] on the board,
           its actual index in the dictionary is [row7][column3]
        4. A card is created to represent the card playing on hand


        '''

        self.design = design
        self.card = Card('')
        self.size = size
        self.collection_of_stack = {str(i) : [] for i in range(0,20)}


        # algorithm 2, each stack in the board has a certain length (self.size)
        i = 0
        while i < self.size:
            for value in self.collection_of_stack.values():
                for n in range(self.size):
                    value.append(self.design)
                i += 1



    def populate_stack(self, stack_n, replacement):

        '''
        --------
        Purpose
        --------
        Populate the stack with a deck of card.

        ----------
        Algorithm
        ----------
        1. Use the stack index to find the stack
        2. After getting the stack, find the starting index of the placeholder for cards in each stack
        3. Replace the empty strings with the values in the replacement list

        '''
        for key, start_index in self.stack_start_index.items():
            if stack_n == key:
                for i, list_value in enumerate(replacement, start_index):
                    self.collection_of_stack[stack_n][i] = list_value


    def construct_board(self):

        '''
        --------
        Purpose
        --------
        Create a deck of 52 playing cards to be used in the game and display them on the board

        ----------
        Algorithm
        ----------
        1. Call Deck class to construct a deck
        2. Shuffle the card randomly
        3. Update the board with cards
        4. Assign labels to the board
        '''

        self.deck = Deck(1, 13, 4)
        self.deck.shuffle()

        # can change the get_card_from_deck arguments
        self.populate_stack('6', self.deck.get_card_from_deck(0, 6))
        self.populate_stack('7', self.deck.get_card_from_deck(7, 16))
        self.populate_stack('8', self.deck.get_card_from_deck(16, 25))
        self.populate_stack('9', self.deck.get_card_from_deck(25, 30))
        self.populate_stack('10', self.deck.get_card_from_deck(30, 36))
        self.populate_stack('11', self.deck.get_card_from_deck(36, 42))
        self.populate_stack('12', self.deck.get_card_from_deck(42, 47))
        self.populate_stack('13', self.deck.get_card_from_deck(47, 53))


        self.collection_of_stack['2'][0] = 'S1'
        self.collection_of_stack['3'][0] = 'S2'
        self.collection_of_stack['4'][0] = 'S3'
        self.collection_of_stack['5'][0] = 'S4'
        self.collection_of_stack['14'][0] = 'F1'
        self.collection_of_stack['15'][0] = 'F2'
        self.collection_of_stack['16'][0] = 'F3'
        self.collection_of_stack['17'][0] = 'F4'
        self.collection_of_stack['6'][3] = 'C1'
        self.collection_of_stack['7'][3] = 'C2'
        self.collection_of_stack['8'][3] = 'C3'
        self.collection_of_stack['9'][3] = 'C4'
        self.collection_of_stack['10'][3] = 'C5'
        self.collection_of_stack['11'][3] = 'C6'
        self.collection_of_stack['12'][3] = 'C7'
        self.collection_of_stack['13'][3] = 'C8'

    def start_game(self):

        '''
        --------
        Purpose
        --------
        Start the game.

        ----------
        Algorithm
        ----------
        1. Ask users if they want to play
        2. If so, construct a board. If not, quit the game.
        '''

        welcome_message = '{:^170}\n{:^170}\n{:^170}'.format('Welcome to NotFreeCell',
                                      'Are you ready to play?',
                                      '(Y/N)')

        response = input(welcome_message)
        acceptable = ['Y','y','yes','Yes','YES','N','n','no','NO']

        # check to see if user wants to quit
        while not self.is_quit(response):
            break

        while response not in acceptable:
                response = input('{:^170}\n'.format('Do you want to play?\n(Y/N)'))
                while not self.is_quit(response):
                    break

        if 'Y' in response or 'y' in response:
            self.construct_board()

        elif 'N' in response or 'n' in response:
            self.quit_game()



    def menu(self):

        '''
        --------
        Purpose
        --------
        Display menu

        '''

        return str('{:^170}\n'
                   '{:^170}\n\n'.format('You can quit at any time during the game.', 'q: quit game'))


    def is_quit(self, command):

        '''
        --------
        Purpose
        --------
        Check to see if the user input is a command


        ----------
        Algorithm
        ----------
        1. Compare with reference letter

        '''
        q = ['Q', 'q']
        if command.strip() in q:
            self.quit_game()
            return True
        else:
            return False


    def locate(self, target):

        '''
        --------
        Purpose
        --------
        Locate a card's stack index and card index in the stack. Both will be used as reference to update the board
        in update_stack function


        ----------
        Algorithm
        ----------
        1. Turn card object into a string for looping
        2. If so, construct a board. If not, quit the game.
        '''

        stack_index = ''

        t = target.__str__()

        for index, stack_list in self.collection_of_stack.items():
            if t in stack_list:
                stack_index = index
                card_index = stack_list.index(t)

                return stack_index, card_index


    def update_stack(self, stack_index, card_index, replacement):

        '''
        --------
        Purpose
        --------
        Replace a card in the board

        ----------
        Algorithm
        ----------
        1. Find the list in the dictionary
        2. Update the value at the given index in the list
        '''
        self.collection_of_stack[stack_index][card_index] = replacement


    def is_top_card(self, card, index = 1, value = ''):

        '''
        --------
        Purpose
        --------
        Check if a card is the topmost card in the stack by checking if the value of the next index is an empty string
        Use 2 different methods to check.

        1. Foundation or free cell:

        2. Cascade:

        ----------
        Algorithm
        ----------
        1. Get stack index
        2. Compare the card to the empty string

        '''

        freeslot_set = [str(x) for x in range(2, 6)]
        cascade_set = [str(x) for x in range(6, 14)]
        foundation_set = [str(x) for x in range(14, 18)]

        location = self.locate(card)
        # convert to integer for mathematical operation purpose
        stack_index = location[0]
        current_index = location[1]
        current_stack = self.collection_of_stack[stack_index]

        # if the card itself is not empty then it is the top card in foundation and cascade
        if stack_index in freeslot_set or stack_index in foundation_set:
            if card != value:
                return True
            else:
                return False

        # if the next card is empty then the card is the last card in that stack
        elif stack_index in cascade_set:
            if current_stack[int(current_index) + index] == value:
                return True
            else:
                return False

    def is_label(self, target):

        '''
        --------
        Purpose
        --------
        Determine if the target location is a label


        ----------
        Algorithm
        ----------
        1. Put all the stack lists into another list
        2. Transpose the board by using * to unpack the value in stack, then use zip to get a list of tuples
        2. Determine if the location is in the row that contains all the label names

        '''

        # algorithm 1
        matrix = []
        for stack in self.collection_of_stack.values():
            matrix.append(stack)

        # algorithm 2
        transposed = list(zip(*matrix))

        # algorithm 3
        if target in transposed[0] or target in transposed[3]:
            return True
        else:
            return False

    def is_cascade_label(self, target):

        '''
        --------
        Purpose
        --------
        Determine if the target location is a cascade label


        ----------
        Algorithm
        ----------
        1. Put all the stack lists into another list
        2. Transpose the board by using * to unpack the value in stack, then use zip to get a list of tuples
        2. Determine if the location is in the row that contains all the cascade label names

        '''

        # algorithm 1
        matrix = []
        for stack in self.collection_of_stack.values():
            matrix.append(stack)

        # algorithm 2
        transposed = list(zip(*matrix))

        # algorithm 3
        if target in transposed[3]:
            return True
        else:
            return False

    def move_card(self):

        '''
        --------
        Purpose
        --------
        Ask user for a card to move


        ----------
        Algorithm
        ----------
        1. Check to see if the input is a command
        2. Check to see if the input is in the board, either a label name or a card
        3. Check to see if the input is the topmost card in the stack
        4. Draw the card
        5. Update the index with the replacement (empty string or previous card)

        '''

        # used when draw a card
        replacement = ''

        card = input('{:^170}\n'.format('Which card do you want to move?'))
        card = card.upper()

        # check to see if user wants to quit
        while not self.is_quit(card):
            break

        # check to see if the card is in the deck before proceeding
        while not self.deck.is_in_deck(card):
            card = input('{:^170}\n'.format('Card not found. Try again.')).upper()
            while not self.is_quit(card):
                break

            # if the card is not the topmost card, ask for a new card
            while not self.is_top_card(card):
                card = input('{:^170}\n'.format('Please pick a card that is the topmost in the stack.')).upper()
                while not self.is_quit(card):
                    break

                # if the card is not in the board, ask for a new card
                while not self.deck.is_in_deck(card):
                    card = input('{:^170}\n'.format('Card not found. Try again.')).upper()
                    while not self.is_quit(card):
                        break

        # draw the card
        self.card = Card(card)
        location = self.locate(card)
        stack_index = location[0]
        target_index = location[1]
        target_stack = self.collection_of_stack[stack_index]


        # if a card drawn is in the foundation, after drawing the card, update the index with the previous one
        foundation_set = [x for x in range(14, 18)]
        current_card_in_place = Card(target_stack[target_index])
        if stack_index in foundation_set:
            replacement = current_card_in_place.get_previous_card()
            self.update_stack(stack_index, target_index, replacement)

        # after drawing the card, replace the card with empty string
        else:
            self.update_stack(stack_index, target_index, replacement)


    def place_card(self):

        '''
        --------
        Purpose
        --------
        Ask user for a location to place the card
        Can choose to place a card on top of another card in the cascade using the label name or the card name and place
        in a particular cell in foundation or free cells with label names


        ----------
        Algorithm
        ----------
        1. Check to see if the input is a command
        2. Check to see if the input is in the board, either a label name or a card
        3. Get the stack index to determine which section the target location is
        4. Call on methods that correspond to the target section

        '''

        freeslot_set = [str(x) for x in range(2, 6)]
        cascade_set = [str(x) for x in range(6, 14)]
        foundation_set = [str(x) for x in range(14, 18)]

        target = input('{:^170}\n\n{:^170}\n\n{:^170}\n\n'.format('Where do you want to move to?',
                       'Enter the label name for foundation and free cells',
                       'Or, enter the card you want to place on top of in the cascade'))

        # card or label
        target = target.upper()

        # check to see if user wants to quit
        while not self.is_quit(target):
           break

        # if the target location is not a card existing in the game or a label, ask for a new card
        while target == str(self.card):
            target = input('{:^170}'.format('This is the card you have right now.\nChoose another location')).upper()
            while not self.is_quit(target):
                break

            # check to see if the card the card is in the deck
            while not self.deck.is_in_deck(target):
                if self.is_label(target):
                    break
                else:
                    target = input('{:^170}'.format('Cannot place it there. Try again.\n')).upper()
                    while not self.is_quit(target):
                        break

        location = self.locate(target)
        stack_index = location[0]
        target_index = location[1]


        if stack_index in freeslot_set:
            self.freeslot(self.card.get_card(), stack_index, target_index)

        elif stack_index in cascade_set:
            if self.is_cascade_label(target):
                target_index = self.from_label_to_top(stack_index)
                self.cascade(self.card.get_card(), stack_index, target_index)
            else:
                self.cascade(self.card.get_card(), stack_index, target_index)

        elif stack_index in foundation_set:
            self.foundation(self.card.get_card(), stack_index, target_index)



    def freeslot(self, card, stack_index, target_index):

        '''
        --------
        Purpose
        --------
        Determine if the card can be placed in the free cells


        ----------
        Algorithm
        ----------
        1. Current index is the label. Add 1 to the index returned from the search to refer to the cell that holds the card
        2. Get the card's suit and value in target location
        3. If the card is empty : cell is not full
        4. Place the card
        5. Update the index with the replacement (empty string or previous card)

        '''

        # i : how many index the actual cell which holds the card is. can be changed based on design
        i  = 1
        target_index += i

        # see algorithm 2
        target_stack = self.collection_of_stack[stack_index]
        current_card_in_place = Card(target_stack[target_index])
        current_value = current_card_in_place.card_face()

        # empty string : cell is empty
        if current_value == '':
            self.update_stack(stack_index, target_index, card)

        # not empty string : cell is full
        elif current_value != '':
            print ('{:^170}\n'.format('You cannot add another card.'))
            self.place_card()



    def foundation(self, card, stack_index, target_index):

        '''
        --------
        Purpose
        --------
        Determine if the card can be placed in the foundation


        ----------
        Algorithm
        ----------
        1. Turn card in target cell into a Card object
        2. Get the suit and value from both the card on hand and card in the foundation cells
        3. Check to see if target cell is empty
        4. Check to see if the card on hand is Ace
        5. If both 2 and 3 are met then add the card to the cell
        6. If the card is not Ace and the cell has a card in it, only add card if value difference is 1 and same suit
        7. Update stack accordingly

        '''

        # i : how many index the actual cell which holds the card is. can be changed based on design
        i  = 1

        target_index += i
        suit = self.card.card_suit()
        value = self.card.card_face()

        target_stack = self.collection_of_stack[stack_index]
        current_card_in_place = Card(target_stack[target_index])

        # cell is empty
        if current_card_in_place.get_card() == '':
            # if the card value is Ace, add a card
            if value == 1:
                self.update_stack(stack_index, target_index, card)
                return True

            # not an Ace, ask for another location
            elif value != 1:
                print ('{:^170}\n'.format('You cannot add anything other than an Ace'))
                self.place_card()

        # see algorithm 6
        elif current_card_in_place.get_card() != '':
            current_value = current_card_in_place.card_face()
            current_suit = current_card_in_place.card_suit()

            if not ((value - current_value == 1) and (current_suit == suit)):
                print ('{:^170}\n'.format('You cannot add a card here'))
                self.place_card()

            elif current_value == 13:
                print ('{:^170}\n'.format('This stack is full. Choose another location.'))
                self.place_card()

            else:
                self.update_stack(stack_index, target_index, card)



    def from_label_to_top(self, stack_index):

        '''
        --------
        Purpose
        --------
        Search for the location of the topmost card in the cascade when given a cascade stack index


        ----------
        Algorithm
        ----------
        1. Loop through cascade list to get the empty string index
        2. Each cascade label is designed to have 3 empty strings before the label and therefore the 4th occurrence of an empty
           string is 1 index after the card in place if any. Thus, subtract 1 from the empty cell index to get the index of
           the topmost card

        '''

        target_stack = self.collection_of_stack[stack_index]
        # algorithm 2 and 3
        total_n = [i for i, x in enumerate(target_stack) if x == '']
        top_index = int(total_n[3]) - 1

        return top_index



    def cascade(self, card, stack_index, target_index):

        '''
        --------
        Purpose
        --------
        Determine if the card can be placed in the cascade


        ----------
        Algorithm
        ----------
        1. Turn card in target cell into a Card object
        2. Get the suit and value from both the card on hand and card in the cascade cells
        3. Check to see if target cell is empty
        4. If target cell has a card, only add if the card on hand has the opposite colour and is 1 value less than
           the card in the cell
        5. Update stack accordingly

        '''

        # i : how many index the actual cell which holds the card is. can be changed based on design
        i = 1

        current_index = target_index
        target_index += i
        value = self.card.card_face()
        colour = self.card.card_colour()

        # algorithm 1
        target_stack = self.collection_of_stack[stack_index]
        current_card_in_place = Card(target_stack[current_index])

        # algorithm 3
        if current_card_in_place.get_card() == '':
            self.update_stack(stack_index, target_index, card)

        # algorithm 4
        elif current_card_in_place.get_card() != '':
            current_value = current_card_in_place.card_face()
            current_colour = current_card_in_place.card_colour()

            if (current_value - value == 1) and (current_colour != colour):
                self.update_stack(stack_index, target_index, card)
                return True

            else:
                print ('{:^170}'.format('Please choose another cell'))
                self.place_card()

    def update_card_on_hand(self):

        '''
        --------
        Purpose
        --------
        Update the current card to empty string if the card on hand has been placed successfully

        '''

        self.card = ''
        return self.card


    def quit_game(self):

        print ('{:^170}'.format('See you.'))
        quit()


    def win(self, value = 13):

        '''
        --------
        Purpose
        --------
        Determine if user win the game


        ----------
        Algorithm
        ----------
        1. Turn all the cards in foundation into Card objects to get card value
        2. Evaluate the last location in each cascade: if empty then there are no cards are in the cell
        3. Win when all the card in foundation set has a value K and all cells in cascade are empty
        4. Default card value is K, can be changed based on design

        '''

        # cascade stack index
        for x in range(14, 18):

            # use the below code for test.win() function when testing win.()
            # if (Card(self.collection_of_stack[self.index_to_stack[x]][1]).card_face())== value:
            if (Card(self.collection_of_stack[str(x)][1]).card_face() == value and
                (self.collection_of_stack[str(int(x)-8)][5] == '')):

                print('{:^170}\n'.format('You win!'))
                return True

        # choice = input('Congratulations! Do you want to play again?\n'
        #                ' Yes, No, Menu')
        # if choice

    '''
    ---------------------------------------------------------------------------------------------------------------------
    Methods below are for displaying board:
    ---------------------------------------------------------------------------------------------------------------------
    '''

    def add_linebreak(self, stack, index1, index2 = None, linetype = '|'):

        '''
        --------
        Purpose
        --------
        Add line break to the labels for display. Does not change the board


        ----------
        Algorithm
        ----------
        1. Take a list of indices and insert the linetype to the location
        2. Default argument index2 is set to None: function can operate on 1 or 2 list of indices

        '''

        #algoithm 1
        for n in index1:
            stack.insert(n, linetype)

        if index2 != None:
            for n in index2:
                stack.insert(n, linetype)

        return stack


    def indices(self, start, end, by=None):

        '''
        --------
        Purpose
        --------
        Create a list of indices for reference

        '''
        return [x for x in range(start, end, by)]


    def print_board(self):

        '''
        --------
        Purpose
        --------
        Arrange the board drawing for user to see


        ----------
        Algorithm
        ----------

        1. Put all the stack lists into another list
        2. Transpose the board by using * to unpack the value in stack, then use zip to get a list of tuples
           (after transposition the card index become the stack index, vice versa)
        3. Get the lists that contain labels and their corresponding cells
        4. Get the indices in the label rows that will be inserted with linebreak
        5. Add linebreak
        6. Turn list of items into a string for printing
        7. Create lines to separate sections
        7. Arrange the board for display

        '''
        # algorithm 7 for foundation + free cells labels / corresponding cards
        separate_line = '{:^170}\n'.format('- ' * 45)
        # algorithm 7 for cascade labels / casacde cards
        separate_line2 = '{:^170}\n'.format('- ' * 35)

        # algorithm 1,2
        matrix = []
        for stack in self.collection_of_stack.values():
            matrix.append(stack)

        transposed = list(zip(*matrix))

        # algorithm 3,4 for foundation and free cells
        header_labels = [i for i in transposed[0]]
        header_cell = [i for i in transposed[1]]
        header_indices = [self.indices(3, 9, 2), self.indices(18, 23, 2)]

        # algorithm 3,4 for cascade
        c = self.locate('C1')
        cascade_labels = [i for i in transposed[c[1]]]
        cascade_indices = [self.indices(6, 24, 2)]

        # algorithm 5
        self.add_linebreak(cascade_labels, cascade_indices[0])
        self.add_linebreak(header_labels, header_indices[0], header_indices[1])
        self.add_linebreak(header_cell, header_indices[0], header_indices[1], '')

        # algorithm 6 for foundation and free cells labels
        h_1 = ''
        for item in header_labels:
            h_1 += '{:^2}'.format(item) + ' ' * 2
        h_1 = '{:^170}\n'.format(h_1)

        # algorithm 6 for card holding cells in foundation and free
        h_2 = ''
        for item in header_cell:
            h_2 += '{:^2}'.format(item) + ' ' * 2
        h_2 = '\n{:^170}\n\n\n'.format(h_2)

        # algorithm 6 for cascade labels
        c_1 = ''
        for item in cascade_labels:
             c_1 += '{:^2}{}'.format(item, ' ' * 2)
        c_1 = '{:^170}\n'.format(c_1)

        # algorithm 6 for cards in cascade
        c_2 = ''
        # if want to trim to see smaller board, change the ending row index. e.g. [4:15]
        for row in transposed[4:15]:
            for item in row:
                c_2 += '\t\t' + (str(item))
            c_2 += '\n\n'

        return '\n' + separate_line + h_1 + separate_line + h_2 + separate_line2 + c_1 + separate_line2 + \
               '\n' + c_2 + '\n' + self.print_current_card() + '\n\n' + self.menu()

    def print_current_card(self):

        '''
        --------
        Purpose
        --------
        Print the current card on hand for user reference

        ----------
        Algorithm
        ----------

        1. Determine if the card on hand is a string or a Card object
        2. Call on method to display the card in string if it is a class object
        3. Return the string

        '''

        if isinstance(self.card, Card):
            return str('{:^170}\n\n{:^170}'.format('Your current card on hand is ', self.card.get_card()))
        elif isinstance(self.card, str):
            return str('{:^170}{}'.format('Your current card on hand is ', self.card))

    def __str__(self):
        return self.print_board()

    '''
    ---------------------------------------------------------------------------------------------------------------------
    Turn the below function on and change the code in line 777 and line 778 to test win.()
    ---------------------------------------------------------------------------------------------------------------------
    '''
    # def test_win(self):
    #     foundation_set = [x for x in range(14,18)]
    #     self.collection_of_stack['14'][1] = 'KS'
    #     self.collection_of_stack['15'][1] = 'KD'
    #     self.collection_of_stack['16'][1] = 'KC'
    #     self.collection_of_stack['17'][1] = 'KH'
    #
    #     return True


def main():
    test = NotFreeCell(20)
    test.start_game()
    print (test)
    while not test.win():
        test.move_card()
        print (test)
        test.place_card()
        test.update_card_on_hand()
        print (test)
            #
            # test.move_card()
            # print (test)
            # test.place_card()
            # test.update_card_on_hand()
            # print (test)
            # test.test_win()


if __name__ == "__main__":
    main()
