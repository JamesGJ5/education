"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

import sys
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


# def process_file(filename, order=2):
#     """Reads a file and performs Markov analysis.
#
#     filename: string
#     order: integer number of words in the prefix
#
#     returns: map from prefix to list of possible suffixes.
#     """
#     fp = open(filename, encoding='UTF-8')
#
#     # Remember, the file object above is an iterator, so once skip_gutenberg_header is applied, the below will not go
#     # over the same lines.
#     skip_gutenberg_header(fp)
#
#     for line in fp:
#         if line.startswith('*** END OF THIS'):
#             break
#
#         for word in line.rstrip().split():
#             process_word(word, order)
#
#
# def skip_gutenberg_header(fp):
#     """Reads from fp until it finds the line that ends the header.
#
#     fp: open file object
#     """
#     for line in fp:
#         if line.startswith('*** START OF THIS'):
#             break
#
#
# def process_word(word, order=2):
#     """Processes each word.
#
#     word: string
#     order: integer
#
#     During the first few iterations, all we do is store up the words;
#     after that we start adding entries to the dictionary.
#     """
#     global prefix
#     if len(prefix) < order:
#         prefix += (word,)
#         return
#
#     try:
#         suffix_map[prefix].append(word)
#     except KeyError:
#         # if there is no entry for this prefix, make one
#         suffix_map[prefix] = [word]
#
#     prefix = shift(prefix, word)
#
#
# def random_text(n=100):
#     """Generates random words from the analyzed text.
#
#     Starts with a random prefix from the dictionary (not the English dictionary, you fool--the dictionary made by
#     processing a particular file of words).
#
#     n: number of words to generate
#     """
#     # choose a random prefix (not weighted by frequency)
#     start = random.choice(list(suffix_map.keys()))
#
#     for i in range(n):
#         suffixes = suffix_map.get(start, None)
#         if suffixes == None:
#             # if the start isn't in map, we got to the end of the
#             # original text, so we have to start again.
#             # The below utilises recursion, but if you think about it, the number of words in the final product always
#             # adds up to the initial n.
#             random_text(n-i)
#             return
#
#         # choose a random suffix
#         word = random.choice(suffixes)
#         print(word, end=' ')
#         start = shift(start, word)
#
#
# def shift(t, word):
#     """Forms a new tuple by removing the head and adding word to the tail.
#
#     t: tuple of strings
#     word: string
#
#     Returns: tuple of strings
#     """
#     return t[1:] + (word,)
#
#
# def main(script, filename='158-0.txt', n=100, order=2):
#     try:
#         n = int(n)
#         order = int(order)
#     except ValueError:
#         print('Usage: %d filename [# of words] [prefix length]' % script)
#     else:
#         process_file(filename, order)
#         random_text(n)
#         print()

class Markov:
    """Object that can be used to generate a somewhat-random string of words based on prefixes and their following
    suffixes in an existing text file.

    originFile: string, name of file from which dictionary to do this is made
    prefix: tuple of words in prefix, resets to empty tuple after a text is processed
    suffixMaps: map from order (integer number of words in the prefix) to a suffix map containing prefixes of that
                order, don't want to compute these maps every single time
    """

    def __init__(self, originFile):
        assert isinstance(originFile, str)
        self.originFile = originFile
        self.prefix = ()
        self.suffixMaps = {}

    def makeText(self, n=100, order=2):
        try:
            n = int(n)
            order = int(order)
        except ValueError:
            print('The number of words to be made and the order to be used must be numbers.')
        else:
            if not order in self.suffixMaps.keys():
                self.process_file(self.originFile, order)
            self.random_text(n, order)
            print()

    def process_file(self, originFile, order):
        """Reads an origin file and performs Markov analysis. Only works on files with UTF-8 encoding.

        originFile: string
        order: integer number of words in the prefix

        returns: map from prefix to list of possible suffixes.
        """
        fp = open(originFile, encoding='UTF-8')

        self.suffixMaps[order] = {}

        # Remember, the file object above is an iterator, so once skip_gutenberg_header is applied, the below will not
        # go over the same lines.
        self.skip_gutenberg_header(fp)

        for line in fp:
            if line.startswith('*** END OF THIS'):
                break

            for word in line.rstrip().split():
                self.process_word(word, order)

        self.prefix = ()

    def skip_gutenberg_header(self, fp):
        """Reads from fp until it finds the line that ends the header.

        fp: open file object
        """
        for line in fp:
            if line.startswith('*** START OF THIS'):
                break

    def process_word(self, word, order):
        """Processes each word.

        word: string
        order: integer

        During the first few iterations, all we do is store up the words;
        after that we start adding entries to the dictionary.
        """
        if len(self.prefix) < order:
            self.prefix += (word,)
            return
        try:
            self.suffixMaps[order][self.prefix].append(word)
        except KeyError:
            # if there is no entry for this prefix, make one
            self.suffixMaps[order][self.prefix] = [word]

        self.prefix = self.shift(self.prefix, word)

    def random_text(self, n, order):
        """Generates random words from the analyzed text.

        Starts with a random prefix from the dictionary (not the English dictionary, you fool--the dictionary made by
        processing a particular file of words).

        n: number of words to generate
        """
        # choose a random prefix (not weighted by frequency)
        suffix_map = self.suffixMaps[order]
        start = random.choice(list(suffix_map.keys()))

        for i in range(n):
            suffixes = suffix_map.get(start, None)
            if suffixes == None:
                # if the start isn't in map, we got to the end of the
                # original text, so we have to start again.
                # The below utilises recursion, but if you think about it, the number of words in the final product always
                # adds up to the initial n.
                self.random_text(n - i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print(word, end=' ')
            start = self.shift(start, word)

    def shift(self, t, word):
        """Forms a new tuple by removing the head and adding word to the tail.

        t: tuple of strings
        word: string

        Returns: tuple of strings
        """
        return t[1:] + (word,)

if __name__ == '__main__':
    # main(*sys.argv)

    markov1 = Markov(originFile='158-0.txt')

    markov1.makeText(n=100, order=2)