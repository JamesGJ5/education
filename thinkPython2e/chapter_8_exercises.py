# Exercise 8.2:

# print("banana".count("a"))

# Exercise 8.3:

def is_palindrome(word):
    """Returns True if the given word is a palindrome or False otherwise."""
    return word == word[::-1]

# Exercise 8.4:

def any_lowercase1(s):
    """Returns True if the first character in the string is lowercase or False if it isn't."""
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """Returns True."""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Returns True if the last character in the string is lowercase or False otherwise."""
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """The only successful function for this exercise's task: returns True if any of the characters in the string are
    lowercase or False otherwise."""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Returns True if all characters in the string are lowercase or False otherwise."""
    for c in s:
        if not c.islower():
            return False
    return True

# Exercise 8.5:

def letter_shift(code, rotation, lower, upper):
    """Takes a code, adds rotation to it to find a new code, and if the new code is outside of a given range, rotates it
    to its equivalent position within said range. Here, desired codes are in alphabet code ranges, hence the 26
    increment/decrement."""
    new_code = code + rotation

    while new_code < lower:
        new_code += 26
    while new_code > upper:
        new_code -= 26

    return new_code

def rotate_word(word, rotation):
    """Takes a word and rotates each letter in the word through the alphabet by a given rotation, as in a Caesar
    cypher."""
    new_word = ""

    for letter in word:
        code = ord(letter)

        if letter.islower():
            new_code = letter_shift(code, rotation, 97, 122)
        elif letter.isupper():
            new_code = letter_shift(code, rotation, 65, 90)
        else:
            new_code = code

        new_letter = chr(new_code)
        new_word += new_letter

    print(new_word)

    # My function seems to work but the solution in the book is more clear and succinct.