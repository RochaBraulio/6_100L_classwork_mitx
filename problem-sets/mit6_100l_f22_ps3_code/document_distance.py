# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Braulio
# Collaborators: None

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    # str_list = []
    # str_list = input_text.split(sep=" ")
    # return str_list

    str_list = []
    str_list = input_text.splitlines() #gets rid of newlines
    str2 = " ".join(str_list)
    str_list2 = str2.split(sep=" ")
    while "" in str_list2: #gets rid of any extra whitespaces
        str_list2.remove("")
    return str_list2
 


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    freq = {}
    for el in input_iterable:
        if el not in freq.keys():
            freq[el] = 1
        else:
            freq[el] += 1
    return freq


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    ch_freq = get_frequencies(word)
    return ch_freq


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    delta = []
    sigma = []
    un_words = [] #intersection of words between freq_dict1 and freq_dict2
    
    #Calculates the intersection of freq_dict1 and freq_dict2, i.e.
    #the list of words that appear on both dicts
    un_words = list(freq_dict1.keys())
    for k2 in freq_dict2.keys():
        if k2 not in un_words:
            un_words.append(k2)
    
    #Calculates delta for each element in un_words list
    for u1 in un_words:
        try:
            d1 = freq_dict1[u1]
        except:
            d1 = 0 #u1 is not in freq_dict1
        try:
            d2 = freq_dict2[u1]
        except:
            d2 = 0 #u1 is not in freq_dict2
        delta.append(abs(d1 - d2))
    
    #Calculates sigma for each element in un_words list
    for u2 in un_words:
        try:
            s1 = freq_dict1[u2]
        except:
            s1 = 0 #u1 is not in freq_dict1
        try:
            s2 = freq_dict2[u2]
        except:
            s2 = 0 #u1 is not in freq_dict2
        sigma.append(s1 + s2)
    
    #Calculates the similarity
    simi = round(1 - (sum(delta)/sum(sigma)),2)
    return simi
    


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    
    mst_frq_wrd = []
    for k,v in freq_dict2.items():
        if k in freq_dict1:
            freq_dict1[k] += v
        else:
            freq_dict1[k] = v
    
    k1 = list(freq_dict1.keys())
    v1= list(freq_dict1.values())
    high = max(v1)
    high_count = v1.count(high)
    if high_count > 1:
        high_idx = []
        for i in range(len(v1)):
        #Gets the index of all values in v1 == high
            if v1[i] == high:
                high_idx.append(i)
        #Uses these indices to retrieve all keys with frequency == high
        for i1 in high_idx:
            high_key = k1[i1]
            mst_frq_wrd.append(high_key)
        mst_frq_wrd.sort()
    else:
        i2 = v1.index(high) #gets the index of high in vl
        high_key = k1[i2] #retrieves the correspoding key in kl
        mst_frq_wrd.append(high_key) #adds this key to the output list
    return mst_frq_wrd


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    file_content = load_file(file_path)
    file_list = text_to_list(file_content)
    total_words = len(file_list)
    tf = get_frequencies(file_list) #not actually tf ye
    for k,v in tf.items():
        tf[k] = v/total_words #now it is tf
    return tf

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    from math import log10
    
    
    idf = {}
    unique_words = [] #list of unique words within all documents
    docs = [] # nested list containing words in each document
    docs_num = 0 #number of documents
    for fl in file_paths:
        fl_content = load_file(fl)
        fl_words = text_to_list(fl_content)
        docs.append(fl_words)
        docs_num += 1
    
    # Gets list of unique words within docs for calculating idf
    for d1 in docs:
        for w1 in d1:
            if w1 not in unique_words:
                unique_words.append(w1)

    
    #Calculates idf for each word
    for w2 in unique_words:
        w_cnt = 0 #initial num of docs with word w in it
        for d2 in docs:
            if w2 in d2:
                w_cnt += 1
        idf[w2] = log10(docs_num/w_cnt)
    return idf

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf = get_tf(tf_file_path)
    idf = get_idf(idf_file_paths)
    tf_idf = {}
    tf_idf_sorted = []
    
    for w1 in tf.keys():
        tf_idf[w1] = tf[w1]*idf[w1]
    while len(tf_idf)!= 0:
        dup_low_v_idx = []
        dup_low_k = []
        tf_idf_k = list(tf_idf.keys())
        tf_idf_v = list(tf_idf.values())
        low = min(tf_idf_v)
        low_count = tf_idf_v.count(low)
        if low_count > 1: # multiple words with the same value of TF-IDF
            for i1 in range(len(tf_idf_v)):
                #Gets the index of all values in tf_idf_v == low
                if tf_idf_v[i1] == low:
                    dup_low_v_idx.append(i1)
            #Uses these indices to retrieve all keys with TD-IDF == low
            for i2 in dup_low_v_idx:
                kmin = tf_idf_k[i2]
                dup_low_k.append(kmin)
            dup_low_k.sort()
            # Add words to output
            for k1 in dup_low_k:
                tf_idf_sorted.append((k1,low))
            # Remove keys from dict
            for k2 in dup_low_k:
                tf_idf.pop(k2)
        else:
            i3 = tf_idf_v.index(low) #gets the index of low in tf_idf_v
            kmin = tf_idf_k[i3] #retrieves the correspoding key in tf_idf_k
            tf_idf_sorted.append((kmin,low))
            tf_idf.pop(kmin)
    return tf_idf_sorted


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    # ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt'] # ORIGINAL- KEEP
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
    
    
       