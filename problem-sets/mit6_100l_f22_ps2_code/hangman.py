# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # Compare letter from secret_word against letter_guessed
    # and store result (boolean) in a list
    match = []
    for letter in secret_word:
        if letter in letters_guessed:
            match.append(True)
        else:
            match.append(False)
    if match.count(True) == len(secret_word):
        return True # all letters_guessed are in secret_words
    else:
        return False


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    progress = []
    for char in secret_word:
        progress.append(char) #converts secret_word in a list

    #Idea is to go over each item from progress and check if it is
    #among letters_guessed. If not, we replace it by an asterisk
    for i in range(len(progress)):
        if progress[i] not in letters_guessed:
            progress[i] = "*"
    return "".join(progress) #join items back into a string for return


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    import string
    
    all_available_letters =  []
    for el in string.ascii_lowercase:
        all_available_letters.append(el) #string will all lowercase letters
    #Idea is to check if letter in letters_guess is found in 
    #all_available_letters list. If it is, then remove it.
    for ch in letters_guessed:
        if ch in  all_available_letters:
            all_available_letters.remove(ch)
    return "".join(all_available_letters) #join items back into a str

def check_valid_input(guess, with_help, previous_guesses, guesses_left):
    """
    Checkes whether the current guess provided by the user is valid or not,
    i.e. if it can be used for current round of the game and provides feedback
    message when current guess is not valid.
    
    Parameters
    ----------
    guess : string, the character provided by the user as guess for
    the current round.
    with_help : boolean, determines whether help mode is enabled
    or not for the current game
    previous_guesses : list, comprised of the letters used by the user
    in previous round of the game as guesses
    guesses_left : int, number of guesses left

    returns:
        boolean, True if current guess is valid,
        or False input is not valid, e.g. numbers or non-alphabet characters and
        ! with help mode turned off, or numbers or non-alphabet characters with
        help mode turned on.
        string, message to be printed to the console when the input provided
        was not valid
    """
  
    guess = guess.lower()
    
    if with_help: #help mode turned on
        if guess == "!":
            if guesses_left >= 3:
                return True, ""
            else:
                return False, "You do not have enough guesses to use help:"
        else:
            if guess.isalpha():
                if guess in previous_guesses:
                    #repeated character provided
                    return False, "Oops! You've already guessed that letter:"
                else: #valid input provided
                    return True, ""
            else: 
                #non-valid character provided
                return False, "Oops! That is not a valid letter. Please input a letter from the alphabet:"
    else: #help mode turned off
        if guess == "!":
            return False, "Help not enabled"
        else:
            if guess.isalpha():
                if guess in previous_guesses: 
                    #repeated character provided
                    return False, "Oops! You've already guessed that letter:"
                else: #valid input provided
                    return True, ""
            else:
                #non-valid character provided
                return False, "Oops! That is not a valid letter. Please input a letter from the alphabet:"
    
def get_unique_vowels_consonants(word):
    """
    Checkes whether input provided is valid or not, i.e. can be used
    as guess for current round of the game.
    Parameters
    ----------
    user_input : string, the character provided by the user as guess for
    the current round.
    with_help : boolean, determines whether help mode is enabled
    or not for the current game

    returns: tuple, comprised of number of unique vowels
    consonants in word
    """
    import string
    
    
    vowels_secret_word = [] 
    consonants_secret_word = []
    vowels = "aeiou"
    consonants = [i for i in string.ascii_lowercase if i not in vowels]
    
    for letter in word:
        if letter in vowels and letter not in vowels_secret_word:
            vowels_secret_word.append(letter)
        elif letter in consonants and letter not in consonants_secret_word:
            consonants_secret_word.append(letter)
    return (vowels_secret_word, consonants_secret_word)
        
    
def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    import random
    
    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print('--------------')
    
    #Initializes game variables
    guesses = 10
    letters_guessed = []
    help_letters = []
    total_score = 0
    player_won = False
    (vowels_secret_word,
    consonants_secret_word) = get_unique_vowels_consonants(secret_word)
    unique_letters_secret_word = vowels_secret_word + consonants_secret_word
    
    
    for turn in range(1,11):
        player_won = has_player_won(secret_word, letters_guessed)
        if guesses >= 0 and player_won == True: # player won the game
            print('Congratulations, you won!')
            print(f'unique letters in secret word: {len(unique_letters_secret_word)}')
            print(f'letters in secret word: {len(secret_word)}')
            total_score = guesses + 4*len(unique_letters_secret_word) + 3*len(secret_word)
            print(f'Your total score for this game is: {total_score}')
            break
        elif guesses == 0 and player_won == False: # player lost the game
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
            break
        else:
            print(f'You have {guesses} guesses left.')
            available_letters = get_available_letters(letters_guessed)
            print(f'Available letters: {available_letters}')
            turn_guess = input('Please guess a letter: ').lower()
            is_valid, message = check_valid_input(
                turn_guess,
                with_help,
                letters_guessed,
                guesses
                )
            # If input is not valid, enter while loop
            while is_valid == False:
                print(message, get_word_progress(secret_word, letters_guessed))
                print('--------------')
                print(f'You have {guesses} guesses left.')
                print(f'Available letters: {available_letters}')
                turn_guess = input('Please guess a letter: ')
                is_valid, message = check_valid_input(
                    turn_guess,
                    with_help,
                    letters_guessed,
                    guesses
                    )
            # If input is valid
            if turn_guess == "!":
                #Get letters from secret_word not guessed yet
                letters_not_guessed = [ch1 for ch1 in secret_word if ch1 not in letters_guessed]
                #Choose letter from help_letters at random
                i = random.randint(0, len(letters_not_guessed) - 1)
                letter_revealed = letters_not_guessed[i]  
                print(f"Letter revealed: {letter_revealed}")
                letters_guessed.append(letter_revealed)
                print(f"{get_word_progress(secret_word, letters_guessed)}")
                guesses -= 3
                print('--------------')
            else:
                if turn_guess in secret_word: #guess is right
                    letters_guessed.append(turn_guess)
                    print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
                    print('--------------')
                else: # guess is wrong
                    if turn_guess in "aeiou": #guess was a vowel
                        guesses -= 2
                        letters_guessed.append(turn_guess)
                        print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                        print('--------------')
                    else: #guess was a consonant
                        guesses -= 1
                        letters_guessed.append(turn_guess)
                        print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                        print('--------------')
                            

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

