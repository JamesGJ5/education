# WHAT IS A FIBONACCI HEAP

# Like the binomial heap, the Fibonacci heap is a list of trees, each one being a heap itself.

# The aforementioned trees can have any shape.

# The minroot in the binomial heap must be kept track of. When we say tree of the smallest root, we mean the following:
# in http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf, on Page 5, the third diagram has
# a B1 (IGNORE WHERE IT SAYS B0) tree and a B4 tree. So, there are two roots in the binomial heap: the root of B1 and
# the root of B2. These trees are often in a list, for example a linked list, by connection of their root nodes. That
# is what you see at 3:53 of the current YouTube video: a tree (containing a single node of value 7) connected to
# another tree, with 4 nodes.

# We keep track of the minroot (specifically, a pointer to this node) because we want fast access to it.


# OPERATION: PUSH

# Push involves adding a node to the list as a tree with just one node; if you then want to add another, do the same.
# Clearly O(1). See 4:49, where you also find that the Fibonacci heap must store pointers to the roots of each
# sub-heap, and must store a pointer to the minroot.


# OPERATION: POP-MIN

# See 5:13; it's the same procedure as the binomial heap--see the current video for how to do this practically.

# Don't have to do the merges in the above in any particular order.

# Add the end, set the minroot to the connect node.

# Above, we only do clean-up when we remove a minroot; not after each addition of a node to the Fibonacci heap. This
# results in improved efficiency (O(1) amortised time complexity).


# OPERATION: DECREASEKEY

# A main advantage of Fibonacci heaps over binomial heaps is that, in a binomial heap, the time complexity of
# decreasekey is O(log(n)), where n is the number of nodes in the binomial heap; in a Fibonacci heap, this can be
# amortised to O(1).

# NOTE: amortised time-complexity is different to average-case time complexity; the former is the time complexity that
# occurs MOST of the time, whereas the latter is that that occurs for the MEAN of the time. Think of the former as the
# mode, the latter as the mean, I think.

# In decreasekey in the Fibonacci heap, if we decrease a key in a tree in the heap such that its value violates its
# position in the tree it is in, we don't sift it up (which would take O(logn)); instead, we just disconnect this node
# from its parent and make it a root in the list of roots (with its initial children still connected, and theirs and
# so on--so, the list mentioned contains yet another tree.

# Then later, clean-up happens when popmin is called.

# todo: find out why a large, shallow tree is bad
# However, if popmin isn't called often enough, a large, shallow tree will build up, which is no goode. To prevent this
# build up:

# 1. Every time a node loses its child, mark that node as a loser.

# 2. When a loser has lost 2 children in total, it gets kicked out of the tree itself and gets put into the root list.
# See 9:59 onwards. The loser that has been dumped into the root list is then unmarked as a loser.

# The code at 11:17 essentially says the following; this code applies whatever the tree looks like, however, for this
# example, start with the first tree. Apply the function decreasekey(v, k') to the 9-node (n) at the bottom of this
# tree, by passing v as the pointer to this node/the value of the node to be changes from and k' as the value this
# 9-node is to be reduced to (6). So, the value
# of this node, and thus n.key, becomes 6; this is < the node's parent (8), so n violates the heap condition.
# Therefore, we create a while loop which executes when n violates the heap condition, as it does initially. Now, the
# next blocks of code run uninterrupted by the while loop, even if n becomes satisfactory of the heap condition, until
# the blocks are passed. So, the 6-node is removed, we make sure it isn't a loser, then we make its parent n. If this
# parent was not a loser, then this process would not be repeated. However, it is, so it does indeed get removed, and
# so does its own parent. However, when n becomes the 4-node, it is not a loser, so said process is repeated no more.
# Instead, we move onto the if statement; the 4-node has lost children, so it is eligible to become a loser. However,
# making it a loser without it being a root node would be a bad idea, for that might mean that later, if another child
# was added and then removed, we'd have to run the code under "repeat" on the root node, which wouldn't work since the
# root node has no parent. Moreover, it would be a waste to reinsert the root node into the root list, where it already
# is present. Therefore, we only make p a loser if it is a root.


# ABOUT GOOD CODING STYLE

# 16:25. So that you don't have to implement an O(n) find() operation to find a key before decreasekey is implemented, give
# each vertex in the graph an identifier of some sort, where vertices describe where each node is, and also give each
# node an identifier. This way, keep two views of the heap decoupled and find a node value by lookup in a dictionary.
# Or, see 16:40 for an object-oriented method of doing this.