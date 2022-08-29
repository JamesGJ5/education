# Code challenges: Q2: Suppose we have two stacks and no other temporary variable. Is to possible to "construct" a
# queue data structure using only the two stacks?

# Used https://www.youtube.com/watch?v=Wg8IiY1LbII for help

class Node:
    """Each Node contains a value as well as a reference to the Node it points to in a linked list.

    val: Any
    next_node: Union[None, Node]
    """

    def __init__(self, val):
        self.val = val
        self.next_node = None

class Stack:
    """A Stack is a linear sequence of linked Nodes, in which Nodes can only be added to or removed from the top of the
    stack and each Node's 'next node' is lower down in the stack than 'it' is.

    top: Union[None, Node]
    size: int
    """

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        new_top = Node(val)
        # Note that instead of using the conditional below, could have its body but without the conditional statement.
        # Then, the Node at the bottom of the stack would always have None as next_node. However, chose to do it this
        # way to avoid the wasted operation of reassigning a Node's next_node to None if it is a new top node and it is
        # being added to an empty stack.
        if self.size > 0:
            new_top.next_node = self.top
        self.top = new_top
        self.size += 1

    def pop(self):
        if self.size > 0:
            popped_val = self.top.val
            self.top = self.top.next_node
            self.size -= 1
            return popped_val
        else:
            return None

    def identify_top(self):
        return self.top.val

class Queue(Stack):
    """Contains two stacks: an inbox and an outbox. Acts as a queue in the manner explained in the YouTube video at
    https://www.youtube.com/watch?v=Wg8IiY1LbII
    """

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def size(self):
        return self.inbox.size + self.outbox.size

    def identify_front(self):
        if self.outbox.size == 0:
            while self.inbox.size > 0:
                to_outbox = self.inbox.pop()
                self.outbox.push(to_outbox)
        return self.outbox.identify_top()

    def enqueue(self, val):
        self.inbox.push(val)

    def dequeue(self):
        if self.outbox.size == 0:
            while self.inbox.size > 0:
                to_outbox = self.inbox.pop()
                self.outbox.push(to_outbox)
        return self.outbox.pop()


# stack1 = Stack()
# stack1.push('a')
# stack1.push('b')
# stack1.push('c')
#
# print(stack1.size)
# print(stack1.pop())
# print(stack1.size)
# print(stack1.pop())
# print(stack1.size)
# print(stack1.pop())
# print(stack1.size)
# print(stack1.pop())

# Expected output:

# 3
# c
# 2
# b
# 1
# a
# 0
# None

# Expected output was reproduced yay


queue1 = Queue()
print(queue1.size())

queue1.enqueue('a')
queue1.enqueue('b')
queue1.enqueue('c')
print(queue1.size())

print(queue1.dequeue())
print(queue1.size())
print(queue1.dequeue())
print(queue1.size())
print(queue1.identify_front())

print(queue1.dequeue())
print(queue1.size())

print(queue1.dequeue())
print(queue1.size())

# Expected output:

# 0
# 3
# a
# 2
# b
# 1
# c
# c
# 0
# None
# 0