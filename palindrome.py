def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(input):
    """Takes an input, converts it to a sting and returns True if it is a palindrome or False otherwise."""
    word = str(input)
    if word == "":
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))