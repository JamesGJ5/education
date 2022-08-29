from typing import Any

# Can use a stack to track browser history (3:46)

# A stack may be considered as an abstract data structure

# To implement a stack, must just make sure to implement a method for pushing and popping

# Let's say last element of this array is top of stack
# stack1 = []
# print(stack1)
# stack1.append('a')
# print(stack1)
# stack1.append('b')
# print(stack1)
# stack1.pop()
# print(stack1)
# stack1.pop()
# print(stack1)

# To be maximally efficient, a stack data structure must do push/pop in O(1).

# As long as you append/pop to end of array in Python (and not the front, which would necessitate much shifting), this
# is satisfied.

# In Python, lists are optimised for popping and appending.

# Can implement stacks using linked lists.


class StackNode:
    """A Node that can form part of a stack.

    val: Any
    next_node: Union[None, Node]
    """

    def __init__(self, val: Any = None):
        self.val = val
        self.next_node = None

    # def __str__(self):
    #     return f'Node value: {self.val}\nNext Node: {self.next_node}'


class Stack:
    """Creates a stack in which Nodes point from the top of the stack to the bottom."""


    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        # I think it would be easier to have next_node be a parameter of StackNode's instantiation. Then the below
        # conditional would not be needed, as next_node could be None?
        next_top = StackNode(val)
        if self.size > 0:
           next_top.next_node = self.top
        self.top = next_top
        self.size += 1

    def getTop(self):
        return self.top.val

    def pop(self):
        if self.size == 0:
            return None
        else:
            popped_top = self.top.val
            self.top = self.top.next_node
            self.size -= 1
            return popped_top


stack1 = Stack()
stack1.push('a')
stack1.push('b')
stack1.push('c')
# print(stack1.top)
# print(stack1.getTop())

print(stack1.size)
print(stack1.pop())
print(stack1.size)
print(stack1.pop())
print(stack1.size)
print(stack1.pop())
print(stack1.size)
print(stack1.pop())

# push and val both run in complex time, and linear total space