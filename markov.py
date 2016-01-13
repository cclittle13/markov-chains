from random import choice

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text = open(file_path).read()

    # print text 

    # file_path.close()

    return text

# open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    # words[i], words[i+1]is a tuple and then add words[i+2] to a list  

    for i in range(len(words) -1):
        key = (words[i], words[i+1])
        # print key 
        # prints set of words in tuple form every combination 
        # consecutive words 
        try:
            if key in chains:
                chains[key].append(words[i+2])
            else:
                chains[key] = [words[i+2]]
            # print chains 
        except IndexError:
            pass


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    first_two_words = choice(chains.keys())

    text = first_two_words[0] + " " + first_two_words[1]
    # print text 

    # pull key from dictionary
    # then pick random word from list assigned to the value 
    # then add those 

    while first_two_words in chains:

        # text = text + " " + first_two_words[0] + " " + first_two_words[1]
        next_word = choice(chains[first_two_words])
        text = text + " " + next_word
        first_two_words = (first_two_words[1], next_word)
       
    # print "TEXT: ", text 

    # for key in chains:
    #     chosen_word = choice(chains[key])
    #     print chosen_word
    #     new_tuple = (key[1], chosen_word)
    #     print new_tuple

    
    #     if new_tuple in chains:
    #         chosen_word = choice(chains[new_tuple])

    #     print chosen_word


    return text


input_path = "gettysburg.txt"


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print "Input text next"
# print input_text


# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
