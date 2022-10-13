# INTRODUCTION (https://www.youtube.com/watch?v=ibjEGG7ylHk)

# Union: groups two groups of elements together
# Find: tells you what group an element belongs to

# Applications:

# Used in Kruskal's algorithm
# Used in grid percolation (seeing if there's a path from the bottom of a grid to the top or vice versa)
# Used in network connectivity (are two vertices in a graph connected by a series of edges)
# Least-common ancestors in a tree
# Image processing

# Complexity (with path compression, I believe):

# Construction -> O(n)
# Union, find, get component size, check if connected -> amortised O(n)
# Count components -> O(1)


# KRUSKAL'S ALGORITHM (https://www.youtube.com/watch?v=JZBQLXgSGfs&t=308s)


# UNION AND FIND OPERATIONS (https://www.youtube.com/watch?v=0jNmHPfA_yE)

# 1. First, create a bijection: a mapping between the n objects you have and integers in range [0, n). Not necessary in
# general but permits the creation of an array-based union find, which is very efficient.

# Map the objects to the integers randomly. Store the mappings in a hashtable so you can do a lookup on them.

# 2. Create an array, where each index has an associated object that can be looked up through the mapping. However, the
# integer filling each index position is the index associated with the parent object of the object whose index the current position is at. 
# Right off the bat, before any nodes share groups, said parent is just the position's index number--we say each node is the parent of itself.

# 3. Say two nodes above are C and K. If you find a union between them, then you put the index number representing K
# in the index position representing C, or vice versa. You might decide that the node with the higher index number
# (found through lookup) becomes the parent, especially if this index number is to be some kind of rank.

# 4. When merging two groups both containing multiple nodes, you make the root of one group the root of another. Say
# you have the following groups: C -> K and A -> B. If you are comparing C and A and you create their union, then you
# implement find() on C and you get the root of its group (K) and on A and you get the root of its group (B), then
# the more highly ranked root becomes the parent of the other. However, rankings may not actually matter that much.

# 5. Yep, find is utilised as above: follow the parents of a given node until you have a node whose parent is itself.

# 6. Now, the issue with this is that we might get long paths from a node to its root, so that when we are doing a union 
# between two nodes that are far from their root (whether the root is the same for each and they are thus already in 
# a union, or the root is different for each and they are thus in sets that are disjoint from each other), you have to 
# find the root before joining one root to another, if the root is different--this means a long path must be traversed. 
# So, to improve upon this, we use path compression, where, when we connect one root to another, we make each root's 
# descendents (grandchildren, great-grandchildren etc.) children of the root before doing the join. As a result, the 
# find operation is a lot quicker (because, in future, each node will be very close to whatever the new root is), and 
# we have the amortised O(n) time complexities mentioned higher up in this file.


# UNION FIND CODE (https://www.youtube.com/watch?v=ibjEGG7ylHk&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=19):


# See the file kruskal.py in the current repository for an implementation of the union-find in Kruskal's algorithm