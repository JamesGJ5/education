from collections import defaultdict
import sys

# GRAPHS are NODES (sometimes referred to as vertices) CONNECTED BY EDGES.

# Nodes can be things, edges can represent relationships between these things.

# A directed graph may have arrowheads along edges, an undirected graph may not.

# In a tree, nodes you can travel to via one step from a given start node are the neighbours of the start node. If the
# edges unto these neighbours are directional and point only to these neighbours, you can't so back so the start node
# isn't a neighbour of the neighbours.

# An adjacency list is a good way to represent graphs. An adjacency list is generally a dictionary (in Python), for
# constant time.
#   Each node is a key in the dictionary
#   Each key's values are its node's  neighbours

# See 9:37 for difference between depth-first and breadth-first traversal.

# A depth-first traversal uses a stack, while a breadth-first traversal uses a queue (see 11:40)

# graph = {
#     'a': ['b', 'c'],
#     'b': ['d'],
#     'c': ['e'],
#     'd': ['f'],
#     'e': [],
#     'f': []
# }
# print(graph)

def depth_first_print1(graph, source):
    """Starting from the source node, undertakes a depth-first traversal on the given graph, printing values at each
    node it encounters. Uses an explicit stack (so no recursion). Directed graph 
    with no cycles.

    Time complexity: O(n**2)
    - Should be on this sort of order because there are up to n**2 edges and you 
    will have to traverse all of them. However, edges can be repeated, so might 
    not simply be n**2 steps, could be more, but this order is a good estimate of 
    a worst-case.
    Auxiliary space complexity: O(n)
    """
    # Must use an explicit stack, defined in https://www.youtube.com/watch?v=P2m9qxMiakA as being an ADT (Abstract Data
    # Type) stack that may be implemented by the programmer (me). In Python, can simply use a list and append/pop.
    # Remember: linked list is probably still a better option re: time, but list is fine for the purpose of learning
    # about graphs.
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        # With extend, items in the passed array are appended to the array being extended one-by-one, so the time
        # complexity is O(k), where k is the number of items in the passed array.
        stack.extend(graph[current])

def depth_first_print2(graph, source):
    """Starting from the source node, undertakes a depth-first traversal on the given graph, printing values at each
    node it encounters. Uses an implicit stack (via recursion). Directed graph 
    with no cycles.

    Time complexity: O(n**2)
    - Should be on this sort of order because there are up to n**2 edges and you 
    will have to traverse all of them. However, edges can be repeated, so might 
    not simply be n**2 steps, could be more, but this order is a good estimate of 
    a worst-case.
    Auxiliary space complexity: O(n)
    """
    print(source)
    # Don't actually need to do the below conditional, because when the source key has no value, the for loop will not
    # do any iteration, so there will be no consecutive recursive call.
    # if len(graph[source]) == 0:
    #     return
    for neighbour in graph[source]:
        depth_first_print2(graph, neighbour)

def breadth_first_print(graph, source):
    # According to the YouTube video, breadth-first traversal is really only possible using iteration, since recursion
    # would counteract the queue you'd have to use.
    """Starting from the source node, undertakes a depth-first traversal on the given graph, printing values at each
    node it encounters. Uses iteration and queue. Very similar to the code above for the iterative version of the
    depth_first_print function (depth_first_print1). Directed graph 
    with no cycles.

    Time complexity: O(n**2)
    - Should be on this sort of order because there are up to n**2 edges and you 
    will have to traverse all of them. However, edges can be repeated, so might 
    not simply be n**2 steps, could be more, but this order is a good estimate of 
    a worst-case.
    Total space complexity: O(n)
    """
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        queue.extend(graph[current])

def has_path1(graph, src, dst):
    """Takes a graph and returns True if it contains a valid path from Node src to Node dst, but False otherwise. Uses
    an iterative depth-first traversal. Might not work with a cyclic graph. 
    Directed graph here.

    Time complexity: O(n**2)
    - Should be on this sort of order because there are up to n**2 edges and you 
    will have to traverse all of them. However, edges can be repeated, so might 
    not simply be n**2 steps, could be more, but this order is a good estimate of 
    a worst-case.
    Auxiliary space complexity: O(n)
    """
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        if current == dst:
            return True
        stack.extend(graph[current])
    return False

def has_path2(graph, src, dst):
    """Takes a graph and returns True if it contains a valid path from Node src to Node dst, but False otherwise. Uses
    a breadth-first traversal. Might not work with a cyclic graph. Directed graph 
    here.

    Time complexity: O(n**2)
    - Should be on this sort of order because there are up to n**2 edges and you 
    will have to traverse all of them. However, edges can be repeated, so might 
    not simply be n**2 steps, could be more, but this order is a good estimate of 
    a worst-case.
    Auxiliary space complexity: O(n)
    """
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst:
            return True
        queue.extend(graph[current])
    return False

def has_path3(graph, src, dst):
    """Takes a graph and returns True if it contains a valid path from Node src to Node dst, but False otherwise. Uses
    a recursive depth-first traversal. Might not work with a cyclic graph. Directed 
    graph here.

    Time complexity: O(n**2)
    - Should be on this sort of order because there are up to n**2 edges and you 
    will have to traverse all of them. However, edges can be repeated, so might 
    not simply be n**2 steps, could be more, but this order is a good estimate of 
    a worst-case.
    Auxiliary space complexity: O(n)
    """
    if src == dst:
        return True
    for neighbour in graph[src]:
        if has_path3(graph, neighbour, dst):
            return True
    return False

def has_path_directed_or_undirected(graph, src, dst):
    """Takes a graph and returns True if it contains a valid path from Node src to Node dst, but False otherwise. Uses
    a recursive depth-first traversal. Works with a fully-directed graph (with or without cycles) and an undirected
    graph.

    Time complexity: O(n**2)
    - There are up to n**2 edges, and edges won't be repeated much because nodes 
    won't be revisited much, due to the removals below.
    Auxiliary space complexity: O(n)
    """
    if src == dst:
        return True

    # Note: the below was because I was initially making neighbours into sets for the cases of fully-undirected graphs,
    # but have since stopped.
    # If the neighbours of src are being recorded in a set, you want to convert it to a list, because the removal in
    # the below for loop means the for loop can't be used upon a set, but it can be used upon a list.
    # if isinstance(graph[src], set):
    #     graph[src] = list(graph[src])

    for neighbour in graph[src][::-1]:
        print(neighbour)
        # Only removing if it is the neighbour; if it is not, then that is because the recursion has eventually
        # returned to the exact same place and is trying to remove the same thing as has been removed.
        if neighbour in graph[src][-1:]:
            # Note: if graph[src] is a list and you use the below removal line, things will not work because, when
            # implementing a for loop on a list that shortens by 1 each time, not all elements initially in the list will
            # be visited, since it is the index visited the for loop increments each time, and if elements are leaving
            # their indices, they are not necessarily visited: it will be every other element visited, starting with the
            # first in the list. This is the reason why, above, I use the reverse of the list in the for loop.
            graph[src].remove(neighbour)

        if has_path_directed_or_undirected(graph, neighbour, dst):
            return True
    return False

def undirected_has_path(edges, src, dst):
    """Takes a list of edges, builds this into the adjacency list for an undirected graph, and returns True if the
    graph contains a path from src to dst, but False otherwise.

    Time complexity: O(n**2)
    - There are up to n**2 edges, so building the adjacency map is an n**2 operation 
    in time. Sum that with the n**2 time complexity of has_path_directed_or_undirected 
    and you get an O(n**2) time complexity overall.
    Auxiliary space complexity: O(n)
    """
    graph = defaultdict(list)
    for edge in edges:
        for i in range(2):
            t = graph[edge[i]]
            t.append(edge[1 - i])
    print(graph)
    return has_path_directed_or_undirected(graph, src, dst)

def undirected_path_youtube(edges, src, dst):
    """Takes a list of edges, builds this into the adjacency list for an undirected graph, and returns True if the
    graph contains a path from src to dst, but False otherwise. Uses recursive depth-first search.

    Time complexity: O(n**2)
    Auxiliary space complexity: O(n)
    """
    graph = build_graph(edges)
    return has_path_youtube(graph, src, dst, set())

def build_graph(edges):
    """Builds an adjacency list graph from a list of edges (lists containing 2 nodes)."""
    graph = {}

    for edge in edges:
        end1, end2 = edge
        if not end1 in graph: graph[end1] = []
        if not end2 in graph: graph[end2] = []
        graph[end1].append(end2)
        graph[end2].append(end1)

    return graph

def has_path_youtube(graph, src, dst, visited):
    """Takes an adjacency list for an undirected (or fully-directed) graph, and returns True if the
    graph contains a path from src to dst, but False otherwise. Uses recursive depth-first search.

    Time complexity: O(n**2)
    Auxiliary space complexity: O(n)
    """
    if src in visited:
        return False

    visited.add(src)

    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path_youtube(graph, neighbour, dst, visited):
            return True

    return False

def connected_components_count(graph):
    """Counts the number of collections of connected components.

    Time complexity: O(n**2)
    Auxiliary space complexity: O(n)
    """
    visited = set()
    count = 0
    for node in graph:
        count += explore(graph, node, visited)
    return count

def explore(graph, current, visited):
    """Explores all nodes of a graph, augmenting the passed set of visited nodes as it goes.

    Time complexity: O(n**2)
    Auxiliary space complexity: O(n)
    """
    if str(current) in visited:
        return False

    visited.add(str(current))

    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    # print(True)
    return True

def largest_component(graph):
    """Takes a graph and returns the number of nodes in the largest component. A component is a collection of connected
    nodes in the graph.

    Time complexity: O(n**2)
    Auxiliary space complexity: O(n)
    """
    visited = set()
    largest_component_size = 0

    for node in graph:
        largest_component_size = max(largest_component_size, component_size(graph, node, visited))

    return largest_component_size

def component_size(graph, node, visited):
    """Counts the number of nodes in the component in which the passed node is located.

    Time complexity: O(n**2)
    Auxiliary space complexity: O(n)
    """
    if str(node) in visited:
        return 0

    visited.add(str(node))
    size = 1

    for neighbour in graph[node]:
        size += component_size(graph, neighbour, visited)

    return size

def shortest_path(edges, src, dst):
    """Takes a list of edges (each of which is a list containing the two nodes the edge connects) and builds the edges
    into an adjacency map representing a graph; in the map, each node of the graph is mapped to a list of neighbours.
    After building this adjacency map, the length of the shortest path from node src to node dst is found using a
    breadth-first traversal. If there is no path from src to dst, -1 is returned.

    Old question: according to the YouTube video, the time complexity of this algorithm is O(n). So, if the map doubles in
      number of nodes, the time taken to find the shortest path doubles. However, what assumptions are made about the
      positions of the src and dst node? Surely, if the map is just a huge grid and we double the number of nodes but
      keep the positions of src and dst constant, then the time complexity is actually O(1)? Same question for space
      complexity.
    Answer: because we are thinking about worst-case time complexity to err on the side of caution
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    graph = build_graph(edges)
    visited = set()

    queue = [[src, 0]]

    while len(queue) > 0:
        current_node, current_distance_from_src = queue.pop(0)

        if current_node == dst:
            return current_distance_from_src

        elif current_node in visited: continue

        visited.add(current_node)

        for neighbour in graph[current_node]:
            queue.append([neighbour, current_distance_from_src + 1])

    return -1

def count_islands(grid):
    """Takes a grid (a linear array of equally-sized linear arrays) in which each tile is either 'w' (water) or 'l'
    (land). The number of islands (of land) in the grid is counted and returned.

    Time complexity: O(n), where n is number of tiles (so number of rows x number of columns)
    Auxiliary space complexity: O(n), since each encountered tile must be put into a set such that it is not
        encountered again
    """
    visited = set()
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):

            count += explore_island(grid, r, c, visited)

    return count

def explore_island(grid, r, c, visited):
    """Explores the grid island that the tile at (r, c) may be a part of, marking the island's tiles and returning True
    if it is on an unexplored island but simply returning False otherwise.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    row_inbounds = 0 <= r < len(grid)
    column_inbounds = 0 <= c < len(grid[0])
    if not row_inbounds or not column_inbounds:
        return False

    tile_type = grid[r][c]
    if tile_type == 'w':
        return False

    # Note: the below is a bit clunky, especially in case you miss a couple of brackets, so it might be a better idea
    #   to make visited a dictionary with keys equal to r and each r with its corresponding c, for the coordinate
    #   visited. Could also map the c to a value of True
    if str((r, c)) in visited:
        return False
    visited.add(str((r, c)))

    for r, c in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        explore_island(grid, r, c, visited)

    return True

def minimum_islands(grid):
    """Takes a grid (a linear array of equally-sized linear arrays) in which each tile is either 'w' (water) or 'l'
    (land). The number of grid tiles in the smallest island is returned.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    visited = set()
    smallest_size = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):

            island_size = measure_island(grid, r, c, visited)
            # Note: be careful because the order in the below conditional statement matters. If 0 < island_size <
            # smallest_size is not satisfied, it is because island_size is 0 or island_size is greater than or equal to
            # the current smallest_size. In this case, if smallest_size is 0, either are fine options to assign
            # smallest_size to. However, if smallest_size is not 0, then you wouldn't want to revert it back to 0 and
            # you wouldn't want to assign it a higher or equal to smallest size.
            if 0 < island_size < smallest_size or smallest_size == 0:
                smallest_size = island_size

    return smallest_size

def measure_island(grid, r, c, visited):
    """Takes grid points r (row index) and c (column index) and, if the tile is in and returns the number of tiles in
    the land island it is found in, and returns the count. If the island has already been discovered, returns 0.

    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    """
    count = 0

    if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
        return count

    if not grid[r][c] == 'l':
        return count

    # Note: the below is a bit clunky, especially in case you miss a couple of brackets, so it might be a better idea
    #   to make visited a dictionary with keys equal to r and each r with its corresponding c, for the coordinate
    #   visited
    if str((r, c)) in visited:
        return count

    visited.add(str((r, c)))

    count += 1

    count += measure_island(grid, r - 1, c, visited)
    count += measure_island(grid, r + 1, c, visited)
    count += measure_island(grid, r, c - 1, visited)
    count += measure_island(grid, r, c + 1, visited)


    return count

if __name__ == '__main__':
    # Fully-directed graph
    # graph = dict(a=['b', 'c'], b=['d'], c=['e'], d=['f'], e=[], f=[])
    # print(graph)
    # depth_first_print1(graph, 'a')
    # depth_first_print2(graph, 'a')
    # breadth_first_print(graph, 'a')

    # A cycle is any path in a graph from one node back to itself.

    # In the case of 33:38 of the youTube video, time complexity is O(e), where e is the number of edges, and total space
    # complexity is O(n), where n is the number of nodes. This is the case for iterative and recursive depth-first search,
    # and (iterative) breadth-first search.

    # Could also express the above complexity in a single variable. For example, could just express e in terms of n, since
    # at worst, n**2 is the number of edges (e.g. if each node connects to every single other node). So, time complexity
    # could be expressed as O(n**2). Really, worst case would be n(n-1), but as n gets big, this tends to n**2.

    # Fully-directed graph
    # graph = dict(f=['g', 'i'], g=['h'], i=['g', 'k'], h=[], k=[], j=['i'])
    # print(has_path1(graph, 'i', 'f'))    # False
    # print(has_path1(graph, 'f', 'i'))    # True
    # print(has_path2(graph, 'i', 'f'))    # False
    # print(has_path2(graph, 'f', 'i'))    # True
    # print(has_path3(graph, 'i', 'f'))    # False
    # print(has_path3(graph, 'f', 'i'))    # True


    # Undirected graph's edges
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]

    # Undirected graph
    graph = defaultdict(list)
    for edge in edges:
        for i in range(2):
            t = graph[edge[i]]
            t.append(edge[1-i])
    print(graph)
    # print(has_path_directed_or_undirected(graph, 'i', 'm'))    # True
    #
    # graph = defaultdict(list)
    # for edge in edges:
    #     for i in range(2):
    #         t = graph[edge[i]]
    #         t.append(edge[1-i])
    # print(graph)
    # print(has_path_directed_or_undirected(graph, 'i', 'o'))    # False

    # print(undirected_has_path(edges, 'i', 'm'))    # True
    # print(undirected_has_path(edges, 'i', 'o'))    # False

    # build_graph(edges)

    # print(undirected_path_youtube(edges, 'i', 'm'))    # True
    # print(undirected_path_youtube(edges, 'i', 'o'))    # False

    # connected_components = {
    #     0: [8, 1, 5],
    #     1: [0],
    #     5: [0, 8],
    #     8: [0, 5],
    #     2: [3, 4],
    #     3: [2, 4],
    #     4: [3, 2]
    # }
    #
    # print(largest_component(connected_components))

    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v'],
    ]

    # print(shortest_path(edges, 'w', 'z'))


    const_grid = [[], [], [], [], [], []]

    for i, char in enumerate([*'wlwwwwlwwwwwwlwwwllwlwwllllwww']):
        const_grid[i // 5].append(char)

    # print(const_grid)
    # print(count_islands(const_grid))
    print(minimum_islands(const_grid))