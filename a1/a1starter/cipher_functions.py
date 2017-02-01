# Functions for running an encryption or decryption.
# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28
# Write your functions here:


def clean_message(Message):
    '''(str) -> str
    takes in a message and returns a copy of it that includes only
    its alphabetical characters, where each of those characters
    has been converted to uppercase
    REQ: message is one line
    >>>clean_message('1a2b3cc')
       ABCC
    >>>clean_message('a 2 b c')
       ABC

    '''

    # Creating a placeholder message for the updated string
    new_message = ''
    # scans every letter in the string
    for i in range(len(Message)):
        # Checks if the letter is within the alphabet
        if (Message[i].isalpha()):
            # Adds the letter to the new message in uppercase
            new_message += Message[i].upper()

    return new_message


def convert_letter(letter):
    '''(str) -> int
    takes a letter and converts it into the appropriate number
    from 0-25, with a = 0, b = 1... z = 25
    REQ: The given string is within the alphabet
    >>>convert_letter('A')
    0
    >>>convert_letter('B')
    1
    >>>convert_letter('Z')
    25
    '''
    # Converting the letter to an upper case one in case
    # it hasn't already been done
    letter = letter.upper()
    # converts the letter into a number, then subtracts
    # 65 from it because with the ord function, the letter A = 65
    # with B being 66, C being 67... etc
    # This is to get the numbers to go from 0 - 25
    number = ord(letter) - 65

    return number


def convert_number(num):
    '''(int) -> str
    takes a number and converts it to the appropriate capitalized letter
    with 0-25 resulting in A-Z respectively
    REQ: The number is between 0-25
    >>>convert_number(25)
    'Z'
    convert_number(0)
    'A'
    convert_number(1)
    'B'
    '''
    # Converting the number to a letter
    # adds 65 to the nummber because the char value of 'A' is 65,
    # with 'B' being 66 and 'C' being 67, allows 0-25 to be properly
    # converted with python
    letter = chr((num + 65))

    return letter


def encrypt_letter(letter, num):
    '''(str, int) -> str
    Given a letter character and a number, converts the letter
    into a number from 0-25, then adds the number to the letter.
    If the resulting sum were to end up greater than 25,
    subtracts 26 from it. Finally, converts the letter back
    into a number
    REQ: the given string is a letter with only one character
    >>> encrypt_letter('L',12)
    'X'
    >>> encrypt_letter('A',8)
    'I'
    >>> encrypt_letter('K',17)
    '''

    # Converts the letter into a number
    letter_num = convert_letter(letter)
    total = letter_num + num
    # Makes sure total (the sum) is below 26 and converts it into a letter
    if (total > 25):
        total = total - 26
    encrypted_letter = convert_number(total)

    return encrypted_letter


def decrypt_letter(letter, num):
    '''(str, int) -> str
    Given a letter and a number, converts the letter into a number.
    Then subtracts that value with num, if the resulting value is below 0,
    adds 26 to that value, then converts the number into a letter
    REQ: The given string is a single letter
    >>> decrypt_letter('X',12)
    'L'
    >>> decrypt_letter('I',8)
    'A'
    >>> decrypt_letter('B',17)
    'K'
    '''
    # converts the letter into a number
    letter_num = convert_letter(letter)

    total = letter_num - num

    # Checks if the number is below 0, if it is, adds 26

    if (total < 0):
        total = total + 26
    # converts the total into a number
    decrypted_letter = convert_number(total)

    return decrypted_letter


def swap_cards(deck_cards, index):
    '''(list of int, int) -> NoneType
    index represents an index for the deck_cards list
    Swap the card or value in deck_cards
    at the index with the card that follows it.
    The deck is circular: if the card at the index is on the bottom of the
    deck, swap that card with the top card
    Mutates the given list using this method

    REQ: index is between 0 and 27 (inclusive)
    REQ: there are more than one card in deck_cards

    >>> x = [1, 2, 3, 4]
    >>> swap_cards(x, 3)
    >>> x == [4, 2, 3, 1]
    True
    >>> x = [1, 2, 3, 4]
    >>> swap_cards(x, 2)
    >>> x == [1, 2, 4, 3]
    True
    '''

    # holds value of deck_cards[index]
    temp_value = deck_cards[index]
    # Swaps the card at index with the following card
    # if the card is at the top of the list
    if (deck_cards[index] == deck_cards[-1]):
        # swaps the top value with the bottom value (deck is circular)
        deck_cards[index] = deck_cards[0]
        # reassigns the value of of deck_cards[0] (bottom card)
        deck_cards[0] = temp_value
    else:
        # swaps the values in the list
        deck_cards[index] = deck_cards[index+1]
        # reassigns the value of of deck_cards[index+1]
        deck_cards[index+1] = temp_value


def move_joker_1(deck_cards):
    '''(list of int) -> NoneType
    Find JOKER1 and swaps it with the following card
    the list is circular, so if JOKER1 is the top card, it swaps
    with the bottom card
    REQ: JOKER1 is within the deck_cards
    REQ: there is more than one element in deck_cards
    >>> JOKER1 = 5
    >>> a = [1, 2, 3, JOKER1]
    >>> move_joker_1(a)
    >>> a == [JOKER1, 2, 3, 1]
    True
    >>> JOKER1 = 5
    >>> a = [1, 2, JOKER1, 4]
    >>> move_joker_1(a)
    >>> a == [1, 2, 4, JOKER1]
    True
    '''

    # finds the index value of JOKER1
    joker_index = deck_cards.index(JOKER1)

    # swaps it with the following card
    swap_cards(deck_cards, joker_index)


def move_joker_2(deck_cards):
    '''(list of int) -> NoneType
    Find JOKER2 and moves it two cards down the list, does so
    by swapping the value of JOKER2 and the card following it,
    then repeating this step again.
    the list is circular, so if JOKER2 is the top card, it swaps
    with the bottom card
    REQ: JOKER2 is within the list
    REQ: There is more than one element in deck_cards

    >>> JOKER2 = 5
    >>> a = [1, 2, 3, JOKER2]
    >>> move_joker_2(a)
    >>> a == [2, JOKER2, 3, 1]
    True
    >>> JOKER2 = 5
    >>> a = [1, 2, JOKER2, 4]
    >>> move_joker_2(a)
    >>> a == [JOKER2, 2, 4, 1]
    True
    '''

    # finds the index value of JOKER2
    joker_index = deck_cards.index(JOKER2)
    # swaps it with the following card
    swap_cards(deck_cards, joker_index)
    # finds the index value of JOKER2
    joker_index = deck_cards.index(JOKER2)
    # swaps it again with the following card
    swap_cards(deck_cards, joker_index)


def triple_cut(deck_cards):
    '''(list of int) -> NoneType
    Finds the two jokers and does a triple cut.
    Finds the locations of the two jokers, then finds which appears first.
    Then every value above the first joker goes
    to the bottom of the deck, and every value below the second
    goes to the top
    REQ: Both JOKER1 and JOKER2 are in the deck
    REQ: There are 2 or more elements in the deck

    >>> JOKER1 = 27
    >>> JOKER2 = 28
    >>> x = [1, 2, 3, 4, 27, 5, 6, 28, 7, 8]
    >>> triple_cut(x)
    >>> x == [7, 8, 27, 5, 6, 28, 1, 2, 3, 4]
    'True'
    >>> x = [1, 2, 3, 4, 27, 28, 5, 6, 7, 8]
    >>> triple_cut(x)
    >>> [5, 6, 7, 8, 27, 28, 1, 2, 3, 4]
    'True'
    >>> x = [28, 1, 2, 3, 4, 5, 6, 27]
    >>> triple_cut(x)
    >>> x == [28,1, 2, 3, 4, 5, 6, 27]
    'True'
    '''

    # find the location of both jokers
    joker1_index = deck_cards.index(JOKER1)
    joker2_index = deck_cards.index(JOKER2)
    # find which joker appears first (which index is lower)
    # then declares it with new variables
    if (min(joker1_index, joker2_index) == joker1_index):
        first_joker = joker1_index
        second_joker = joker2_index
    else:
        first_joker = joker2_index
        second_joker = joker1_index
    # Determining the uppermost card index to know where the deck ends
    final_index = (len(deck_cards) - 1)
    # assigning temporary decks so the list itself doesn't mutate
    # getting all values from 0th to the first joker
    above_first_joker = deck_cards[0:first_joker]
    # getting all the values between the jokers
    between_jokers = deck_cards[first_joker+1:second_joker]
    # getting all the values from the second joker to the end
    # end = last card of the deck
    below_second_joker = (deck_cards[second_joker+1:final_index+1])
    # re ordering the deck according to the algorithm
    # adds back in the jokers to their correct places as well
    deck_cards[:] = (below_second_joker + [deck_cards[first_joker]] +
                     between_jokers + [deck_cards[second_joker]] +
                     above_first_joker)


def insert_top_to_bottom(deck_cards):
    '''(list of int) -> NoneType
    finds the value of the bottom card of the deck
    moves that many cards from the top of the deck to the bottom
    placing them above the bottom card
    REQ: There is more than one element in deck_cards
    >>> a = [0,1,2,3,4,5,6,3]
    >>> insert_top_to_bottom(a)
    >>> a == [3, 4, 5, 6, 0, 1, 2, 3]
    True
    >>> JOKER2 = 28
    >>> JOKER1 = 27
    >>> x = [1,3,2,4,1,5,6,7,4,6,8,9,9,5,3,5,7,8,8,4,3,2,4,6
    ,27,28]
    >>> insert_top_to_bottom(x)
    >>> x == [1, 3, 2, 4, 1, 5, 6, 7, 4, 6, 8, 9, 9, 5, 3, 5, 7, 8, 8,
    4, 3, 2, 4, 6, 27, 28]
    True
    '''

    # find the value of the bottom card
    bottom_card = deck_cards[-1]
    # finds the last index of the cards
    last_index = len(deck_cards) - 1
    # different cases if the bottom card is JOKER2
    if (bottom_card == JOKER2):
        bottom_card = JOKER1
    # grabs bottom_card amount of cards from the top of the deck
    # (0 to bottom_card)
    insert_amount = deck_cards[0:bottom_card]
    # Takes the bottom_card VALUE to the last value in the list
    # and places this in the front, then places the values from
    # 0 to the bottom_card VALUE and adds them to the end

    deck_cards[:] = (deck_cards[bottom_card:last_index] +
                     insert_amount + [deck_cards[last_index]])


def get_card_at_top_index(deck_cards):
    '''(list of int) -> int
    Gets the value of the card at the top of the deck, gets the index
    with that value, and returns the value of the card at
    that index
    if this card is JOKER2, uses JOKER1 as the index.
    REQ: There is more than one element in the deck_cards

    >>> get_card_at_top_index([1,2,3,4,5])
    2
    >>> get_card_at_top_index([5,6,2,1,5,6])
    6
    >>> JOKER2 = 5
    >>> JOKER1 = 2
    >>> get_card_at_top_index([JOKER2,1,2,3,JOKER1,6])
    2
    '''
    # gets the index to search for

    index = deck_cards[0]
    # changes the value of index if it's JOKER2
    if (index == JOKER2):
        index = JOKER1

    # get the value of deck_cards at the index
    final_value = deck_cards[index]

    return final_value


def get_next_value(deck_cards):
    '''(list of int) -> int
    Performs all 5 steps of the algorithm
    simply uses the functions:
    move_joker_1
    move_joker_2
    triple_cut
    insert_top_to_bottom
    get_card_at_top_index
    Then just returns the value of get_card_at_top_index

    REQ: JOKER1 and JOKER2 are in the deck
    REQ: There are at 28 elements in the deck

    >>>get_next_value([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,
        21,24,27,2,5,8,11,14,17,20,23,26])
    11

    >>>get_next_value([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
        16,17,18,19,20,21,22,23,24,25,26,27,28])
    28
    '''

    # performs all 5 steps of the algorithm
    move_joker_1(deck_cards)

    move_joker_2(deck_cards)

    triple_cut(deck_cards)

    insert_top_to_bottom(deck_cards)

    keystream_value = get_card_at_top_index(deck_cards)

    return keystream_value


def get_next_keystream_value(deck_cards):
    '''(list of int) -> int
    Repeats the algorithm until the given keystream values is between
    the numbers 1-26
    REQ: There are 28 elements in deck_cards
    REQ: JOKER1 and JOKER2 are in the deck

    >>>get_next_keystream_value([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,
        21,24,27,2,5,8,11,14,17,20,23,26])
    11

    >>>get_next_keystream_value([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
        16,17,18,19,20,21,22,23,24,25,26,27,28])
    8
    '''

    # repeating get_next_value until it returns a number
    # that is between 1-26
    keystream_value = get_next_value(deck_cards)

    # Makes sure the keystream value is between 1 and 26
    if (keystream_value < 1 or keystream_value > 26):
        while (keystream_value < 1 or keystream_value > 26):
            # changes keystream_value
            keystream_value = get_next_value(deck_cards)

    return keystream_value


def process_message(deck_cards, message, crypt_type):
    '''(list of int, str, str) -> str
    given message, returns it encrypted or decrypted
    based on crypt_type, if crypt_type is 'e', encrypt the message
    if crypt_type is 'd', decrypt the message

    REQ: crypt_type is either 'e', or 'd'
    REQ: deck_cards contains more than 1 element
    REQ: deck_cards contains JOKER1 and JOKER2

    >>> process_message([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,21,24,27,2,
        5,8,11,14,17,20,23,26], '1 am $1ck of th1$,h3lp', 'e')
    'LVZRYEESOTY'

    >>> process_message([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,
        21,24,27,2,5,8,11,14,17,20,23,26],
        'EQFZSR3TEAP^NXL3SRJAMN1GAT', 'd')
    'THISISITTHEMASTERSWORD'
    '''

    # holds the processed message
    processed_message = ''
    # cleans the message for any non-letters
    cleaned_message = clean_message(message)

    # if the message is to be encrypted
    if (crypt_type == 'e'):
        # encrypts each letter of the message
        for i in range(len(cleaned_message)):
            # adds the value to the processed_message
            # gets the next keystream value as well
            processed_message += encrypt_letter(
                cleaned_message[i], get_next_keystream_value(deck_cards))

    # if the message is to be decrypted
    elif (crypt_type == 'd'):
        # decrypts each letter of the message
        for i in range(len(cleaned_message)):
            # adds the value to the processed_message
            # gets the next keystream value as well
            processed_message += decrypt_letter(
                cleaned_message[i], get_next_keystream_value(deck_cards))

    return processed_message


def process_messages(deck_cards, messages, crypt_type):
    '''(list of int, list of str, str) -> list of str
    Gets a list of encrypted or decrypted messages depending on
    crypt_type, if crypt_type = 'd', decrypted, if crypt_type = 'e'
    encrypted

    REQ: crypt_type is 'd' or 'e'
    REQ: there are 28 elements in the deck
    REQ: JOKER1 and JOKER2 are in the deck

    >>> process_messages([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,
        18,21,24,27,2,5,8,11,14,17,20,23,26],
        ['EQFZSRTEAPNXL3SRJAMN1GAT','GLCEGMOTMTRWKHAMGNME'], 'd')
    ['THISISITTHEMASTERSWORD', 'NOTHISCANTBEITTOOBAD']

    >>> process_messages([1,4,7,10,13,16,19,22,25,28,3,6,9,12,15,18,
        21,24,27,2,5,8,11,14,17,20,23,26],
        ['Wh@t 1s l1f3', 'Hopefully not coding this'], 'e')
    ['HQQZVE', 'SZWMOFWLWSXNTGMYGDCEGM']
    '''
    # list for all the processed messages
    processed_messages = []

    for i in messages:
        # decrypts or encrypts for each message value
        processed_messages.append(
            process_message(deck_cards, i, crypt_type))

    return processed_messages


def read_messages(fileOpen):
    '''(io.TextIOWrapper) -> list of str
    Reads and returns the contents of the file as a list of messages
    strips the newline from each line.

    REQ: fileOpen is valid
    REQ: file must be open with 'r'
    '''

    # list that will contain the messages
    list_messages = []
    my_file = fileOpen

    # reads the entire file into a list
    file_list = my_file.readlines()

    # checks all elements in the file list
    for messages in file_list:
        # strips the new lines within the message and
        # puts them together into a new list
        list_messages.append(messages.strip('\n'))

    return list_messages


def read_deck(fileOpen):
    '''(io.TextIOWrapper) -> list of int
    Reads and returns the contents of a file as a list of integers
    also strips all the newlines

    REQ: the file only contains integers from 1-28
    REQ: fileOpen must be valid

    '''
    # list that will contain the numbers
    list_nums = []
    my_file = fileOpen

    # reads the entire file into a list
    file_list = my_file.readlines()

    for i in range(len(file_list)):
        if ('\n' in file_list[i]):
            # strips all the new lines
            file_list[i] = file_list[i].strip('\n')

    for i in range(len(file_list)):
        # gets rid of all spaces in the elements of the file
        file_list[i] = file_list[i].split()
        # adds the the list
        list_nums += file_list[i]

    # converts the list of strings into a list of integers
    for i in range(len(list_nums)):
        list_nums[i] = int(list_nums[i])
    return list_nums
