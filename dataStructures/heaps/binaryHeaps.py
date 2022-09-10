import math

# In a min-heap, a parent node is always smaller than OR EQUAL TO any of its children in value.

# Keep a min-heap sorted and getting the smallest element is always O(1), because you know it's the root node.

# The most famous heap type is a binary heap.

# To be a heap, a binary tree must have all rows completely filled before beginning the filling of a final row.
# Moreover, in the array representing it (if it is an array), there can't be any unoccupied indices before the final
# index.

# In an array representing a heap, for a node at index i, parent node is at (i-1)//2, child nodes are at
# 2i + 1 and 2i + 2.
# See https://cs.stackexchange.com/questions/87154/why-does-the-formula-2n-1-find-the-child-node-in-a-binary-heap for why this is. Note, here, a "predecessor" of a node 
# is a node at the index before it, not necessarily its parent. Moreover, where it says i′=2**T − 1 + 2j, they get that from taking i=2**(T−1) − 1 + j (an index in the 
# array before the last one being considered) and replacing the T with T + 1, because the last array being considered is 1 ahead of its predecessor.

# Binary heap operations: insert, get min/max, extract min/max, update, build.

# To put a node into an array, you must then readjust its position to make it fit min/max-heap by using sift_up or
# sift_down. i.e. swap when smaller than parent or larger than parent, or vice versa with children.

# In sift_down, you swap with the smallest child (in min-heap).

# For a min-heap:

class min_heap:

    def __init__(self, contents=[]):

        # Don't necessarily want to modify in-place the list being passed.
        self.heap = contents.copy()

        # The time complexity of heapify is O(n). See paper for derivation of this, as well as why we start iterating
        # from the final leaf of the heap and make sure to do sift down rather than sift up.
        for i in range(len(self.heap))[::-1]:
            self._siftdown(i)

    # Note: _ before method name means it is used internally. For example, it might be called in another method, but I
    # guess it wouldn't be called outside of this class definition. Here, it is called in insert...
    def _siftup(self, i):
        """Time complexity: O(log(n)), where the base of the log is 2 in the case of a binary tree
        Auxiliary space complexity: O(1)
        """
        parent = (i - 1) // 2
        while i > 0 and self.heap[parent] > self.heap[i]:

            # Using tuple assignment is clearly a good way of swapping values
            self.heap[parent], self.heap[i] = self.heap[parent], self.heap[i]

            i = parent
            parent = (i - 1) // 2

    def _siftdown(self, i):
        """Time complexity: O(log(n)), where the base of the log is 2 in the case of a binary tree
        Auxiliary space complexity: O(1)
        """
        left = 2 * i + 1
        right = 2 * i + 2
        while ((left < len(self.heap) and self.heap[i] > self.heap[left]) or
            (right < len(self.heap) and self.heap[i] > self.heap[right])):

            # todo: figure out if the below priority-giving should indeed be done
            # Here, if both left and right child nodes are present and have equivalent values, priority is given in
            # swapping the parent node with the right child node.
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right

            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]

            i = smallest
            left = 2 * i + 1
            right = 2 * i + 2

    def insert(self, element):
        """Time complexity: O(log(n)), where the base of the log is 2 in the case of a binary tree
        Auxiliary space complexity: O(1)
        """
        self.heap.append(element)
        self._siftup(len(self.heap) - 1)

    def get_min(self):
        """Returns the minimum value of the heap, but doesn't remove it.

        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        """
        if len(self.heap) > 0: return self.heap[0]

    def get_max(self):
        """Returns the maximum value of the heap, but doesn't remove it.

        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        # Note: I haven't checked this solution
        num_full_rows = int(math.log(len(self.heap) + 1, 2))

        # 1 + 2**1 + 2**2 + 2**3 + ... is a geometric series where a=1 and r=2. Its sum for the nth element (the 1
        # being at n=1) is a * (r ** n - 1) / (r - 1). So, the capacity of the filled rows (before the final row).
        full_rows_capacity = 2 ** (num_full_rows - 1)

        return max[self.heap[full_rows_capacity:]]

    def extract_min(self):
        """Returns the minimum value of the heap and removes it.

        Time complexity: O(log(n))
        # Note: if we just removed the min value and then re-arranged the queue such that the None left the queue like a
        # vacancy, we'd have to move every single node back one (think of the array), which would be O(n). Swapping
        # min with the final leaf before extraction and then doing sift-down is just O(log(n)).
        Auxiliary space complexity: O(1)
        """
        # To remove the min (i.e. root node), first swap it with the last leaf node, then do whatever sifting is
        # necessary on that leaf node.
        if self.heap > 0:

            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

            min = self.heap.pop()
            self._siftdown(0)

            return min

    def update_by_index(self, i, new):
        """Updates the value of the node at index i to new.

        Time complexity: O(log(n))
        Auxiliary space complexity: O(1)
        """
        old = self.heap[i]
        self.heap[i] = new

        if new < old: self._siftup(i)

        else: self._siftdown(i)

    def update(self, old, new):
        """Updates all nodes in the heap with value old to a value of new.

        Time complexity: O(n), because the iteration is the part with the highest time complexity
        Auxiliary space complexity: O(1)
        """
        # Video method, which seems slow because you iterate when you do the for if statement and then you iterate when
        # looking for the index:
        # if old in self.heap:
        #     self.update_by_index(self.heap.index(old), new)

        for i, val in enumerate(self.heap):

            if val == old:
                self.update_by_index(i, new)

# Reverse operators and change some names to get max-heap. See link to code in video notes.

# Heaps can be used for sorting, a la heapsort:

def heapsort(arr):
    """Sorts arr in ascending order using a min-heap.

    Time complexity: O(nlog(n)), because for each node in the heap (of which there are n), you do _sift_down (which has
        an O(log(n)) time complexity). The video just goes into the specifics of what coefficient nlog(n) would be
        multiplied by, essentially, which is a bit extraneous for now.
    Auxiliary space complexity: O(n)
    """
    heap = min_heap(arr)
    return [heap.extract_min() for i in range(len(heap.heap))]

# So, auxiliary space complexity above is O(1), because in __init__ of min_heap, we COPY the array to self.heap;
# however, if we simply assign self.heap to the initial array rather than a copy of it, we can do heap operations in
# place, and thus heapsort would have an auxiliary space complexity of O(1). So, O(nlog(n)) and O(1) are great pairings,
# competitive with other sorting algorithms. However, heapsort isn't an unstable sorting algorithm, meaning it doesn't
# keep values in the initial array that are the same in the same order, so heapsort isn't always applicable.
# To visualise the reasons for the instability, take the array [1, 6, 8, 7, 7] for example and heapify it--you should
# find that, in the heapified array, the 7s are in a different order compared to the unheapified array.

# Heaps can also be used for priority queues (https://www.youtube.com/watch?v=7z_HXFZqXqc). A priority queue is like a
# queue, except that elements in the queue are
# arranged in a particular order. For example, if the queue contains GPAs of students and the queue is to free tutoring,
# you might want the lower GPAs to leave the queue first and thus allow the lower GPA students free tutoring first.
# For the front of the queue to be popped each time while following priority, the queue must re-sort after each
# addition to the back of the queue, in case the sorting breaks the order.

# In the above case, the priority queue would be a min-heap, and each time we enqueue, we add a new leaf; each time we
# dequeue, we remove first node via extract_min. In fact, full list of priority queue methods and their translation to
# heap methods:

# Enqueue: insert, O(logn), see in min_heap class definition
# Dequeue: extract_min O(logn)
# Peek, as in see element at front of priority queue: get_min O(1)
# Change priority, as in change the value of an element in the list at a certain index (or all elements of the list
#   with a certain value) and thus change its priority: update_by_index (or the method 'update'), which is O(log(n))
#   (or O(n))

# Note: if priority was given to higher values of priority queue, we'd use a max-heap instead.

# Note: my below is different from the video, especially since I used inheritance. Haven't tested it yet, though.
class PriorityQueue(min_heap):
    """Here, priority is given to smaller queue elements."""

    # def __init__(self):
    #     self.queue = min_heap()

    def enqueue(self, element):
        self.insert(element)

    def dequeue(self):
        return self.extract_min()

    def peek(self):
        return self.get_min()

    def change_priority_by_index(self, i, new):
        self.update_by_index(i, new)

    def change_priority(self, old, new):
        self.update(old, new)

    def is_empty(self):
        return len(self.queue.heap) == 0

# Don't want to reinvent the wheel, so in Python, use heapq for priority queues utilising heaps

# Priority queue is used in Dijkstra's algorithm, Huffman coding algorithm and Prim's algorithm

# One way in which heaps differ from binary search trees is that, for a given parent node, the left-hand child doesn't
# need to be smaller than the right-hand child, so you can have duplicates. See
# C:\Users\james\PycharmProjects\trees\youTube2.py for notes on binary search trees.