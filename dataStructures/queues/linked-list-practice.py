from logging.config import valid_ident


class Node:
    def __init__(self, val):
        self.val = val
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

class Queue:

    def __init__(self, capacity=float('inf')):

        self.back = self.front = None
        self.length = 0
        self.capacity = capacity

    def enqueue(self, val):

        if self.is_full():
            print("Sorry, the queue is full")
            return

        enqueued_back = Node(val)

        if self.is_empty():
            self.front = enqueued_back

        else:
            self.back.next_node = enqueued_back

        self.back = enqueued_back
        self.length += 1

    def dequeue(self):

        if self.is_empty(): return None

        elif self.length: self.back = None

        dequeued_front = self.front
        self.front = dequeued_front.next_node
        self.length -= 1

        return dequeued_front.val

    def peek(self):

        return self.front.val

    def is_empty(self):

        return self.length == 0

    def is_full(self):

        return self.length == self.capacity