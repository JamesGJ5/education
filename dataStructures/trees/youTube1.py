from typing import Union

# In a TREE, EDGES connect NODES, and nodes contain VALUES.

# In a BINARY TREE, every node is the PARENT to AT MOST TWO CHILDREN. Good to show off terminology like this in
# technical interviews.

# A ROOT is a node with no parent. A BINARY TREE should have exactly 1 root.

# LEAF nodes are nodes with no children, and can occur at different levels of a tree from one another.


# In a coding interview, they might not tell you what they are presenting you with is. To discover if it is a binary
# tree:

# Remember the criteria for a BINARY TREE:
#   <= 2 children per node
#   Exactly 1 root
#   Exactly 1 path between root and any node
#   todo: resolve the below query
#   According to the video, an empty tree (no nodes or edges) is considered a binary tree as well... but wouldn't an
#       empty tree have 0 roots, and thus not count?

# Even a tree with a single node fits the criteria above and is thus a binary tree.

# An empty tree is also considered a binary tree.

# A tree in which A's child is B, B's child is C and C's child is A is not a binary tree because all nodes have parents
# (so there are 0 roots) and there are infinite numbers of path from one node to another, since the tree is cyclical.


class Node:
    """A node in a binary tree."""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# def depth_first_values(root: Union[Node, None]):
#     """Takes a root Node object and returns, as elements of a list in order of when they were encountered, the values
#     of all of the Nodes in the binary tree it is a part of. Uses a iterative depth-first traversal. If root is None,
#     we have an empty tree.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n), because Nodes will be stored in a stack, but the number of Nodes in the stack
#         can't exceed n, because each Node can only have (at most) 1 parent Node.
#     """
#     values = []
#
#     if root:
#
#         stack = [root]
#         while len(stack) > 0:
#             current = stack.pop()
#             values.append(current.val)
#
#             if current.right: stack.append(current.right)
#             if current.left: stack.append(current.left)
#
#     return values


def depth_first_values(root: Union[Node, None]):
    """Takes a root Node object and returns, as elements of a list in order of when they were encountered, the values
    of all of the Nodes in the binary tree it is a part of. Uses a recursive depth-first traversal. If root is None,
    we have an empty tree.

    Time complexity: O(n)
    Auxiliary space complexity: O(n), because Nodes will be stored in a stack, but the number of Nodes in the stack
        can't exceed n, because each Node can only have (at most) 1 parent Node.
    """
    values = []

    if root:

        values.append(root.val)

        for child in root.left, root.right:
            values.extend(depth_first_values(child))

    return values


def breadth_first_values(root: Union[Node, None]):
    """Takes a root Node object and returns, as elements of a list in order of when they were encountered, the values
    of all of the Nodes in the binary tree it is a part of. Uses a breadth-first traversal. If root is None, we have
    an empty tree.

    Time complexity: O(n**2) because, for each Node in the list, you must remove it from the front of the queue; here,
        I do that inefficiently by popping from the front of the list (which means all elements down the line must
        shift, with O(n) time complexity)
    Auxiliary space complexity: O(n)
    """
    values = []

    if root:

        queue = [root]

        while len(queue) > 0:
            current = queue.pop(0)
            values.append(current.val)

            for child in current.left, current.right:
                if child:
                    queue.append(child)

    return values

# def tree_includes(root: Union[Node, None], target):
#     """Begins with the root Node of a binary tree and returns True if that tree contains a Node with a value 'target'
#     but False otherwise. Uses a breadth-first search. If root is None, we have an empty tree.
#
#    Time complexity: O(n**2) because, for each Node in the list, you must remove it from the front of the queue; here,
#        I do that inefficiently by popping from the front of the list (which means all elements down the line must
#        shift, with O(n) time complexity)
#     Auxiliary space complexity: O(n)
#     """
#     if root:
#
#         queue = [root]
#         while len(queue) > 0:
#
#             current = queue.pop(0)
#
#             if current.val == target:
#                 return True
#
#             for child in current.left, current.right:
#                 if child:
#                     queue.append(child)
#
#     return False

# def tree_includes(root: Union[Node, None], target):
#     """Begins with the root Node of a binary tree and returns True if that tree contains a Node with a value 'target'
#     but False otherwise. Uses an iterative depth-first search. If root is None, we have an empty tree.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     if root:
#
#         stack = [root]
#         while len(stack) > 0:
#
#             current = stack.pop()
#
#             if current.val == target:
#                 return True
#
#             for child in current.left, current.right:
#                 if child:
#                     stack.append(child)
#
#     return False


def tree_includes(root: Union[Node, None], target):
    """Begins with the root Node of a binary tree and returns True if that tree contains a Node with a value 'target'
    but False otherwise. Uses a recursive depth-first search. If root is None, we have an empty tree.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    if root:

        if root.val == target:
            return True

        return tree_includes(root.left, target) or tree_includes(root.right, target)

    return False

# def tree_sum(root: Union[Node, None]) -> float:
#     """Begins with the root Node of a binary tree and returns the sum of the values of all the Nodes in the tree, using
#     a breadth-first search. Note: for any null Nodes (non-existent node), the Node's value represents 0. If the
#     Node passed is None, we have an empty tree (and the Node is not actually a root). Also, the Node values must be
#     numbers.
#
#    Time complexity: O(n**2) because, for each Node in the list, you must remove it from the front of the queue; here,
#        I do that inefficiently by popping from the front of the list (which means all elements down the line must
#        shift, with O(n) time complexity)
#     Auxiliary space complexity: O(n)
#     """
#     sum = 0
#
#     queue = [root]
#     while len(queue) > 0:
#
#         current = queue.pop(0)
#         if current:
#             sum += current.val
#
#             for child in current.left, current.right:
#                 queue.append(child)
#
#     return sum

# def tree_sum(root: Union[Node, None]) -> float:
#     """Begins with the root Node of a binary tree and returns the sum of the values of all the Nodes in the tree, using
#     an iterative depth-first search. Note: for any null Nodes (non-existent node), the Node's value represents 0. If the
#     Node passed is None, we have an empty tree (and the Node is not actually a root). Also, the Node values must be
#     numbers.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     sum = 0
#
#     stack = [root]
#     while len(stack) > 0:
#
#         current = stack.pop()
#         if current:
#
#             sum += current.val
#
#             for child in current.left, current.right:
#                 stack.append(child)
#
#     return sum

def tree_sum(root: Union[Node, None]) -> float:
    """Begins with the root Node of a binary tree and returns the sum of the values of all the Nodes in the tree, using
    a recursive depth-first search. Note: for any null Nodes (non-existent node), the Node's value represents 0. If the
    Node passed is None, we have an empty tree (and the Node is not actually a root). Also, the Node values must be
    numbers.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    if not root: return 0

    return root.val + tree_sum(root.left) + tree_sum(root.right)

# def tree_min_value(root: Union[Node, None]) -> float:
#     """Takes the root Node of a binary tree and returns the minimum value of any of the Nodes in the binary tree. If
#     root is None, returns float('inf'). Uses a breadth-first traversal.
#
#     Time complexity: O(n**2) because, for each Node in the list, you must remove it from the front of the queue; here,
#       I do that inefficiently by popping from the front of the list (which means all elements down the line must
#       shift, with O(n) time complexity)
#     Auxiliary space complexity: O(n)
#     """
#     min_value = float('inf')
#
#     queue = [root]
#     while len(queue) > 0:
#
#         current = queue.pop(0)
#         if current:
#
#             min_value = min(min_value, current.val)
#
#             for child in current.left, current.right:
#                 queue.append(child)
#
#     return min_value

# def tree_min_value(root: Union[Node, None]) -> float:
#     """Takes the root Node of a binary tree and returns the minimum value of any of the Nodes in the binary tree. If
#     root is None, returns float('inf'). Uses an iterative depth-first traversal.
#
#     Time complexity: O(n)
#     Auxiliary space complexity: O(n)
#     """
#     min_value = float('inf')
#
#     stack = [root]
#     while len(stack) > 0:
#
#         current = stack.pop()
#         if current:
#
#             min_value = min(min_value, current.val)
#
#             for child in current.left, current.right:
#                 stack.append(child)
#
#     return min_value

def tree_min_value(root: Union[Node, None]) -> float:
    """Takes the root Node of a binary tree and returns the minimum value of any of the Nodes in the binary tree. If
    root is None, returns float('inf'). Uses a recursive depth-first traversal.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    if not root: return float('inf')
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))

def max_path_sum(root: Union[Node, None]) -> float:
    """Takes the root Node of a binary tree and returns the smallest sum of values accrued on the way from the root to
    any leaf Node. Uses a recursive depth-first traversal. If root Node is None, returns -float('inf').

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    if not root: return -float('inf')

    path_sum = root.val

    # If not, the root is a leaf, so you wouldn't want to add the maximum of its children (None) because you'd be
    # adding -infinity. For a Node, you find the maximum of its children. If these are real Nodes, this makes sense.
    # However, if one child is None, you want to make this code consistent by essentially giving None a value of -inf
    # and thus allowing the code to simply return the value of the child that is actually a Node. Therefore, -inf is
    # only here to make code consistently work for when both of a Node's children are Nodes and for when one child is
    # None but the other is a node.
    if root.left or root.right:
        path_sum += max(max_path_sum(root.left), max_path_sum(root.right))

    return path_sum


if __name__ == '__main__':

    # a = Node('a')
    # b = Node('b')
    # c = Node('c')
    # d = Node('d')
    # e = Node('e')
    # f = Node('f')
    #
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.right = f

    # print(depth_first_values(a))
    # print(depth_first_values(None))
    # print(breadth_first_values(a))
    # print(tree_includes(a, 'f'))

    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    # print(tree_sum(a))
    # print(tree_sum(None))
    # print(tree_min_value(a))
    # print(tree_min_value(None))

# In terms of trees, recursive solutions are usually best for finding and building paths, according to the video.

    # print(max_path_sum(a))
    # print(max_path_sum(None))