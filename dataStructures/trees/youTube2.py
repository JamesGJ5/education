# In a binary SEARCH tree, for a given node, it is BIGGER than EVERY node in its LEFT SUBTREE, and SMALLER than EVERY
# node in its RIGHT SUBTREE.

# The above leads to there being NO DUPLICATE NODES in a binary search tree, especially since parent-child
# relationships are < or > inequalities, NOT <= or >=.

# When INSERTING a node into a binary search tree, you always add it as a LEAF. However, to find where this leaf will
# be, you first compare the node being added to the root node; if it is smaller, you then compare with the root node's
# left child, but the right child if it is bigger, and then you continue this comparison down the binary tree until
# you are comparing it with a leaf node, at which point you put it either as left child or right child, depending on
# the inequality. HOWEVER, IF AT ANY POINT YOU ARE COMPARING THE ADDED NODE WITH A NODE OF THE SAME VALUE, YOU CANNOT
# ADD IT IF YOU WANT THE BINARY TREE TO REMAIN A BINARY SEARCH TREE. O(log(n)).

# When FINDING a node of a given value, you do the same traversal as above and return True if you encounter a node of
# the same value, but False otherwise. O(log(n)).

# When DELETING a node, there are three possible cases:

# 1. Node being deleted is a leaf node (0 children). O(1) for the deletion part, but the FINDING of the node to be
# deleted may increase time complexity to O(log(n)):
#   In this case, I reckon the node can be removed from the tree simply and it'll still be a binary search tree.

# 2. Node being deleted has 1 child. O(1) for the deletion part, but the FINDING of the node to be deleted may increase
# time complexity to O(log(n)):
#   In this case, I reckon the node can be removed from the tree and then its child must move up and take its
#   place, then one of these steps (1, 2 or 3) is repeated depending on how many children the node that was just moved
#   up had. Can possibly just use some sift down method, preferentially replacing the left nodes as you go to maintain
#   the binary search tree. HOWEVER, IF THE TREE IS MORE LIKE A LINKED LIST (WITH ATTRIBUTES 'LEFT' AND 'RIGHT' FOR EACH
#   NODE) THAN AN ARRAY, ONLY NEED TO CHANGE THE PARENT OF THE NODES THAT HAVE JUST LOST THEIR PARENTS, AND NOT THE
#   CHILDREN FURTHER DOWN THE LINE.
#   Child node has its parent reassigned to the parent of the node being deleted. If using a linked list rather than
#   an array, this is very efficient.

# 3. Node being deleted has 2 children. O(log(n)) for the deletion part (because you must find the node to replace the
# deleted node with, by traversal:
#   Call the node being deleted D, its smaller (left-hand) child L and its bigger (right-hand) child R. If you replace
#   D with L, you indeed have the property that the new parent is smaller than all values in the right-hand subtree (at
#   the top of which lies R). However, if L had any right-hand children of its own, then that would remain in the left
#   subtree (where L was), and thus L would not be bigger than all values in the left subtree, where it used to be.
#   Thus, this would not be a valid solution.
#   INSTEAD, what you do is traverse the right-hand subtree, deviating towards left-hand nodes wherever you can, until
#   you find the last left-hand node in this path (see the YouTube video). Then, you convert D into this node, and the
#   binary search tree order is retained. O(log(n)
#   todo: make sure there isn't anymore to the above. For example, if L has no children, do you still take a left-hand
#   node from the right-hand subtree instead?
#   Answer: I think we just find the in-order successor for consistency.

# According to
# https://www.baeldung.com/cs/applications-of-binary-trees#:~:text=In%20computing%2C%20binary%20trees%20are,insertion%2C%20deletion%2C%20and%20traversal.
# binary trees, in the form of binary search trees for example, are indeed mainly used for searching and sorting.