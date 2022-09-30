def insertion_sort(arr):
    """Takes an array and implements insertion sort on it, returning the array sorted in ascending order. Stable
    sorting algorithm. https://www.youtube.com/watch?v=nKzEJWbkPbQ&t=391s

    Time complexity:
        Worst case: O(n**2)
    Auxiliary space complexity: O(1)
    """

    # Here, we iterate from the beginning of the array to the end, each time comparing the element at the current
    # iteration stage with the one before it and swapping that same element as many times towards the beginning of the
    # array as necessary.

    # Need a variable to store the current element, then reassign element it is swapping with to the current element's
    # position, and the current element to the swapped element's old position, then continue.

    for i in range(1, len(arr)):
        current = arr[i]
        j = i

        while j > 0 and arr[j - 1] > current:

            arr[j] = arr[j - 1]

            j -= 1

        # Doing this at the end avoids unnecessary assignment operations in the mean time
        arr[j] = current

    return arr

def selection_sort(arr):
    """Takes an array and implements selection sort on it, returning the array sorted in ascending order. Stable
    sorting algorithm. See https://www.youtube.com/watch?v=EwjnF7rFLns

    Time complexity:
        Worst case: O(n**2)
    Auxiliary space complexity: O(1)
    """

    # Here, first create a variable min. We then start at the index i. While having a pointer at the
    # first index, we iterate through all consecutive indices, storing the lowest value that has been found at any
    # point in the variable min (and it must be smaller than arr[i]), along with its index j. When this iteration has
    # finished, we give the element at index i to the element at index j, then give the value in min to the element at
    # index i. We don't allow i to be the highest index in the array.

    for i in range(len(arr) - 1):
        idx_of_min = i

        j = i + 1
        while j < len(arr):

            if arr[j] < arr[idx_of_min]:

                idx_of_min = j

            j += 1

        arr[i], arr[idx_of_min] = arr[idx_of_min], arr[i]

    return arr


def bubble_sort(arr):
    """Takes an array and implements bubble sort on it, returning the array sorted in ascending order. Stable
    sorting algorithm. See https://www.youtube.com/watch?v=uJLwnsLn0_Q&t=412s.

    Time complexity:
        Worst case: O(n**2)
    Auxiliary space complexity: O(1)
    """

    # Starting with index i = 0, we compare arr[i] with arr[i + 1] and swap if the former is bigger than the latter.
    # Whether we do the swap or not, we then increment i and repeat all the way down the array. We repeat this entire
    # process for a number of times equal to len(arr)

    # I just put len(arr) - 1 because the last element remaining (x) at the beginning will always be in the correct place. This 
    # is because, in one pass of bubble sort (i.e. one iteration in the for loop, call this a bubble-up), the smallest element, wherever it is in the 
    # array, will move 1 place closer to the front of the array if it isn't there already. So, say this element is at the end 
    # of the array, at index len(arr) - 1; then, to get to index 0, the number of times it must move by 1 would be 
    # [len(arr) - 1 - 0 / 1] = len(arr) - 1, so it would be in the correct place (at the front) in len(arr) - 1 bubble-ups.
    for i in range(len(arr) - 1):

        j = 0
        while j + 1 < len(arr):

            if arr[j] > arr[j + 1]:

                arr[j + 1], arr[j] = arr[j], arr[j + 1]

            j += 1

    return arr


# def quick_sort(arr):
#     """Takes an array and implements quick sort on it, returning the array sorted in ascending order. Unstable
#     sorting algorithm (take the example of [2, 2, 1], where the 2s will swap). See
#     https://www.youtube.com/watch?v=Vtckgz38QHs, although I didn't use the same code here.
#
#     Time complexity:
#         Best case: n*log(n), if the pivot is the median of the array
#         Average case: n*log(n)
#             (https://www.quora.com/In-practice-how-often-is-average-case-time-complexity-analysis-performed)
#         Worst case: n**2, if the array is:
#             sorted, in which case subsequent recursions will take a version of the previous array with its LAST element
#                 popped each time;
#             or in the reverse order to sorted, in which case subsequent recursions will take a version of the previous
#                 array with its FIRST element popped each time
#     Auxiliary space complexity: O(n), so not as good as the code in the video
#
#     """
#
#     # We initialise two variables: i = -1 and j = 0. These point to different parts of the list. 'i' should really point
#     # to the element before the 0th, but really it points to the end of the list. However, that is fine because it
#     # won't do anything to its element until it is incremented for the first time. The element at the end of the list
#     # is called the 'pivot'. What we do is compare arr[j] with the pivot. If arr[j] < pivot (or if arr[j] is the end of
#     # the list, i.e. at the pivot), we increment i and swap arr[i] with arr[j], then we increment j and continue;
#     # otherwise, we increment j alone and continue. When the pivot has finally been swapped with arr[i], what we do
#     # then is go to the pivot's new position and call the function recursively on the list R ahead of it (which should
#     # only contain values greater than the pivot) and that before it, list L, which should only contain values smaller
#     # than or equal to the pivot.
#     # If arr[j] is ever not the same element as the pivot but has a value the same as it, we do the same as we would if
#     # it was the pivot: increment i and swap arr[i] with arr[j]--this is to ensure that this value ends up in L, so
#     # that the sorting algorithm is more stable. Also, we have decided that L will contain values smaller than or equal
#     # to the pivot. Moreover, in L, the new pivot will be smaller than or equal to the duplicate, so the duplicate will
#     # be in the new pivot's subtree and eventually end up next to the original pivot. Base case for the recursion: when
#     # len(arr) == 0.
#
#     if len(arr) == 0:
#
#         return arr
#
#     i, j = -1, 0
#
#     while j < len(arr):
#
#         if arr[j] <= arr[-1]:
#
#             MAJORLY USEFUL POINT: THE NUMBER OF TIMES THAT i IS INCREMENTED IS EQUAL TO THE NUMBER OF ELEMENTS THAT
#             ARE SMALLER THAN OR EQUAL TO THE VALUE OF THE PIVOT. THEREFORE, THE PIVOT ENDS UP IN ITS CORRECT POSITION
#             IN THE SORTED ARRAY, WITHOUT ANYMORE MOVEMENTS OF IT BEING NEEDED, AFTER IT IS SWAPPED TO THE FINAL
#             POSITION OF i.
#             i += 1
#
#             arr[i], arr[j] = arr[j], arr[i]
#
#         j += 1
#
#     return quick_sort(arr[: i]) + arr[i: i + 1] + quick_sort(arr[i + 1:])


def quick_sort(arr, start: int, end: int):
    """Takes an array and implements quick sort on it, returning the array sorted in ascending order. Unstable
    sorting algorithm (take the example of [2, 2, 1], where the 2s will swap). See
    https://www.youtube.com/watch?v=Vtckgz38QHs, I did use the same code here.

    arr: array to be sorted
    start: start index
    end: end index

    Time complexity:
        Best case: n*log(n), if the pivot is the median of the array
        Average case: n*log(n)
            (https://www.quora.com/In-practice-how-often-is-average-case-time-complexity-analysis-performed)
        Worst case: n**2, if the array is:
            sorted, in which case subsequent recursions will take a version of the previous array with its LAST element
                popped each time;
            or in the reverse order to sorted, in which case subsequent recursions will take a version of the previous
                array with its FIRST element popped each time
    Auxiliary space complexity: O(log(n)), because 2 recursive stack frames are formed in each recursive call, to a stack depth
        of log2(n), and only log2(n) stack frames are on the stack at any time; each stack contains the same space,
        it's not like a new array is being made each time since it is the reference to the same list being passed to
        the function calls each time.
    """

    # Base case
    if end <= start: return

    # Sorting array in place, no sub arrays
    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)

    return arr


def partition(arr, start: int, end: int) -> int:
    """Sorts array and finds index of pivot"""

    pivot = arr[end]
    i = start - 1

    j = start
    while j < end:
        if arr[j] < pivot:

            # MAJORLY USEFUL POINT: THE NUMBER OF TIMES THAT i IS INCREMENTED IS EQUAL TO THE NUMBER OF ELEMENTS THAT
            # ARE SMALLER THAN OR EQUAL TO THE VALUE OF THE PIVOT. THEREFORE, THE PIVOT ENDS UP IN ITS CORRECT POSITION
            # IN THE SORTED ARRAY, WITHOUT ANYMORE MOVEMENTS OF IT BEING NEEDED, AFTER IT IS SWAPPED TO THE FINAL
            # POSITION OF i.
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    # This is swapping the pivot itself to its final position
    i += 1
    arr[i], arr[j] = arr[j], arr[i]

    return i


def merge_sort(arr):
    """Takes an array and implements recursive merge sort on it, returning the array sorted in ascending order. Stable
    sorting algorithm.

    Time complexity:
        Worst case: O(n*log(n)), since there are log2(n) recursive rows and n elements per row, so n comparisons per
            row
    Auxiliary space complexity: O(n), see paper
    """

    # 1. If the array passed has a length of 0 or 1, simply return it. Otherwise, split the array in half (or as near to
    # half as possible) and merge sort each array.
    # 2. After each array has been merge sorted, time to compare the two arrays. Initialise two variables, 'i' and 'j', as
    # zero, and initialise a sorted_whole array.
    # 4. As long as both i and j are smaller than the length of the merge-sorted left and right arrays respectively,
    # there are still elements left to compare, so do the following:
    #   a. Compare left[i] to right[j]. If left[i] <= right[j], add left[i] to sorted_whole and increment i.
    #   b. Otherwise, add right[j] to the sorted_whole and increment j.
    # 5. Add the remaining elements of left to sorted_whole, then the remaining elements of right.

    if len(arr) == 1:

        return arr

    sorted_left = merge_sort(arr[: len(arr) // 2])
    sorted_right = merge_sort(arr[len(arr) // 2:])

    sorted_array = []

    i, j = 0, 0

    while i < len(sorted_left) and j < len(sorted_right):

        if sorted_left[i] <= sorted_right[j]:

            sorted_array.append(sorted_left[i])

            i += 1

        else:

            sorted_array.append(sorted_right[j])

            j += 1

    return sorted_array + sorted_left[i: ] + sorted_right[j: ]


def merge_sort(arr):
    """Takes an array and implements iterative merge sort on it, returning the array sorted in ascending order. Stable sorting
    algorithm.

    Time complexity:
        Worst case: O(n*log(n)), since there are log2(n) recursive rows and n elements per row, so n comparisons per
            row
    Auxiliary space complexity: O(n), see paper
    """

    # 1. Taking a bottom-up approach, so starting from the idea of the array being split into individual elements, then
    # building them up into a sorted array.
    # 2. Initialise i = 0. While i < len(arr), do the following:
    #   a) Compare the first element to the second element, and swap if the latter is smaller than the former.
    #   Increment i by 2.
    #   b) Continue step a) until the condition of i < len(arr) is no longer satisfied.
    # 3.

    i = 0
    while i < len(arr):

        if arr[i] > arr[i + 1]:

            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        i += 2


def timsort():
    """What Python's sort function uses.
    
    Worst-case time complexity: O(nlogn)
    Worst-case auxiliary space complexity: O(n)
    """
    pass


if __name__ == '__main__':

    x = [3, 2, 1, 6, 2, 7]

    # print(insertion_sort(x))
    # print(selection_sort(x))
    # print(bubble_sort(x))
    # print(quick_sort(x, 0, len(x) - 1))
    # print(quick_sort(x))
    # print(merge_sort(x))