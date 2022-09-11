# t = [2, 1, 2, 3, 4]
# t.append(5)
# print(t)
# t.extend([6, 7])
# print(t)
# t.sort()
# print(t)

# t = [1, 2, 3]
# x = t.pop(1)    # t.pop(1) removes the 1th element from the list, and the variable assignment makes x equal to said
#                     # element.
# print(t)
# print(x)
# del t[0]    # Alternatively, the slice index can be used rather than a single index, to remove multiple elements
# print(t)
# print(t.remove(3))
# print(t)

# s = "spam"
# t = list(s)
# print(t)
# sagain = str(t) # As the print below will show, this action doesn't reverse list(s), but instead makes even the square
#                     # brackets in the new t part of the new string sagain; join is what you want to use.
# print(sagain)

# s = "spam is a food"
# t = s.split("s")   # The argument here is optional - if none is included, the words in the string will be made the
#                        # elements.
# print(t)

# t = ["You", "are", "a", "midget."]
# delimiter = " " # Using space as a delimiter makes sure the returned string has a space in  between each word.
# s = delimiter.join(t)
# print(s)

t = [1, 3, 2, 5, 4]
t.sort()
print(t)