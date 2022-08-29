# NOTE: IN http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf, ON PAGE 5, UNDER THE 3RD
# DIAGRAM, B0 SHOULD BE CORRECTED TO B4.

# BINOMIAL TREE

# Binomial tree Bk is of order k

# B0 is a tree with one node

# Bk (for k >= 1) is a pair of B(k-1) trees, where (for a min binomial tree) the B(k-1) with the smaller root value is
# the root of Bk, and the root of the other B(k-1) is the leftmost child of the root of Bk. We choose this order in the
# min-binomial heap


# BINOMIAL TREE STRUCTURAL PROPERTIES

# 1. 2**k nodes in Bk

# See Page 2 of http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf for "Proof of
# Property 1"; it's all about doubling the number of nodes in B(k-1) when combining two B(k-1)'s to get Bk, starting
# with the fact that B0 has only 1 node

# 2. The height of a binomial tree is k--see a vertical line in
# https://subscription.packtpub.com/book/application-development/9781785888731/12/ch12lvl1sec83/binomial-trees#:~:text=Its%20height%20is%20equal%20to,in%20terms%20of%20itself%2C%20recursively.
# for what an incrementation of height by 1 looks like.

# Following on from above, because the node in B0 has no children or parents, it has a height of 0, which is why Bk has
# indeed a height of k; each time you add 1 to k-1, the root of a tree of the same order is raised to be the parent of the
# root of another; the former root becomes the overall root, so height from lower tree to its old root (k-1) + height from
# lower tree's old root to overall tree's new root (1) = k-1 + 1 = k, so Bk has a height of k.

# The above is my proof; see Page 2 of http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf
# for "Proof of Property 2".

# 3. Note: in the source we're learning from, parentheses in which one character (e.g. k) appears over another (e.g. i)
# means the binomial coefficient: see
# https://math.stackexchange.com/questions/1713706/what-does-2-values-vertically-arranged-in-parenthesis-in-an-equation-mean
# Here, I will represent this as (k/i), it's the same as kCi (k choose i)

# There are exactly (k/i) nodes at depth i = 0, 1, ... k, where i = 0 is the root of Bk; (k/0) is just 1, necessarily
# for i to be the depth the root is situated at. This is why we call the structure a BINOMIAL TREE.

# See Page 2 of http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf for "Proof of
# Property 3"; I understand most of it, I just don't understand how D turns into a binomial coefficient in the first
# place.
# todo: answer the above question

# 4. The root has degree k, which is greater than that of any other node; degree is essentially how many children it has.
# For example, every time you combine two B(k-1)s to become Bk, the root of one B(k-1) gains 1 new child (the root of
# the other B(k-1)), and B0 has 0 children so we know its root's degree is 0; so, we know the root of Bk has a degree
# of k.

# If the children of the root of Bk are numbered from left to right by i = k-1, k-2, ... 0, then child i is the root of the
# subtree Bi--look at the B2 in http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf and
# number its children in this manner. Now, look at the trees said children are roots of and you will see that this is
# the case. This is because the larger-root B(k-1) is added as a leftmost node to the other B(k-1) each time k is
# raised by 1.

# See Page 2 of http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf for the process of
# starting with an array of numbers and making a min binomial tree out of it--a ground up approach must be taken to this,
# because you will not need to make as many comparisons if you start with B0 and work your way upwards than if you
# try to start with the first element of the array as the root of the final tree, I think--in the latter case, you
# might find down the line that you have a node that must be sifted up.


# BINOMIAL HEAP

# A min binomial heap H is a collection of distinct min binomial trees. For each k >= 0, there is at most one min
# binomial tree in H whose root has degree k.

# Observation 1: an min binomial heap with n number of nodes consists of at most log(n) + 1 binomial trees.

# Observation 2: a binomial heap of n nodes and a binary representation of n has a relation. What is meant by "a binary
# representation of n" is this: n is simply an integer, and a binary representation of an integer is just a base 2 form
# of that integer.

# More from the lecture notes: "Binary representation of n requires log(n) + 1 bits."
# Say that n is 124520186 in base 10. Now, just like in the base 10 number N (124520186) the number of
# digits is given by log10(1.23... * 10**8) // 1 + 1 = 8 + 1 = 9, the base 2 form of N will have log2(N) // 1 + 1 digits. If a
# digit is represented by a bit, then log2(N) // 1 + 1 bits will be needed to represent N.

# Finally, within this observation: "adding a node into a binomial heap H is equivalent to adding a binary '1' to the
# binary representation of H. This makes sense because a single node is equal to a B0 tree; it has n = 1, and the
# binary representation of the base-10 1 is still 1.

# See Page 2 of http://www.iiitdm.ac.in/old/Faculty_Teaching/Sadagopan/pdf/ADSA/binomialheap.pdf for an example of
# starting with an array of numbers and making a min binomial heap out of it. Must read the paragraph above it to
# understand. From B1 to B2, two nodes were added, so you go from binary 10 (which is 2 in base 10), to binary 11
# (which is 3 in base 10), to binary 100 (which is 4 in base 10).

# I think that, when it says "for n = 8, the final binomial heap has B3 = 1 and B2 = B1 = B0 = 0 which is
# 1 0 0 0, the binary representation of 8", it means when you look at this binomial heap on Page 3, you see 1 B3 but
# you don't see any B2, B1 or B0, which is why the binary number is 1 0 0 0.

# When it says "For n = 17, the binomial heap consists of one B4 and B0, which corresponds to the binary representation
# of 1 0 0 0 1", it means that if you draw the diagram, you will see a 1 B4 tree and 1 B0 tree side by side (but no
# B1, B2 or B3) which is why the binary number is 1 0 0 0 1.


# INSERTION OF NODE INTO BINOMIAL HEAP

# Inserting a node into a binomial heap H is equivalent to adding a binary '1' to the binary representation of H (or
# the binary representation of the number of nodes in H, as stated earlier. At worst, the newly inserted node B0
# (a binary '1' is B0, as B0 contains just 1 node, and the binary representation of 1 just looks like 1) triggers merge
# at each iteration, e.g. inserting B0 creates a new B1, which in turn creates a new B2 and so on. For example, if we
# start with a binomial heap H represented by the binary number 111111111, then if we had B0, we get a flow like this:

# 111111111 + 1 = 111111112 -> 111111120 -> 111111200 -> 111112000 -> 111120000 -> 111200000 -> 112000000 ->
# 120000000 -> 200000000 -> 1000000000; every time the 2 moves back and leaves a zero is an example of a carry

# Remember, a different digit position corresponds to a different k in Bk; so, as the 2 moves across the digits, it
# creates a new Bk at that digit position, and then the two Bks at that position must merge and that creates a new Bk+1 (so
# we get a 2 at the digit beforehand and the digit we were just at becomes 0...

# But yeah, since log2(n) is the number of digits, where n is the number of nodes in the binary heap, there are
# log2(n) merges (one at each digit/iteration), so insert is O(log2(n)). Moreover, no matter how large the tree is, the
# merge complexity is the same (O(1))--just need to make the root of one tree the child of another; if not for this,
# the complexity would be different to simply log2(n), probably


# MERGING OF BINOMIAL HEAPS

# Merging binomial H1 and H2 is equivalent to adding two binary numbers--in particular, adding the binary
# representation of |H1| and |H2|, where I think || refers to the number of nodes in each heap.

# "In the worst case, every BIT addition generates a carry which is equivalent to creating a new Bi while merging a copy of
# B(i-1)". According to
# https://www.electronics-tutorials.ws/combination/comb_7.html#:~:text=So%20when%20adding%20binary%20numbers,for%20addition%20and%20so%20on.
# a carry is just each time a digit becomes greater than or equal to 2 due to an addition, so then this contributes to
# the addition at the previous column, and so on... each time we moved back the 2 in the example somewhere above with
# lots of numbers, that was a carry.

# Say the binary numbers we are adding are 111 and 111. Say i-1 is 0 (i.e. we are looking at the rightmost digit in
# each). Since this digit is a 1 for each, the two (don't get too confused by "copy") B0s will merge, and then create
# a B1 (which is Bi, because i-1 = 0). After this, we will have three B1s (two in the initial heaps and one from the
# merge)... look at the diagrams on Pages 4 and 5 to understand this--will probably need to see all the diagrams to
# understand what comes next.

# But for merges starting with procedure mentioned above, O(log(n)) is time complexity in the worst case (where merge
# and carry occurs at each bit position), where n = |H1| + |H2|. In the worst case, |H1| = |H2|, because merges can
# only continue as far as the highest index position in the smaller binary number. Because merge and creation is what
# happens at each digit position (and there are log2(n)) digits, then because the time each merge takes even for
# different digits is the same (just have to connect one root to another, the size of the merged trees doesn't matter),
# then this is an O(log2(n)) procedure.

# So, merge has a time complexity of O(log2(n)).

# As explained on the website, procedure for merging is as follows:

# 1. If B0 is present in just one of the heaps, then do nothing. However, if B0 is present in both of the heaps, merge
# two copies of B0 and create one B1. In general, merge two copies of Bi whenever they are present and create a copy of
# Bi+1.

# 2. On merging the B0s as above, we may get three copies of B1... leave the first B1 and merge the last two to obtain
# one B2.

# 3. Now, two B2s exist in the example on the website. Whenever, more than two copies of Bi exists, leave the first one
# and merge the last two.

# 4. Now, merge two B3, and the website example is complete.


# EXTRACT MIN FROM BINARY HEAP

# For extract min, take Bk as the tree containing the minimum of a binomial heap H. The root has children that are
# roots of Bk-1, Bk-2 ... B0, as stated in the 4th structural property. To remove the min is simple: basically, take
# away the root of Bk and you are just left with the individual child trees mention, unconnected. Now, we perform merge
# on these so that each Bi occurs at most once. As we have already seen, merge has a time complexity of O(log(n)) in
# the worst case, so...

# ... extract min has a time complexity of O(log(n)) in the worst case.


# DECREASE KEY

# In this operation, we choose to decrease the value of a node. In a min binomial heap, if you think back to how the
# tree is built from the ground up, you realise that each node must be greater than or equal to its parent. Therefore,
# if you decrease the value of that node such that it becomes smaller than or equal to that of its parent, it must
# move.

# So say the value of the node pointed by the pointer x is decreased to the desired value y. If y is larger [although
# the lecture notes say smaller for some reason] than its parent, i.e., on performing decrease, the min binomial heap
# property is still maintained, then no further modification is needed.

# Otherwise, min-heapify() routine (sift-up in C:\Users\james\PycharmProjects\heaps\binaryHeaps), which takes
# O(log(n)), n being number of nodes in binomial heap, since the height of the binomial heap is log2(n), since the
# height of Bk is k, and the number of nodes in the tree is 2**k = n, so height == k == log2(n).


# DELETE

# To do this, just use the extract min and decrease key subroutines: the node to be deleted is decreased using
# decrease key to -infinity (or any value smaller than current minimum); because decrease key is used, it becomes the
# node in the min position. We then use extract min. Decrease key is O(log(n)) and so is extract min, so DELETE has a
# complexity of O(log(n)).


# FOR BINOMIAL HEAP CODE, SEE https://www.geeksforgeeks.org/implementation-binomial-heap/ (FROM A DIFFERENT WEBSITE)
# AND https://www.youtube.com/channel/UChjlYGbn1bX7gXLq9c9dnBg (A VIDEO)