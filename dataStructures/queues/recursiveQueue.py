# Okay, first let's remind ourselves of the fundamentals of the queue data structure:
# - FIFO (first in, first out)
# - Typical methods:
# -- enqueue (add value to back of queue)
# -- dequeue (remove value at front of queue and return it)
# -- peek (return value at front of the queue but don't remove it)
# -- is_empty (return True if a queue is empty and False otherwise)
# -- is_full (return True if a queue is full and False otherwise)

# Now, a stack can simply be implemented via recursion, as each frame may make a recursive call, and then the newest frame must return before that which generated does, permitting a 
# last in, first out (LIFO) flow. However, queue's are FIFO, so by definition a single recursive stack would not work.

# However, it has been seen in questions1.py that a queue may be implemented using two explicit stacks. So, perhaps it may be implemented using two implicit (recursive) stacks, and 
# thus perhaps a queue may be implemented via recursion in that way.

# First, I will try to implement, without help, a queue via two explicit stacks.

class QueueViaStacks:

    def __init__(self, maxlen = float('inf')):
        self.inbox = []
        self.outbox = []
        self.size = 0
        self.maxlen = maxlen

    def enqueue(self, val):
        if self.is_full():
            print('Sorry, the queue is full')
            return
        else:
            self.inbox.append(val)
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print('Sorry, the queue is empty')
            return
        elif len(self.outbox) == 0:
            for _ in range(self.size):
                self.outbox.append(self.inbox.pop())
        self.size -= 1
        return self.outbox.pop()

    def peek(self):
        if self.is_empty():
            print('There is nothing in the queue')
            return
        elif len(self.outbox) == 0:
            return self.inbox[0]
        else:
            return self.outbox[-1]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxlen

def test_QueueViaStacks(object):
    print(object.__dict__)
    print(object.peek())
    print(object.is_empty())
    print(object.is_full())
    print()

q1 = QueueViaStacks(maxlen=5)
test_QueueViaStacks(q1)

q1.enqueue('a')
q1.enqueue('b')
test_QueueViaStacks(q1)

print(q1.dequeue())
test_QueueViaStacks(q1)

q1.enqueue('c')
test_QueueViaStacks(q1)

print(q1.dequeue())
test_QueueViaStacks(q1)

q1.enqueue('d')
q1.enqueue('e')
q1.enqueue('f')
q1.enqueue('g')
test_QueueViaStacks(q1)

q1.enqueue('h')
test_QueueViaStacks(q1)