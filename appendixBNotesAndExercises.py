# ANALYSIS OF ALGORITHMS

# B.1: Order of growth

# See Pages 201 and 202 for why the following actions can be beneficial: specifying a machine model under while
# algorithm run time and space apply, considering the worst case scenario re: run time and space, specifying the run
# time as a function of problem size, and grouping functions into categories depending on how quickly they gro as
# problem size increases.

# The latter activites can be replaced by simply using big-O notation.

# Crossover point is where an algorithm with an O(n**2) time complexity becomes, as n rises, worse re: time than a
# function with an O(n) time complexity. The location of the crossover point depends on the details of the algorithms,
# input and hardware, so is usually ignored for purposes of algorithmic analysis, but don't forget about it.

# An order of growth is a set of functions (like 2n, 100n and n + 1) whose growth behavior is considered equivalent.

# In O(log.b(n)), the base (b) doesn't matter because changing bases is the equivalent of multiplying by a constant
# (independent of n), which doesn't change the order of growth.

# Orders of growth from best to worst:

# O(1) (constant)
# O(log.b(n)) (logarithmic (for any b))
# O(n) (linear)
# O(n*log.b(n)) (linearithmic)
# O(n**2) (quadratic)
# O(n**3) (cubic)
# O(c**n) (exponential (for any c))

# Exercise B.1:

# 1. Cubic order of growth for all.
# 2. Cubic order of growth.

# https://en.wikipedia.org/wiki/Big_O_notation was used to answer the below, paying particular attention to the
# 'Properties' section of the linked article.
# 3. If f is in O(g), a multiplication of f by constant 'a' is also in O(g). Addition by constant 'b' doesn't change
# the order of growth, so af + b is also in O(g).
# 4. If f1 and f2 are in O(g), f1 + f2 is a subset of O(g).
# 5. If f1 is in O(g) and f2 is in O(h), then f1 + f2 is in O(max(g, h))
# 6. If f1 is in O(g) and f2 is O(h), f1.f2 is O(g.h)


# B.2: Analysis of basic Python operations

# In Python, most arithmetic operations are constant time. However, for very large integers, the run time may increase
# significantly with the number of digits.

# Indexing operations—reading or writing elements in a sequence or dictionary—are also
# constant time, regardless of the size of the data structure.

# A for loop that traverses a sequence or dictionary is usually linear (O(n)), as long as all of the
# operations in the body of the loop are constant time. For example, adding up the elements
# of a list (here, t) is linear:

# total = 0
#     for x in t:
#     total += x

# The built-in function sum is also linear because it does the same thing, but it tends to be
# faster because it is a more efficient implementation; in the language of algorithmic analysis,
# it has a smaller leading coefficient.

# As a rule of thumb, if the body of a loop is in O(n**a) then the whole loop is in O(n**(a+1)). The exception is if you
# can show that the loop exits after a constant number of iterations. If a loop runs k times regardless of n, then the
# loop is in O(n**a), even for large k, because the complexity will really be k (constant number of times the body
# runs) * O(n**a) (complexity of body) which is simply O(n**a) in Big-O notation.

# Dividing by a constant doesn't change the order of growth either, so if a body of a loop is in O(n**a) and it runs
# n/k times, the loop is in O(n**(a+1)), even for large k.

# Most string and tuple operations are linear, except indexing (i.e. retrieving the element at a given index) and len,
# which are constant time.

# The built-in functions min and max are linear.

# The run-time of a slice operation is proportional to the length of the output, but independent of the size of the
# input.

# String concatenation is linear; the run time depends on the sum of the lengths of the
# operands.

# All string methods are linear, but if the maximum length the string can have is a constant—for example, operations on
# only single characters—they are considered constant time.

# The string method join is linear; the run time depends on the total length of the strings.

# Most list methods are linear, but there are some exceptions (see Page 204).

# Most dictionary operations and methods are constant time, but there are some exceptions:
# -> The run time of update is proportional to the size of the dictionary passed as a parameter (to update the
# dictionary being updated), not the dictionary being updated.
# -> Methods 'keys', 'values' and 'items' are constant time because they return iterators. But if you loop through the
# iterators, the loop will be linear.


# Exercise B.2:

# 1. A comparison sort is a sorting algorithm that takes the keys being sorted and compares only their magnitudes to
# each other, and uses no other properties of the keys, to sort the keys in ascending order, for example. For example,
# in merge sort, when rebuilding the sorted array after breaking it up into its elements, magnitude comparisons are
# made at every level.
# n.log(n) is the best 'worst case' order of growth for a COMPARISON SORT. This is the worst case scenario for merge
# sort, introsort, heapsort, block sort, timsort (combines merge sort and insertion sort), cubesort...
# O(n) is the best 'worst case' order of growth for ANY SORTING ALGORITHM.  This is only the worst case scenario for
# NON-COMPARISON SORTS like spreadsort, LSD (Least Significant Digit) radix sort, MSD radix sort...

# 2. Bubble sort's average and worst case order of growths are O(n**2), so it is bad for sorting large numbers of items
# (like 1 million 32-bit integers).

# 3. The order of growth for radix sort (in time) is O(d(n+b)). Here, d is the maximum number of
# digits in any of the sorted items, while b is the base of the sorted items (should be the same for each). As n->inf,
# O(d(n+b))->O(n).
# The sorted elements must be either integers, fixed size strings, floating points (i.e. can be decimal but has fixed
# number of significant figures), and to "less than", "greater than" or "lexicographic order" comparison predicates
# (but not simply of overall element magnitude).

# 4. If you have an array with repeated elements, a stable sort preserves the order of the repeated elements in the
# sorted array. For example, if you have two numbers "1" in the unsorted array but they represent different things
# (e.g. age of Tim and number of apples in bowl), you might want to preserve the order for some reason.

# 5. Bogosort: its best runtime is O(n), its average is (n x n!) and its worst is unbounded. It's not useful for
# sorting, it's more just to contrast with better algorithms. It shuffles the data randomly until it happens to be
# sorted.

# 6. The C library uses the quick-sort algorithm.; the Python library uses the Timsort algorithm (which combines merge
# sort and insertion sort). The former (quicksort) is NOT stable but the latter (Timsort) is stable.

# 7. The problem with non-comparison sorting is that their complexity is usually dependent on other parameters than the
# size of an input, whereas O(n.log(n)) comparison sorts tend to be less so. This is probably why Python uses the latter.


# B.3: Analysis of search algorithms

# Linear search (O(n)) traverses the items of the collection in order, stopping if it finds the target.

# The in operator for sequences uses a linear search; so do string methods like find and
# count.

# If the elements of the sequence are in order, you can use a bisection search (or binary search), which is O(log n).

# There is another data structure, called a hashtable that is even faster—it can do a search
# in constant time—and it doesn’t require the items to be sorted. O(1).

# Searches in Python (in, for example) generally use linear search.


# B.4: Hashtables

# See this section of the book for how hashtables work.

# Note: when expanding a hashtable (in order to permit each list
# in the hashtable to contain, on average, only 1 key, value tuple), the lists are all added to a hashtable that is
# twice as big (has twice the number of lists). This Rehashing has a time complexity of O(n), since you need to rehash
# (i.e. calculate a new index in the new hashtable for each pair) each entry sequentially. However, this expansion must
# only be done when the number of pairs in the hashtable reaches the capacity (number of lists in) the hashtable.
# Rehashing is done when this criterion is met so that each list remains with an average of 1 key, value tuple, because
# then searching for a key within a list has a time complexity of only O(1), and the list the key is deemed to be in
# is controlled by the key's hash value, so looking for the list takes O(1) complexity.

# I guess we start with 2 lists per hashtable so that we aren't taking up unnecessary space.

# The total number of units of work in adding n keys to a hashtable is a*n - a. When doubling as above, a is 2. Want to
# keep a*n - a low for time, so keep a as 2 (can't be any lower).

# We multiply capacity by a constant each time capacity is reached, rather than add a certain number to capacity with
# each addition, as the latter would involve O(n) complexity for each key addition because all keys would need
# rehashing each time capacity was increased (i.e. every time a new key was added). n is number of keys in hashtable
# before each addition.