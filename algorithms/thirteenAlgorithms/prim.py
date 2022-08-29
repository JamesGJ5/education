# Prim's algorithm is different from Dijkstra's algorithm in that:
# -> Dijkstra's finds the shortest path between two nodes, but Prim's creates an MST (Minimum Spanning Tree)
#   -> My reason: Say you're building a telecoms network, using lots of wires. Ideally, you would want each node to communicate
#   as quickly as possible with each other node, by the shortest possible path in each pairing. However, this would
#   take a huge amount of wiring. Instead, we aim for a compromise using a minimum spanning tree, which takes much
#   less wiring but still ensures that all nodes are interconnected and information can travel from one node to another
#   relatively quickly.
#   -> Better reason: see https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/
#   -> On the other hand, you might want to find the shortest path when travelling using a map, which is why Google uses
#   Dijkstra's in Google Maps: they don't need an exorbitant amount of resource to perform this task.
# -> Prim's algorithm works only on undirected graphs because it assumes each node is accessible from each other node.

# 1. In Prim's algorithm, you start from ANY node (remember, not looking to find the shortest path from one node to every
# other node, so not considering a particular "start" node--just making an MST) and add this node to a "visited" list.
# 2. You now look at all edges leading away and pick the shortest edge, then add the node you get to to a visited list.
# 3. Now, consider both nodes in the visited list and repeat Step 2, choosing any smallest edge if there are multiple,
# just don't pick an edge leading to a node that has already been visited and don't pick an edge that leads to the
# edges forming of any cycles; in fact, if you don't pick any edges leading to nodes already visited, you won't have
# cycles.
# IMPORTANT: you can consider a "visited" edges neighbours multiple times, you just can't consider an edge that travels
# to a "visited" node.

# First, I am going to code this naively. My way is going to take a list of lists (edges) in each of which the triplet
# of elements are the two labels for the nodes the edge connects, followed by the weight of this edge. These edges are
# undirected.

# My function is going to use a helper function called build_graph, which builds an adjacency map from these edges,
# i.e. a mapping of a node (the key) to nodes that edges stemming from it lead to alongside the weights of said edges
# (found as a 2-tuple in a list, i.e. neighbour, weight).

# I need a way to record which edges are visited, so I think the best thing to do will be to create a set called
# "visited".

# Going to start with the first node indexed in adjacency_map.keys(). When I have this, going to add it to "visited",
# then iterate through the tuples in its values and find the tuple containing a neighbour that isn't in "visited" and
# that has the smallest weight, or joint-smallest weight. To do this, would probably be best to iterate through these
# tuples with a for loop, incrementing the neighbour node if the new neighbour is not in visited and has a smaller
# value. I guess I could initialise chosen_neighbour as None and the weight as float('inf'). At the end of this
# iteration, if chosen_neighbour isn't None, want to record the edge, so add a tuple containing key, neighbour, weight
# to a list of edges. Call the chosen_neighbour X.

# Next, want to move onto the smallest edge present that is coming away from X or the first node.

# Actually, I have thought of a way to do this. First, take the list of edges and double its size by, for each edge
# X, Y, w, creating a list Y, X, w. Now, the order in the list will correspond to the direction of the edge. Start with
# the list at index 0 (might as well since it is arbitrary), take the 0th element of it as the node in consideration
# and add X to visited.

# Add list[0][0] to "visited". Now, initialise the index of the edge to be considered as -1 and smallest_weight as float('inf'),
# then iterate through the list of edges, updating the
# index whenever you find an edge whose first element IS in visited and whose second element is NOT in "visited" and whose
# weight is smaller than any valid weights so far, but remove an edge from the list whenever you find that
# its second element has indeed been visited.
# When this is done, pop the edge at the chosen index from the list and append it to a new list, called "MST".
# Repeat the iteration; if ever, at the end of an iteration, the index is still -1, this must mean that the list is
# empty or all nodes have been visited.

# THE BELOW WORKS BUT IT IS INEFFICIENT

# def _reflect_edges(edges):
#     """Takes the list of undirected edges and replaces it with a list of directed edges (e.g. an undirected edge gets
#     turned into two directed edges within this undirected edge).
#
#     Time complexity: O(n), where n is the number of undirected edges
#     Auxiliary space complexity: O(n)
#     """
#
#     for edge in edges[:]:
#
#         reflection = [edge[1], edge[0], edge[2]]
#         edges.append(reflection)
#
#     print("done")
#     return edges
#
#
# def my_prim(edges):
#     """Takes edges, a list of lists in which each inner list consists of: node beginning edge, node edge leads to, and
#     weight of edge. A helper function _reflect_edges(edges) makes sure that the list contains both directions for a
#     given edge. For example, if there is [X, Y, 5], it makes sure there is also [Y, X, 5]. This algorithm returns
#     a list of undirected edges contained in the MST.
#
#     Time complexity: O(n**2), where n is the number of undirected edges. This is because the for loop is O(n), and if
#         the nodes are linearly connected, only one edge will become forbidden (added to skip_edges) in each entirety of
#         the for loop, meaning the while loop will run a number of times equal to the number of edges.
#     Auxiliary space complexity: O(n)
#     """
#
#     edges = _reflect_edges(edges)
#     print(edges)
#
#     visited_nodes = {edges[0][0]}
#
#     # Indices of edges to be skipped in iterations
#     skip_edges = set()
#
#     mst = []
#
#     while len(skip_edges) < len(edges):
#
#         i = -1
#         smallest_weight = float('inf')
#
#         for j, element in enumerate(edges[:]):
#
#             if j in skip_edges:
#                 # print(j)
#                 continue
#
#             start_node = element[0]
#             end_node = element[1]
#             weight = element[2]
#
#             if end_node in visited_nodes:
#                 skip_edges.add(j)
#                 continue
#
#             if start_node in visited_nodes:
#                 if weight < smallest_weight:
#                     i = j
#                     smallest_weight = weight
#
#         # If i == -1 and you continue with the below, it'll give you the last edge in the list, whether it fits the mst
#         # or not.
#         if i != -1:
#
#             chosen_edge = edges[i]
#             print(chosen_edge)
#
#             mst.append(chosen_edge)
#             skip_edges.add(i)
#             visited_nodes.add(chosen_edge[1])
#
#         # print(len(visited_nodes))
#
#     return mst


def naive_prim(adjacency_matrix):
    """Takes an adjacency matrix and prints out the edges in the minimum spanning tree within it, along with the weight
    of each.
    https://favtutor.com/blogs/prims-algorithm-python#:~:text=What%20is%20Prim's%20Algorithm%3F,form%20the%20minimum%20spanning%20tree.

    Time complexity: O(v**2) because for each node, we are using the adjacency matrix to consider its relationship with
        each other node, and even itself; this is reflected in the two O(v) loops in the code below
    Auxiliary space complexity: O(v), where v is the number of vertices
    """

    assert len(adjacency_matrix) == len(adjacency_matrix[0])

    # Number of vertices (nodes)
    v = len(adjacency_matrix)

    # Each index in selected is for a different node. When it has been "visited", the element at said index will become
    # 1. In any pass of the below outer for loop, we want all element that have been visited to have edges stemming
    # from them considered, because edges stemming FROM a visited node are valid, it's just that edges being considered
    # in the direction of a visited node is not
    selected = [0] * v  # O(v)

    # The below is the number of edges that have been found for the MST. Of course, before we start looking, this is
    # zero
    no_edge = 0

    selected[0] = True

    # The below is to accompany the later print statements
    print("Edge : Weight\n")

    # In the MST, the number of edges will always be less than or equal to the number of nodes - 1. This may make it
    # seem like the the below while loop should say no_edge <= V - 1 (or < V). However, we have chosen to start with
    # no_edge = 0, so the number of edges that will be in the MST after any pass will be no_edge (going into the MST)
    # + 1. If the final MST should contain, at most, V - 1 edges, the no_edge going into it should be (at most) V - 2.
    # So, the loop will run V - 1 times, in which V - 1 edges will be added to the MST and at the end of which no_edge
    # will be V - 1, so the while loop won't run anymore.
    while no_edge < v - 1:

        minimum = float('inf')

        # 'a' and 'b' are the nodes at each end of the edge returned by this iteration of the while loop.
        a = 0
        b = 0

        # There are at most v nodes for which edges stemming from them can be considered
        for i in range(v):

            # Only want to consider edges stemming from nodes that have already been visited, hence the below 'if'
            # statement
            if selected[i]:

                # Now we are considering the node on the other end of the edge
                for j in range(v):

                    # First part of the if statement is necessary because we don't want to consider any edge leading
                    # from the node labelled by 'i' to itself or to any node that has already been visited;
                    # Second part of if statement exists because, if not adjacency_matrix[i][j], then we are
                    # considering a j that actually isn't led to from i by an existing edge--really, we are considering
                    # an non-existent edge, for which adjacency_map[i][j] (i != j because we've passed the first part
                    # of the if statement) gives 0, which evaluates to False.
                    if not selected[j] and adjacency_matrix[i][j]:

                        if adjacency_matrix[i][j] < minimum:

                            minimum = adjacency_matrix[i][j]

                            a = i
                            b = j

        print(str(a) + "-" + str(b) + ":" + str(adjacency_matrix[a][b]))
        selected[b] = True
        no_edge += 1


from collections import defaultdict
import heapq

def create_spanning_tree(graph, starting_vertex):
    """Takes a graph (represented by an adjacency map, not matrix) and returns the MST (minimum spanning tree) present
    in the graph.

    Time complexity: O(Elog(V)) because:
        PART 1 + PART 2 + PART 3 (see below for these parts) = O(V) + O(Vlog(V)) +
        O(Elog(V)) = O(V) + O((V+E)log(V))... now, E >> V (for fully-connected), so V + E >> V. Moreover, log(V) is
        likely to be at least 1, so O((V+E)log(V)) >> O(V) is very probable, so discount O(V)... = O((V+E)log(V)).
        Remember, E >> V, so this approximates to O(Elog(V))
    Auxiliary space complexity: O(E), as:
        There can be at most < E elements in the heap at any time (the heap carries
        edges)
    """
    mst = defaultdict(set)

    visited = set([starting_vertex])

    edges = [
        # Cost is weight, to is the node the edge leads to
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]

    # PART 1
    # Min heap priority queue. Initially, the only edges in this heap are those that stem from starting_vertex
    # This takes O(n), where n is the number of edges being heapified--see lined paper and
    # C:\Users\james\PycharmProjects\heaps\youTube2.py. Assume worst case, where each vertex is connected to every
    # other vertex. So, because the below heapification occurs for only one vertex, which must then have V edges coming
    # out of it, the time complexity is O(V).
    # RESULT OF PART 1: O(V)
    heapq.heapify(edges)

    # i.e. while there are edges in the heap queue (an empty heap evaluates to False)
    # The while loop executes at most V - 1 (~V) times, because we will have at most V - 1 edges in the MST and each
    # execution of the while loop should yield one of those edges if there is a path from each vertex to each other
    # vertex, because there should be a 'to' that hasn't yet been visited.
    while edges:

        # The below picks the edge with the minimum cost from the heap.

        # PART 2
        # Assume the worst case scenario: each node is connected to every other node. So, each node has V edges coming
        # out of it. Therefore, the first time round, the time complexity of the below pop is O(log(aV)) (because of
        # sift-down--see C:\Users\james\PycharmProjects\heaps\youTube2.py), where a is
        # some constant. The second time round, due to the next node, approximately V edges will be added, so we now
        # have O(log(2aV))... if we assume V edges is added overall for each node (which is not the case because some
        # edges will lead to_next nodes which have been visited), then eventually, we get O(log(V*aV)) = O(log(V**2)
        # (forget the constant) = O(2log(V)); if the average time complexity is somewhere between O(log(V)) and
        # O(2log(V)), it varies only by a small factor, so say the AVERAGE TIME COMPLEXITY is O(log(V)). While loop
        # executes V times overall, so overall, time complexity due to bottom is O(Vlog(V)).
        # RESULT OF PART 2: O(Vlog(V))
        cost, frm, to = heapq.heappop(edges)

        # In the worst case, we have a heap where
        if to not in visited:
            # If to is not in visited, the edge is valid; so, because this edge has the minimum cost of valid edges, it
            # will be added to the mst, 'to' to visited first
            visited.add(to)

            # This adds the edge to the mst, as a value of the key frm
            mst[frm].add(to)

            # Here we are adding new valid edges to the heap; remember, the other edges from starting_vertex are still
            # in there since they are still worth considering

            # Each node can be connected to each other node, so the for loop can run through v iterations, meaning the
            # outer for loop has a time complexity of O(v)

            # PART 3
            # The for loop runs 2E times TOTAL. This is because we have an adjacency map, mapping each node (as a key)
            # to neighbours; but there are also mappings of the neighbours to the initial node, since the graph is undi-
            # rected. We iterate through all of these, but there's only actually one edge for each pair of mappings, so
            # there are 2 * number of edges mappings in total (2E).
            # The contents of the for loop are O(log(V)), so the entirety of the for loop is Elog(V). Because 2E is the
            # TOTAL (across all executions of the while loop), we don't need to multiply this by V like we did earlier
            # with the pop complexity.
            # RESULT OF PART 3: O(Elog(V))
            for to_next, cost in graph[to].items():

                if to_next not in visited:

                    # Time complexity for this will be, on average, O(log(V)), for similar reasons as mentioned
                    # above the line reading "cost, frm, to = heapq.heappop(edges)"
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

# There is also an implementation of Prim's algorithm using what is called the Fibonacci heap, which allows the
# algorithm to utilise a time complexity of O(E + Vlog(V)). Depending on E and V, this may be better than the binary
# heap implementation above under certain scenarios.

if __name__ == '__main__':

    # edges = [
    #     ['a', 'b', 4],
    #     ['a', 'h', 8],
    #     ['b', 'c', 8],
    #     ['b', 'h', 11],
    #     ['i', 'h', 7],
    #     ['g', 'h', 1],
    #     ['c', 'i', 2],
    #     ['c', 'f', 4],
    #     ['i', 'g', 6],
    #     ['g', 'f', 2],
    #     ['c', 'd', 7],
    #     ['d', 'f', 14],
    #     ['d', 'e', 9],
    #     ['e', 'f', 10]
    # ]

    # print(_reflect_edges(edges))
    # print(my_prim(edges))

    # How the below works is, imagine that the column with index i and the row with index i both represent the same
    # node. Therefore, in the diagonal of the graph, all elements are zero, because any node is at a distance of 0 from
    # itself. However, the 0's in other positions actually represent that the row's node and the column's node aren't
    # linked by an edge. We want to avoid non-existent edges and edges between a node in itself in our code (by
    # avoiding 0), so these positions are marked with 0 in adjacency matrix.
    # adjacency_matrix = [
    #     [0, 9, 75, 0, 0],
    #     [9, 0, 95, 19, 42],
    #     [75, 95, 0, 51, 66],
    #     [0, 19, 51, 0, 31],
    #     [0, 42, 66, 31, 0]
    # ]
    #
    # naive_prim(adjacency_matrix)




    pass