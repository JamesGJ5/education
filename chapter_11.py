# eng2sp = dict()
# print(eng2sp)
# eng2sp["hello"] = "hola"
# print(eng2sp)
# eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
# print(eng2sp)
# print(eng2sp["two"])
# print(eng2sp.get("three", None))
# print(eng2sp.get("four", None))

def histogram(s):
    """Returns a dictionary containing the characters in the given string and their
    frequencies.

    Preconditions:
    s: string

    Postconditions:
    d: dictionary"""

    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

# 11.4:

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError("Value doesn't appear in dictionary.")

# LookupError is a built-in function


# 11.5:

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse

# If you have a dictionary that maps multiple keys to the same value, then if you want to make an inverted dictionary, ]
    # it'd be apt for the new values to be lists of the keys originally with the same value.