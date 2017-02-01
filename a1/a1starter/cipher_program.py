"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    # variable to open the deck
    deck_file = open(DECK_FILENAME, "r")
    # variable to open the message file
    message_file = open(MSG_FILENAME, "r")
    # sends the variables for the file and MODE to process_messages
    # and gets the decrypted/encrypted file (depending on mode)
    crypted_message = cipher_functions.process_messages(
        cipher_functions.read_deck(deck_file),
        cipher_functions.read_messages(message_file), MODE)
    # prints the elements of the crypted message, one per line
    for i in crypted_message:
        print(i)
    # closing the files
    deck_file.close()
    message_file.close()

main()
