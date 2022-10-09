# https://docs.python.org/3/library/heapq.html

# heappush(), heappop(), heappushpop() and heapreplace() only work properly when 
# the object they are invoked on is correctly a min-heap

# In the case of the heapq library, _siftup occurs from the root toward the 
# leaves, while _siftdown occurs from the leaves toward the root

# YouTube video on this: https://www.youtube.com/watch?v=58cYFs_W2_s&t=579s, 
# although it leaves out the merge() function