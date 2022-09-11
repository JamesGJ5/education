def reverse(string):
    """Takes a string and prints each of its characters in reverse, on a new line."""
    index = -1
    while index >= -len(string):
        letter = string[index]
        print(letter)
        index -= 1

def print_ducklings():
    """Prints the names of the ducklings in Robert McClsokey's book Make Way for Ducklings."""
    prefixes = 'JKLMNOPQ'
    suffix_1 = 'ack'
    suffix_2 = 'uack'

    for letter in prefixes:
        if not letter == "O" and not letter == "Q":
            print(letter + suffix_1)
        else:
            print(letter + suffix_2)

def find(word, letter, start):
    """Takes a word and letter and returns indices at which this letter is found, starting its search at a given start
    index."""
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(string, character, start):
    """Takes a string and prints the number of appearances a given character appears in it, from the given start index
    to the end of the string."""
    count = 0
    for letter in string[start:]:
        if letter == character:
            count += 1
    print(count)

def is_reverse(word1, word2):
    """Takes two words and, assuming they are free of whitespace, returns True if one is the reverse of the other or
    False otherwise."""
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True