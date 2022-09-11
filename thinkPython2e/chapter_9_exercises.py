from chapter_8 import is_reverse


# Exercise 9.7:

def has_triple_double(word):
    """Returns True if the given word has three consecutive double letters and False otherwise."""

    if len(word) >= 6:
        if word[0].lower() == word[1] and word[2] == word[3] and word[4] == word[5]:
            return True
        else:
            return has_triple_double(word[1:])
    return False


"""Prints words in words.txt that have three consecutive double letters in them."""


# Exercise 9.7:

def has_triple_double(word):
    """Returns True if the given word has three consecutive double letters and False otherwise."""

    if len(word) >= 6:
        if word[0].lower() == word[1] and word[2] == word[3] and word[4] == word[5]:
            return True
        else:
            return has_triple_double(word[1:])
    return False

"""Prints words in words.txt that have three consecutive double letters in them."""

# fin = open("words.txt")
# for line in fin:
#     word = line.strip()
#     if has_triple_double(word):
#         print(word)
# fin.close()

# According to this programme, the words in words.txt with three consecutive double letters are bookkeeper,
    # bookkeepers, bookkeeping and bookkeepings.


# Exercise 9.8:

def is_palindrome(string):
    """Returns True if the given word is a palindrome and False otherwise."""

    return is_reverse(string, string)

# for i in range(999997):
#     if is_palindrome(str(i).zfill(6)[2:]) and not is_palindrome(str(i).zfill(6)[1:]) and not is_palindrome(str(i).zfill(6)):
#         # The latter two conditionals above come from the desire for the string to end in a palindrome of length 4 (no more
#             # and no less, not a palindrome of said length contained within a larger palindrome.
#         if is_palindrome(str(i + 1).zfill(6)[1:]) and not is_palindrome(str(i + 1).zfill(6)):
#             if is_palindrome(str(i + 2).zfill(6)[1:5]) and not is_palindrome(str(i + 2).zfill(6)) and not is_palindrome(str(i + 2).zfill(6)[1:]) and not is_palindrome(str(i + 2).zfill(6)[:5]):
#                 if is_palindrome(str(i + 3).zfill(6)):
#                     print(str(i).zfill(6))
#                     print(str(i + 1).zfill(6))
#                     print(str(i + 2).zfill(6))
#                     print(str(i + 3).zfill(6))

# The numbers the odometer reads are 198888, then 198889, then 198890, then 198891.


# Exercise 9.9:

for agediff in range(51):
    print("Age difference is", str(agediff))
    for spawnage in range (100):
        strspawnage = str(spawnage).zfill(2)
        momage = spawnage + agediff
        strmomage = str(momage).zfill(2)
        if is_reverse(strspawnage, strmomage):
            print("Spawn's age is", strspawnage, "and mom's age is", strmomage)

# When age difference is 18 years, when the spawn's age equals the mom's age reversed, their respective ages at each
    # point are 02 & 20, 13 & 31, 24 & 42, 35 & 53, 46 & 64, 57 & 75, 68 & 86 and 79 & 97. The answer to the specific
    # question is 57 years old.