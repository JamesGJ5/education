# These exercises are those from Section 9.2:

# Exercise 9.1:

"""The below is a programme that opens words.txt, prints all words within it longer than 20 characters, and then closes
words.txt."""

# fin = open("words.txt")
# for line in fin:
#     word = line.strip()
#     if len(word) > 20:
#         print(word)
# fin.close()


# Exercise 9.2:

def has_no_e(word):
    """Returns True if the given word doesn't have the letter e in it."""

    for letter in word:
        if letter.lower() == "e":
            return
    return True


"""Below is a programme that opens words.txt, prints all words within it that lack the letter e, prints the percentage 
of words in the file that don't have the letter e, then closes the file."""

# fin = open("words.txt")
# without_e = 0
# for line in fin:
#     word = line.strip()
#     if has_no_e(word):
#         print(word)
#         without_e += 1
# pct_without_e = without_e / 113783 * 100
# print(str(pct_without_e) + "% of words in words.txt have no e in them.")
# fin.close()


# Exercise 9.3:

def avoids(word, forbidden):
    """Takes a word and a string of forbidden letters and returns True if the word doesn't use any of the forbidden
    letters."""

    for letter in word:
        if letter.lower() in forbidden:
            return
    return True


"""Programme that allows the user to input letters (lowercase) to be forbidden, then prints the number of words in files.txt that 
avoid these characters. N.B: if e is forbidden, so is E."""

# not_forbidden = 0
# forbidden = input("Only enter characters that are to be forbidden: ")
# fin = open("words.txt")
# for line in fin:
#     word = line.strip()
#     if avoids(word, forbidden):
#         not_forbidden += 1
# print(not_forbidden)
# fin.close()


"""The programme below takes words.txt and finds the combination of 5 letters that excludes the fewest of the words in 
file, i.e. the combination for which the number of words in said file that omit the letter in said combination is the 
lowest. However, due its high latency, I have not had time to successfully run it yet, so I may do later."""

# from itertools import combinations
#
# comb = combinations(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
# "u", "v", "w", "x", "y", "z"], 5) # Generates a list of tuples, each of which contains five letters stored as strings.
#
# most_not_forbidden = 0
#
# for i in list(comb):
#
#     print(i)
#     current_not_forbidden = 0
#     forbidden = i
#     fin = open("words.txt")
#
#     for line in fin:
#         word = line.strip()
#
#         if avoids(word, forbidden) == True:
#             current_not_forbidden += 1
#
#     if current_not_forbidden > most_not_forbidden:
# # This step allows for information about the tuple with the fewest  excluded words to be retained.
#         most_not_forbidden = current_not_forbidden
#         least_exclusive_five = i
#
# print(least_exclusive_five)
# fin.close()


def uses_only(word, usedletters):
    """Takes a word and a string of lowercase letters and returns True if the word contains only the letters in the
    list. N.B: e counts for both itself and E."""

    for letter in word:
        if letter.lower() not in usedletters:
            return
    return True


# Exercise 9.4:

"""Prints the words in words.txt that use only the letters acefhlo."""

# fin = open("words.txt")
# for line in fin:
#     word = line.strip()
#     if uses_only(word, "acefhlo"):
#         print(word)
# fin.close()

# My sentence that uses only letters in acefhlo: A loco local!


# Exercise 9.5:

def uses_all(word, usedletters):
    """Takes a word and a lowercase string of required letters and returns True if the word uses all the required letters at
    least once. N.B: if A is included instead of a for example, that is fine."""

    return uses_only(usedletters, word)


def using_all(usedletters):
    """Prints the words and number of words in word.txt that use all of the given letters."""

    no_of_words = 0
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if uses_all(word, usedletters):
            print(word)
            no_of_words += 1
    print(no_of_words)
    fin.close()

# using_all("aeiou")    # 598 words in words.txt use all of aeiou
# using_all("aeiouy")   # 42 words in words.txt use all of aeiou


# Exercise 9.6:

def is_abecedarian(word):
    """Returns True if the letters in the given word appear in alphabetical order (double letters are ok)."""

    previous = word[0].lower()
    for letter in word:
        if letter.lower() < previous:
            return
        previous = letter.lower()
    return True


"""Determines how many abecedarian words there are in words.txt."""

# abecedarian_number = 0
# fin = open("words.txt")
# for line in fin:
#     word = line.strip()
#     if is_abecedarian(word):
#         print(word)
#         abecedarian_number += 1
# print(abecedarian_number)