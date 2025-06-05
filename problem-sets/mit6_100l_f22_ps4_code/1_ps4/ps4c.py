# Problem Set 4C
# Name: Braulio Rocha
# Collaborators: None

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    
    
    from copy import deepcopy
    
    eng_words = load_words(WORDLIST_FILENAME)
    pads_copy = deepcopy(pads)
    valid_words_from_pads = []
    # Gets the number of valid words in decrypted ciphertext for each pad
    # and adds this to valid_words_from_pads
    for i in range(len(pads_copy)):
        valid_words_count = 0
        decrypted_ciphertext = ciphertext.decrypt_message(pads_copy[i]).get_text()
        decrypted_list = decrypted_ciphertext.split(" ")
        for word in decrypted_list:
            if is_word(eng_words, word):
                valid_words_count += 1
        valid_words_from_pads.append(valid_words_count)
    # Retrieves index k from pad with the highest count of valid words
    # according to function specification
    if valid_words_from_pads.count(max(valid_words_from_pads)) > 1:
        # Creates list with indices of pads equal to the max
        high = [
            j
            for j in range(len(valid_words_from_pads))
            if valid_words_from_pads[j] == max(valid_words_from_pads)
            ]
        k = max(high) # retrieves the last pad equal to the max
    elif valid_words_from_pads.count(max(valid_words_from_pads)) == 1:
        k = valid_words_from_pads.index(max(valid_words_from_pads))
    # Retrieves best pad and its correspoding decrypted ciphertext
    best_pad = pads_copy[k]
    best_decrypted_ciphertext =ciphertext.decrypt_message(best_pad).get_text()
    return ps4b.PlaintextMessage(best_decrypted_ciphertext, best_pad)

def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    encrypted_story = get_story_string()
    pads = get_story_pads()
    e1 = ps4b.EncryptedMessage(encrypted_story)
    d1 = decrypt_message_try_pads(e1,pads)
    return d1.get_text()


if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)
    pass