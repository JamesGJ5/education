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

# q1 = QueueViaStacks(maxlen=5)
# test_QueueViaStacks(q1)

# q1.enqueue('a')
# q1.enqueue('b')
# test_QueueViaStacks(q1)

# print(q1.dequeue())
# test_QueueViaStacks(q1)

# q1.enqueue('c')
# test_QueueViaStacks(q1)

# print(q1.dequeue())
# test_QueueViaStacks(q1)

# q1.enqueue('d')
# q1.enqueue('e')
# q1.enqueue('f')
# q1.enqueue('g')
# test_QueueViaStacks(q1)

# q1.enqueue('h')
# test_QueueViaStacks(q1)

# Okay, the above seemed to work out pretty well. Now it is time to think about how I might replace self.inbox and self.outbox with implicit stacks (via recursion). 

# Well, to do this while maintaining the same methods, we'll have to address a few things:
# - self.inbox and self.outbox themselves. I guess we'd have to have a static recursive process that only returns when something must change. For example, if the queue 
#   at any given time should have 2 items in the outbox and 1 in the inbox, we don't want this to change before we modify the queue next so the recursive processes 
#   can't return as soon as they are called. Therefore, the base case (the top of the stack) must have some condition in it that prevents it from returning. I can 
#   think of the following things that could even somewhat permit that:
#   -- Dynamic programming, which I don't know much about
#   -- The input function, which waits for input from a user
#   -- Some kind of wait function from a time module, although it shouldn't have a maximum wait time in theory, instead it should wait infinitely long. However, 
#       there must be something that breaks the frame out of that waiting, so such a function wouldn't be sufficient

#   Moreover, I think it is worth listing when the stack must be interrupted:
#   -- When you enqueue, you must add another frame to the top of the inbox stack
#   -- When you want to dequeue and the outbox stack is empty but the inbox stack isn't (so you must move the inbox stack to the outbox stack but in reverse)
#   -- When you want to dequeue and the outbox stack is not empty, you must remove a frame from the top of it

#   Additionally, each stack frame must hold a value, otherwise what else is being enqueued and dequeued? Perhaps this value would be passed as an argument to the 
#   functional call that creates the frame.

# - enqueue. If the inbox stack has items in it, would probably have to make some sort of top-level call that affects the highest frame in the inbox stack somehow.
# - dequeue. If the queue isn't empty, would have to probably make a top-level call to remove a frame from the top of the outbox stack if it has items, or do this 
#   after making a top-level call that tells each frame, from the top of the inbox stack downwards, to enter the outbox stack
# - peek. If the stack has items, would involve seeing what is at the bottom of the inbox recursive stack (not too difficult maybe) or, slightly more difficult, seeing 
#   what is at the top of the outbox recursive stack, which would probably necessitate some top-level call.
# - is_empty and is_full could probably be implemented without touching the stack, just got to update self.size whenever enqueuing or dequeueing is done, however.

# So, all points to doing the following: learning how to affect a recursive frame from __main__.