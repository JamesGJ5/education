from typing import Union

def linear_search(arr, x) -> Union[int, None]:
    """Takes an array and returns the index of the first occurrence of x if it is in the array, or None otherwise.

    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    """

    for i, element in enumerate(arr):

        if element == x:
            return i

    return None


# def binary_search(arr, x) -> Union[int, None]:
#     """Takes a sorted array and returns the index of the first occurrence of x if it is in the array, or None otherwise.
#     Uses recursion.
#
#     Time complexity: O(log(n))
#     Auxiliary space complexity: O(log(n)), as that's how the number of times _binary_search can be called (and thus
#         the maximum stack depth, too) scales
#     """
#
#     # What we want this to do is first compare x to the midpoint of the array if odd in length, or the rounded-up
#     # midpoint if the array is even in length. If x is greater than this midpoint, then we call the function with the
#     # upper slice of this array. If x equals the midpoint, return the index of this midpoint. If x is smaller than the
#     # midpoint, then we call the function with the lower slice of this array.
#
#     # Base case: when the array is empty, return None
#
#     # In order to make the index easy to return even if we find it in a stack frame besides the main frame, it might be
#     # easier to permit the function called to take the array and x, but a helper function to take the array, x, start
#     # and end.
#
#     start = 0
#     end = len(arr) - 1
#
#     return _binary_search(arr, x, start, end)
#
#
# def _binary_search(arr, x, start, end):
#     """Performs the binary search, returning the index of x when it finds it or adjusting start and end and calling
#     itself again."""
#
#     if start > end: return None
#
#     midpoint = (start + end) // 2
#
#     if x < arr[midpoint]:
#         end = midpoint - 1
#
#     elif x == arr[midpoint]: return midpoint
#
#     else:
#         start = midpoint + 1
#
#     return _binary_search(arr, x, start, end)


def binary_search(arr, x) -> Union[int, None]:
    """Takes a sorted array and returns the index of the first occurrence of x if it is in the array, or None otherwise.
    Iterative solution.

    Time complexity: O(log(n))
    Auxiliary space complexity: O(1)
    """

    start = 0
    end = len(arr) - 1

    while start <= end:

        midpoint = (start + end) // 2

        if x < arr[midpoint]:
            end = midpoint - 1

        elif x == arr[midpoint]: return midpoint

        else:
            start = midpoint + 1

    return None


# For breadth-first search, this applies to a graph. If starting from a given node and looking for another node
# while starting the path from the former node, see Line 98 of C:\Users\james\PycharmProjects\graphs\graphs\youTube1.py,
# i.e. the function "has_path" (which I think is commented out) that uses a "breadth-first traversal". This is
# iterative, because using recursion for a breadth-first traversal is not so intuitive--a breadth-first traversal uses
# a queue, following the FIFO principle, while recursion is stack-based, following the LIFO principle.

# For depth-first search, this applies to a graph. If starting from a given node and looking for another node
# while starting the path from the former node, see Line 113 of C:\Users\james\PycharmProjects\graphs\graphs\youTube1.py,
# i.e. the function "has_path" (which I think is commented out) that uses a "recursive breadth-first traversal". See
# Line 83 (two function definitions earlier) for the iterative version.

# Dijkstra's algorithm applies to a graph with weighted edges. It tells you the shortest distance (if we treat said
# weights as distances) between a given node and every other node in the graph; inaccessible nodes will be said to have
# a distance of float('inf') from the source node.



if __name__ == '__main__':

    a1 = [1, 2, 3, 4, 5, 6]
    a2 = []

    # print(linear_search(a1, 0))
    print(binary_search(a1, 2))