# Exercise 10.1:

def nested_sum(t):
    """Takes a list of lists of integers, adds up the elements from all of the nested lists and returns the sum."""

    total = 0
    for element in t:
        total += sum(element)
    return total

# t = [[1, 2], [3], [4, 5, 6]]
# print(nested_sum(t))


# Exercise 10.2:

def cumsum(t1):
    """Takes a list of numbers and returns the cumulative sum, i.e. a list where the ith element is the sum of the
    first i + 1 elements from the original list."""

    t2 = []
    for i in range(len(t1)):
        t2.append(sum(t1[:i+1]))
    return t2

# t1 = [1, 2, 3]
# print(cumsum(t1))


# Exercise 10.3:

def middle(t1):
    """Takes a list and returns a new list that contains all but its first and last elements."""

    t2 = t1[1:len(t1)-1]
    return t2

# t1 = [1, 2, 3]
# print(middle(t1))


# Exercise 10.4:

def chop(t1):
    """Takes a list, modifies it by removing the first and last elements, and returns None."""

    del t1[0]
    del t1[-1]

# t1 = [1, 2, 3]
# print(chop(t1))


# Exercise 10.5:

def is_sorted(t1):
    """Takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise."""

    return t1 == sorted(t1) # sorted() is a built-in list function

# t1 = [2, 1, 2, 3]
# print(is_sorted(t1))


# Exercise 10.6:

def is_anagram(s1, s2):
    """Takes two strings and returns True if they are anagrams of one another and False otherwise."""

    return sorted(s1) == sorted(s2)

# s1 = "abc "
# s2 = "ba c"
# print(is_anagram(s1, s2))


# Exercise 10.7:

def has_duplicates(t):
    """Takes a list and returns True if there is any element that appears more than once and False otherwise."""

    if len(t) > 1:
        if t[0] in t[1:]:
            return True
        else:
            return has_duplicates(t[1:])
    return False

# t1 = [1, 2, 3]
# print(has_duplicates(t1))


# Exercise 10.8:

from random import randint

# samples = 10000
# hastwosame = 0  # Initialising a variable referring to the number of samples containing at least two students with
#                         # the same birthday, assuming all students are born in the same 365 day period.
# for sample in range(samples):
#     t = []
#     for student in range(23):
#         t.append(randint(1, 365))
#     if has_duplicates(t):
#         hastwosame += 1
# print(str(hastwosame / samples * 100) + "%")


# Exercise 10.9:

def fileappend(file):
    """Takes a file and builds a list with one element per line of it via append."""

    t = []
    fin = open(file)
    for line in fin:
        t.append(line.strip())
    fin.close()
    return t

def fileconcatenate(file):
    """Takes a file and builds a list with one element per line of it via concatenation."""

    t = []
    fin = open(file)
    for line in fin:
        t = t + [line.strip()]
    fin.close()
    return t

# It seems the latter of the two functions takes longer to run, probably because the number of lists is added to each
    # time a word is added, whereas for the first, the number of lists remains 1.


# Exercise 10.10:

def in_bisect(t, target):
    """Takes a sorted list of strings and a target value and returns True if the word is in the list and False if it's
    not, without using the bisect module.

    Precondition: the strings in the list are sorted."""

    middle_index = len(t) // 2
    if len(t) >= 1:
        middle_value = t[middle_index]
        if target < middle_value:
            return in_bisect(t[:middle_index], target)
        elif target == middle_value:
            return True
        else:
            return in_bisect(t[middle_index + 1:], target)
    return False

from bisect import bisect_left

def in_bisect2(t, target):
    """Takes a sorted list of strings and a target value and returns True if the word is in the list and False if it's
    not, with aid of the bisect module."""

    i = bisect_left(t, target)
    if i != len(t) and t[i] == target:
        return True
    return False


# Exercise 10.11:

# t = fileappend("words.txt")
# for word in t:
#     reverse = word[::-1]
#     if in_bisect2(t, reverse):
#         print(word, "&", reverse)


# Exercise 10.12:

def disinterlock(s, n):
    "Takes a string and splits it into a list of n new strings, which, when interlocked, form the original string, s."

    strings = []
    for i in range(n):
        strings.append(s[i::n])
    return strings

def findinterlocked(t, n):
    """Takes a list, t, and prints all the words that are n-interlocked."""

    for word in t:
        strings = disinterlock(word, n)
        works = True
        for string in strings:
            if not in_bisect2(t, string):
                works = False
                break
        if works == True:
            print(word, "=", " + ".join(strings))