# Queues are useful for tracking requests for a limited resource, e.g. a printer.

# Queues are also useful for implementing graph algorithms.

# 1st: with an array

queue = []

# # Adding elements only to end of array (O(1) in time)
# queue.append('a')
# print(queue)
#
# queue.append('b')
# print(queue)
#
# # Removing elements from the front of a queue (O(n) in time)
# queue.pop(0)
# print(queue)

# Maximally efficient queue is O(1) in time

# 2nd: with a linked list

class QueueNode:

    def __init__(self, val):
        self.val = val
        self.next_node = None

class Queue:
    """Enqueue and dequeue are both O(1) in time."""

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, val):
        new_node = QueueNode(val)
        if self.size == 0:
            self.front = new_node
        else:
            self.back.next_node = new_node
        self.back = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        # If you don't have the below conditional, then when the queue is emptied by dequeueing, self.back will still
        # be the last Node that was present in the queue.
        elif self.size == 1:
            self.back = None
        dequeuedNode = self.front
        self.front = self.front.next_node
        self.size -= 1
        return dequeuedNode.val

queue1 = Queue()
print(queue1.size)

queue1.enqueue('a')
queue1.enqueue('b')
queue1.enqueue('c')
print(queue1.size)
# print(queue1.front.val)
# print(queue1.back.val)

print(queue1.dequeue())
print(queue1.size)
print(queue1.dequeue())
print(queue1.size)
print(queue1.front.val, queue1.back.val)

print(queue1.dequeue())
print(queue1.size)

print(queue1.dequeue())
print(queue1.size)

