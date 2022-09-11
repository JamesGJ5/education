# Exercise 13.1 - 13.4:

import string

def process_file(filename, * skip_header):
    """Takes a file and returns a histogram containing the words in the file,
    stripped of whitespace and leading/trailing punctuation, as keys, their values
    their frequency of occurence in said file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: dictionary (map from word to frequency)
    """

    hist = {}
    fp = open(filename, "r", errors = "ignore")

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'):
            break

        process_line(line, hist)

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file opbject
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: dictionary (map from word to frequency)
    """
    # TODO: rewrite using Counter

    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables).lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1

def most_common(hist):
    """Makes a list of word-frequency pairs in order of descending frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t

def print_most_common(hist, num=20):
    """Prints the most common words in a histogram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print (20 is default)
    """

    t = most_common(hist)
    print("The most common words are:")
    for freq, word in t[:num]:
        print(word, freq, sep = " - ")

def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """

    # TODO: reimplement using Counter
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""

    return sum(hist.values())

def different_words(hist):
    """Returns the number of different words in a histogram."""

    return len(hist)


# Exercise 13.5:

import random

def random_word(histogram):
    """Chooses a random word from a histogram.

    Probability of a word being chosen is proportional to its frequency.
    """
    # TODO: rewrite using Counter
    li = []

    for word, freq in histogram.items():
        li.extend([word] * freq)

    return random.choice(li)

# print(random_word(hist))


# Exercise 13.6:

def subtract2(d1, d2):
    """Returns a set with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    # TODO: reimplement using Counter
    return set(d1) - set(d2)

# Exercise 13.7:

import chapter_10_exercises
import bisect

def random_word2(histogram):
    """Chooses a random word from a histogram.

    Probability of a word being chosen is proportional to its frequency.
    """

    # keys() and values() work congruently, i.e. they return the same order as
    #   each other
    words = list(histogram.keys())
    cumfreqs = chapter_10_exercises.cumsum(list(histogram.values()))

    # picking a random number between 1 and n (the total number of words in the book)
    n = cumfreqs[-1]
    random_num = random.randint(1, n)

    # finding the index at which random_num would be placed in cumfreqs to maintain
    #   sorted order
    i = bisect.bisect(cumfreqs, random_num)

    # finding the word in the position of the found index in the list words
    random_word = words[i]
    print(random_word)

# hist = process_file("emma.txt", True)

# Exercise 13.8:

# Read text file, return dictionary mapping prefixes to a collection of possible
#   suffixes. Collection may be list, tuple or dictionary. Test programme with
#   prefix length 2, but write programme such that it is easy to try other lengths
#   (maybe have prefix length as a parameter somewhere).

# Could have one function that processes an entire file in this way; within that
#   could have other functions. Probably not a line-by-line one, since consecutive
#   words can be on different lines. Could have a sub-function which takes a prefix
#   and a suffix and adds the prefix to the dictionary as a key (if it isn't one
#   already) and the suffix to the tuple/list/dictionary of its values. Actually,
#   collection would probably have to be mutable for accumulation, so either a list
#   or a dictionary. Some combinations of words, especially if the prefix is chosen
#   to be of length 1, show up very often, so a dictionary might be best to store
#   the collection for search time's sake, and order doesn't seem to matter. Full
#   stops and commas after a word probably prevent it from being a suffix to the
#   following word, as does the em dash, colon and semi-colon. Hyphen should
#   probably be replaced with whitespace. In fact, the hyphen is probably the only
#   one in string.punctuation() that escapes being a blockage. Could probably process
#   the file two lines at a time so consecutive words on different lines can be checked.

# STORE SUFFIXES AS ELEMENTS IN A DICTIONARY. A dictionary can be searched quickly
#   and is mutable (necessary for accumulation) and we don't care about probability
#   of a suffix following so only need one copy of the suffix in the stored collection.
#   collection dictionary's values will be None. Also, order suffixes are found
#   doesn't matter.

# Hyphenated words will be treated as one word for ease; any punctuation trailing
# a word prevents it from being part of the prefix for the following word.

# Check the file two lines at a time, iterating through each line as the
#   first in the pair in each case, so that consecutive words on consecutive lines
#   may be checked.

# An update could be to think of a way to do this without repeating checking lines -
#   could just check the first word in the consecutive line.

def markov_dict(filename, prefix_length=2):
    """Takes a file and returns a dictionary mapping each prefix to the one-word
    suffices that appear ahead of it in the file.

    filename: string
    prefix_length: num, number of words in prefix
    """

    d = {}
    fp = open(filename, "r", errors="ignore")

    for line in fp:

        process_lines(line, d)

def process_line(line, prefix_length, d):
    """For every prefix in the given line, this adds its suffix (if there is one on
    said line or the next one) to the given dictionary.

    line: string
    prefix_length: num
    d: dictionary
    """

    strippables = string.whitespace + string.punctuation
    # COULD USE SPLIT WITH PUNCTUATION AS A DELIMITER TO MAKE SPLITS OF CONSECUTIVE
    #   WORDS THAT AREN'T BLOCKED BY PUNCTUATION