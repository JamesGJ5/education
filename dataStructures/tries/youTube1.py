# In a trie, the root will be *, and after each complete word, we put another *. See 2:40 of the video.

# See 3:38 for why it can be much quicker to look for a word in a trie than a word in a list. In essence, you get that
# looking for a word (of length m) in a trie has a time complexity of O(m).

# Adding a new word also has a time complexity of O(m), since, in the trie, you must simply follow the longest, already-
# present prefix of the word and then simply add the remaining letters.

# My own, untested, uncleaned attempt:

# class TrieNode:
#     """A node in a trie, its value can be a single character."""
#
#     def __init__(self, val):
#         assert len(val) == 1
#         self.val = val
#         # Should make the below a dictionary mapping the next value being searched for to the node that it is a value of
#         self.next_nodes = []
#
#
# class Trie:
#     """A trie containing TrieNodes."""
#
#     def __init__(self):
#         self.root = TrieNode('*')
#
#     def add_string(self, string):
#
#         if len(string) == 0:
#             return
#
#         final_node = self.root
#         i = 0
#
#         while i < len(string):
#
#             for node in final_node.next_nodes:
#                 if node.val == string[i]:
#
#                     final_node == node
#                     i += 1
#                     break
#
#         for character in string[i:]:
#             new_node = TrieNode(character)
#             final_node.append(new_node)
#             final_node = new_node
#
#         final_node.append(TrieNode('*'))
#
#         # What we want to do is start at the root node. We want to check if the first character of the string being
#         # added is the same as any of the root node's next node (N)'s values. If it is, we want to then check if any of
#         # N's next nodes is equal to that of the second character in the string, and continue until either:
#             # we've looked at all of the string's characters to be added
#             #   return
#             # a next node doesn't contain the next character to be added (going to break out of the for loop if this
#             # happens)
#             #   add the next character as a new node, then the character after that to a new node...
#
#         # Recursion sounds like it would be fun, but it would introduce an O(n) auxiliary space complexity, I think.
#         # So, I think iteration would be best.
#
#         # A final_node variable would be a good idea, so we know where to start adding the remaining characters of the
#         # string.
#
#         # It would also be good to store i, the index of the character of the string we are comparing with the value of
#         # the next node
#
#     def find_string(self, string):
#
#         if len(string) == 0:
#             return
#
#         final_node = self.root
#         i = 0
#
#         while i < len(string):
#
#             for node in final_node.next_nodes:
#                 if node.val == string[i]:
#                     final_node == node
#                     i += 1
#                     break
#
#         if i < len(string):
#             return False
#
#         return True


# Video code:

class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode('*')

    def add_word(self, word):
        """Time complexity: O(n), where n is the length of the word being added
        Auxiliary space complexity: O(n), as at most n letters of the word must be added
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.children[letter] = TrieNode(letter)
            current_node = current_node.children[letter]
        current_node.is_end_of_word = True

    def does_word_exist(self, word):
        """Time complexity: O(n), where n is the length of the word being added
        Auxiliary space complexity: O(1)
        """
        if word == '':
            return True
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]
        return current_node.is_end_of_word


# Trie can help if you are given a list of words and you are asked if a word is in that list. Making a trie from the
# list and doing a traversal MAY be faster, IF you are checking if multiple words are in that list, for example.

# Trie can help you if you are given a list of words and you have to find the longest prefix that is common to all of
# them. Well, if len(Trie.root.children) > 1, you can tell there is no such prefix. However, if it is 1, then follow
# the next nodes until you find a node with multiple children. In that case, you return the nodes you have
# looked at as a list (could append to the list on your way).