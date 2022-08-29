# This is cool. Basically, the question gives you an array that is unsorted and asks to find the 2nd largest item.
# Can do this by using a min-heap, and adding to the min-heap from the array until the min-heap has 2 elements, then
# the next time a 3rd element is added to the mix, the minimum value of the heap is removed if smaller than added item,
# and then continue until the array is finished and there are 2 elements in the heap. Of course, will have to allow for
# edge cases, for example if there is not 2nd largest item in the array.

# Can always use peek (i.e. get-min) to see if an element is worth adding to the heap. Otherwise, for when we are
# looking for (say) the 100th largest element, if the heap then has 100 elements, we are going to add the new element
# as a leaf, then sift up; if it gets to the top of the heap, we will just be removing the same element we just added,
# which would be a waste of time.

# Time complexity: O(n)
# Auxiliary space complexity: O(1), as the heap is always of size 2

# Long video to explain more: https://www.youtube.com/watch?v=hGK_5n81drs, especially 4:30 onwards.