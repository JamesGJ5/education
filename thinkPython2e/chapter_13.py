# 13.5 OPTIONAL PARAMETERS:

# Below, the first parameter is required; the second is optional. The default value
#   of num is 10.

def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')

# If a function has both required and optional parameters, all the required parameters have
#   to come first, followed by the optional ones.

# 13.7 RANDOM WORDS:

# ["asbd"] * 10 creates a list with 10 copies of the string "asbd".
# extend() is a method that can be used on a list instead of append when the arg-
#   ument is to be added as more than one element.