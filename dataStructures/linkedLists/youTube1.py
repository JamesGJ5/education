from typing import Union

class Node:
    # Storing value in node and reference to next node in linked list

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

def print_linked_list(head: Node) -> None:
    """Takes a node in a linked list and traverses the section of the linked list it is at the head of, printing the
    value at each node encountered.

    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    """
    # TODO: use accurate time profiling to confirm that the iteration below really does take less time than the
    #   commented-out recursion even further below
    while head:
        print(head.val)
        head = head.next_node

    # Time complexity: O(n)
    # Auxiliary space complexity: O(n), because of the space for each recursive call
    # if not head: return
    # print(head.val)
    # print_linked_list(head.next_node)

# def linked_list_to_list(head: Node) -> None:
#     """Takes a node in a linked list and converts the segment of the linked list it's the head of to a list. Uses
#     iteration.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     l = []
#     while head:
#         l.append(head.val)
#         head = head.next_node
#
#     return l

def linked_list_to_list(head: Node, l: list = []) -> None:
    """Takes a node in a linked list and converts the segment of the linked list it's the head of to a list. The list
    passed to this function as an argument is extended by the resultant list. Uses recursion.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    if not head: return

    l.append(head.val)
    linked_list_to_list(head.next_node)

    return l

def linked_list_sum(head: Node) -> float:
    """Takes a node in a linked list and returns the sum of its elements. Done by iteration.

    Time complexity: O(n)
    Auxiliary space complexity: O(n) if the sum is a sequence (like a string), O(1) if the sum is a number
    """
    sum = head.val
    while head.next_node:
        head = head.next_node
        sum += head.val

    return sum


# def linked_list_sum(head: Node) -> float:
#     """Takes a node in a linked list and returns the sum of its elements. Done by recursion.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n), because of space for each recursive call
#     """
#     if not head.next_node:
#         return head.val
#     else:
#         return head.val + linked_list_sum(head.next_node)#

def linked_list_check(head: Node, val) -> bool:
    """Returns True if the given value is the value of a node in the linked list. Head is the node at the head of the
    linked list. Uses iteration.

    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    """
    while head:
        if head.val == val:
            return True
        head = head.next_node
    return False

# def linked_list_check(head: Node, val) -> bool:
#     """Returns True if the given value is the value of a node in the linked list. Head is the node at the head of the
#     linked list. Uses recursion.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     if not head:
#         return False
#     elif head.val == val:
#         return True
#     else:
#         return linked_list_check(head.next_node, val)

def linked_list_get(head: Node, idx: int):
    """For a given index (idx), returns the value of the node at that index in a zero-indexed linked list that head
    appears at the start of. Uses iteration.

    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    """
    count = 0

    while head:
        if count == idx:
            return head.val
        head = head.next_node
        count += 1

    if not head:
        raise Exception("idx provided doesn't correspond to position in linked list/no node was initially provided.")

# def linked_list_get(head: Node, idx: int):
#     """For a given index (idx), returns the value of the node at that index in a zero-indexed linked list that head
#     appears at the start of. Uses recursion.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     if not head:
#         raise Exception("idx provided doesn't correspond to position in linked list/node was initially provided.")
#     elif idx == 0:
#         return head.val
#     else:
#         return linked_list_get(head.next_node, idx-1)

def reverse_linked_list(head: Node) -> Node:
    """Reverses a linked list given the Node at the head of it. Returns the head Node of the new linked list. Uses
    iteration.

    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    """
    new_next = None
    while head:
        old_next = head.next_node
        head.next_node = new_next
        new_next = head
        head = old_next

    return new_next

# def reverse_linked_list(head: Node, new_next: Union[None, Node] = None) -> Node:
#     """Reverses a linked list given the Node at the head of it. Returns the head Node of the new linked list. Uses
#     recursion.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     if not head:
#         return new_next
#
#     old_next = head.next_node
#     head.next_node = new_next
#
#     return reverse_linked_list(head=old_next, new_next=head)

# def zip_linked_lists(head1: Node, head2: Node) -> None:
#     """Zips two linked lists, which at first begin with Nodes head1 and head2 respectively. head1 shall begin the head
#     of the zipped linked list. Uses iteration.
#
#     Time complexity: O(min(n, m)) (there will be 2*min(n, m) reassignments)
#     Auxiliary space complexity: O(1)
#     """
#     head = head1
#     new_next = head2
#
#     while head:
#
#         old_next = head.next_node
#         head.next_node = new_next
#         head = head.next_node
#         new_next = old_next
#
#         if not old_next:
#             return

def zip_linked_lists(head1: Node, head2: Node) -> None:
    """Zips two linked lists, which at first begin with Nodes head1 and head2 respectively. head1 shall begin the head
    of the zipped linked list. Uses recursion.

    Time complexity: O(min(n, m)) (there will be 2*min(n, m) reassignments)
    Auxiliary space complexity: O(min(n, m)) (there will be 2*min(n, m) reassignments and 1 recursive call per
        reassignment)
    """
    if not head2:
        return

    old_next = head1.next_node
    head1.next_node = head2
    head1 = head2
    head2 = old_next

    zip_linked_lists(head1, head2)

if __name__ == '__main__':
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    q = Node(1)
    r = Node(2)
    s = Node(3)
    t = Node(4)
    u = Node(5)
    v = Node(6)

    a.next_node = b
    b.next_node = c
    c.next_node = d

    q.next_node = r
    r.next_node = s
    s.next_node = t
    t.next_node = u
    u.next_node = v


    # print(linked_list_to_list(a))
    # print(linked_list_sum(a))
    # print(linked_list_check(a, 'E'))
    # print(linked_list_get(a, 0), linked_list_get(a, 3))

    # new_head = reverse_linked_list(a)
    # print_linked_list(new_head)

    zip_linked_lists(a, q)
    print_linked_list(a)