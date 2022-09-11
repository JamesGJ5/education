# Exercise 12.1:

from chapter_11 import histogram

def most_frequent(s):
    """Takes a string and prints the letters in order of decreasing frequency.
    s: string"""

    # Creates a dictionary where the lowercase of each character in s is a key, its
    # value its frequency of occurence in the lowercase of s, then returns a
    # dict_items object, t, that iterates through character - frequency pairs.
    t = histogram(s.lower()).items()

    # Creates a list of tuples, each of which is a character-frequency pair.
    li = []
    for character, frequency in t:
        li.append((frequency, character))

    # Sorts the list of tuples in order of, primarily, increasing frequency, then
    # secondarily, increasing alphabetical order; then it reverses this list of tuples.
    li.sort(reverse=True)

    # Prints each frequency-character pair in the new list.
    for frequency, character in li:
        print(frequency, character)

def read_file(filename):
    """Returns the contents of a file as a string.

    Preconditions:
    filename: name of a file in string format."""

    fin = open(filename)
    string = fin.read()
    fin.close()
    return string

# string = read_file("words.txt")
# most_frequent(string)


# Exercise 12.2:

from chapter_11_exercises import invert_dict

def sorted_dict(filename, * length):
    """Takes a file and makes it into a dictionary whose keys are the lines of the
    file, stripped, and whose values are the stripped lines in a sorted list.
    Optionally, a length argument can be passed, which allows only keys of an
    exact length to be made.

    Preconditions:
    filename: name of a file in string format

    Postconditions:
    sorted_dict: dictionary"""

    sorted_dict = {}
    fin = open(filename)

    for line in fin:
        word = line.strip()

        if len(length) > 0 and len(word) == length[0] or len(length) == 0:
            sorted_dict[word] = tuple(sorted(line.strip()))

    return sorted_dict

def anagram_dict(d):
    """Takes a dictionary and returns a new dictionary whose keys are tuples of 
    keys of the old dictionary that shared the same value (the same sorted list), 
    i.e. whose keys are tuples of anagrams; the values are the lengths of these
    tuples. N.B: the tuples are all of length greater than 1.
    
    Preconditions:
    d: dictionary
    
    Postconditions:
    anagram_dict: dictionary"""

    li = invert_dict(d).items()
    anagram_dict = {}

    for sorted, anagrams in li:
        if len(anagrams) > 1:
            anagram_dict[tuple(anagrams)] = len(anagrams)

    return anagram_dict

def anagram_returner(d):
    """Returns a list of tuples of anagrams sets (that are keys in the dictionary anagram_dict) and their sizes,
    in order of, primarily, decreasing list size, then secondarily, decreasing
    alphabetical order of the list.
    
    Preconditions:
    d: dictionary"""

    d_items = d.items()
    li = []

    for anagrams, number in d_items:
        li.append((number, anagrams))

    li.sort(reverse=True)

    return li

"""This programme reads a word list from a file and prints all the sets of words of 
length 8 (no argument has to be supplied where the 8 is, though) that are 
anagrams, in order of decreasing size of anagram set."""


def anagram_finder(filename, * length):
    """Takes a file and returns lists of sets of anagrams (of stripped lines)
    within it. If it is words.txt, these will be word anagrams. If a length is
    provided, only words with the given length will be in the printed lists.

    Preconditions:
    filename: name of file in string format
    length: a number

    Postconditions:
    li: a list"""

    if len(length) > 0:
        d = sorted_dict("words.txt", length[0])
    else:
        d = sorted_dict("words.txt")
    d2 = anagram_dict(d)
    li = anagram_returner(d2)

    return li

# print(anagram_finder("words.txt", 8))

# Exercise 12.3:

def word_differences(word1, word2):
    """Returns the number of differences between words of equal length. A
    difference is where the character at a given index in one word differs from
    that in the equivalent position in the other word.

    Preconditions:
    word1: string
    word2: string
    len(word1) == len(word2)"""

    assert len(word1) == len(word2)

    count = 0

    for chr1, chr2 in zip(word1, word2):
        if chr1 != chr2:
            count += 1

    return count

def metathesis_pairs(li):
    """Prints all pairs of words that differ by swapping two letters.

    Preconditions:
    li: list of tuples that contain anagrams of each other."""

    for anagram_set in li:
        for word1 in anagram_set:
            for word2 in anagram_set:
                if word1 < word2 and word_differences(word1, word2) == 2:
                    print(word1, "&", word2)


# li = []
# for t in anagram_finder("words.txt"):
#     li.append(t[1]) # li is now a list of tuples, each containing a set of anagrams.
# metathesis_pairs(li)


# Exercise 12.4:

def word_dict():
    """Reads a word list (words.txt) and returns a dictionary whose keys are the
    words within it and whose values are None.

    Postconditions:
    d: dictionary"""

    d = {}

    fin = open("words.txt")
    for line in fin:
        word = line.strip()

        d[word] = None

    return d

d = word_dict()

def wordchildren(word):
    """Takes a word and returns a tuple containing elements that are the children
    of the word (formed by removing a single letter from the word).

    Preconditions:
    word: string

    Postconditions:
    children: tuple, element(s): string(s)"""

    children = ()

    for i in range(len(word)):
        child = word[0 : i] + word[i + 1 :]
        children += child,

    return children

reducible = {"": True, "a": True}

def is_reducible(word):
    """Returns True if a word is reducible or False otherwise.

    Preconditions:
    word: string, in words.txt"""

    if word in reducible:
        return True

    elif word == "":
        return True

    elif not word in d:
        return False

    else:
        children = wordchildren(word)

        for word in children:
            if is_reducible(word):

                reducible[word] = True
                return True

        return False

def reduciblewords():
    """Takes words.txt and adds all the words in it that are reducible to the
    dictionary called reducible.

    Preconditions:
    filename: "words.txt"
    """

    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if is_reducible(word):
            reducible[word] = True
    fin.close()

reduciblewords()
reduciblelist = []
for word, value in reducible.items():
    reduciblelist.append((len(word), word))
reduciblelist.sort(reverse = True)
print(reduciblelist)