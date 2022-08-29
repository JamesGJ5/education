import heapq

# Below is just a shortest path algorithm and a helper function used within it that I made with little help,
# for practice. Will probably replace with the most efficient version of Dijkstra's that I can find on the internet. 
# Note: my function doesn't follow Dijsktra's.

def _build_graph_and_dict(edges):
    """Takes a list of weighted edges, as described in the function shortest_path's definition, and returns an adjacency map
    along with a dictionary containing all of the nodes mapped to float('inf'), for use in shortest_path.

    Time complexity: O(n), where n is number of edges
    Auxiliary space complexity: O(n), because:

    Number of keys in shortest_path_map and adjacency_map is each the number of nodes. In the best case scenario, all edges
    are undirected, so there won't be opposing edges, and all nodes will be connected to every other node, meaning
    that for a given number of edges, there'll be as few nodes as possible. However, in the worst case, every node is
    connected to only one other node and edges are directed, meaning that for a given number of edges n, the number of
    nodes is as high as possible: n. Therefore, there are n keys in each shortest_path_map (with 1 value per key) and
    adjacency_map. Now, for the adjacency_map, the number of tuples (each of which contains a node adjacent to the
    key and the weight of the edge from the key to this adjacent node) in the values is simply equal to the number of
    edges, so is also n. I don't know how much space each key (a single string character in the examples in "__main__")
    takes up compared to each tuple, but say the space taken up by each is m1 and m2. Therefore, space taken up in
    adjacency_map altogether is (m1+m2)n. Therefore, O(n) auxiliary space for the adjacency_map. O(n) for shortest_path_map,
    so O(n) for the outputs altogether.
    """

    shortest_path_map = {}
    adjacency_map = {}

    for edge in edges:

        start_node = edge[0]
        end_node = edge[1]
        weight = edge[2]

        # Adding each node to shortest_path_map with value float('inf') if it isn't already in there, and make its
        # predecessor in the shortest path to it None. Must be in list form because will be augmented during the
        # traversal in the function shortest_path.
        for node in start_node, end_node:
            if not node in shortest_path_map:
                shortest_path_map[node] = [float('inf'), None]

            # Must do this for end_node too, because even if it doesn't have any edges leading away from it, it must be
            # included in the adjacency map for shortest_path to work without having to write a bunch of extra code there
            if not node in adjacency_map:
                adjacency_map[node] = []

        adjacency_map[start_node].append((end_node, weight))

    return shortest_path_map, adjacency_map


def shortest_path(edges, src):
    """Takes a list of edges (where each edge is represented by a list containing a first node, a second node to which
    the edge travels from the first node, and the edge of the weight), builds it into an adjacency map, and uses that
    adjacency map to return a dictionary mapping, for a given source node, the shortest distances from that node to
    each destination node, and, for each destination node, the node that would be visited penultimately on the shortest
    path from src to that node; if a node is inaccessible, its distance is returned as float('inf') and the previous
    node on the path is returned as None. Moreover, if the destination is the source, its distance is 0 and its
    previous node is just the source. Note: each edge is unidirectional, but two opposing edges form an undirected
    edge. Assumes a directed graph without cycles, although if it must have cycles, can just make something comparable
    to a visited set; see comments above the for loop in the function body.

    Time complexity: O(n (from _build_graph_and_dict) + n (the total number of iterations of the below for loop will
        just be the number of edges because the number of adjacencies is the same as the number of edges)) = O(n)
    Auxiliary space complexity: O(n (from shortest_path_map and adjacency_map) + n) = O(n)
    """

    # First we have to build the adjacency map from the edges. A key will be a node, and its corresponding value will
    # be a list of tuples, each of which houses an adjacent node that can be travelled to, followed by the weight of
    # the edge that must be taken to get there.

    shortest_path_map, adjacency_map = _build_graph_and_dict(edges)

    # I was first thinking that one good way to do this would be to make a function that finds the shortest weighted
    # path from src to dst (destination), then calls that multiple times, passing all nodes in the map as dst.
    # HOWEVER, this might be inefficient, because this might take (number of nodes) entire traversals altogether,
    # whereas if we just did one traversal we could log the shortest path for each node all in the same traversal.

    # So in the above idea, we want to traverse so that all possible paths are covered. Therefore, it doesn't seem to
    # matter whether we use a breadth-first traversal or depth-first traversal in terms of applicability. However, must
    # still consider the complexity associated with each. I think both will take the same time complexity to traverse
    # all possible paths, since the number of possible paths is the same for each algorithm. Moreover, I suppose
    # space complexity will be the same for each, since we'd be considering the number of nodes visited in total in a
    # path, and since the paths are the same in each case, this number would be the same for a given path in each case.
    # In short, whatever the algorithm, time complexity is O(n**2), since the worst case is each node being linked to
    # every other node, and the auxiliary space complexity is O(n), for the stack/queue. These apply since, here, we
    # have a directed graph.

    # Using a breadth-first search. Format of a queue element is: node, shortest path from src, node before it on
    # shortest path from src.
    queue = [[src, 0, src]]

    while len(queue) > 0:

        current = queue.pop(0)

        current_node = current[0]
        distance = current[1]
        predecessor = current[2]

        if distance < shortest_path_map[current_node][0]:

            shortest_path_map[current_node] = [distance, predecessor]

        # If the graph was undirected, a depth first search might be better. In this case, for a given path, we'd add
        # each edge taken (and the direction it was taken in) to a set. Then, when at a node and looking at its neigh-
        # bours, we'd only add to the stack the neighbours which, to get to them from the node in question, would take
        # an edge and direction not present in the set. However, after the for loop was done, and we went to the node
        # behind the initial node so that the path could go elsewhere, we would remove said edge from the set, because
        # we might want to take the same edge in a different path--just don't want to take it multiple times in one
        # path. HOWEVER, there may be better solutions on the internet.

        # For the above for a breadth-first search, maybe just pass the set to each neighbour found in a particular
        # path, if possible.

        # Also, wouldn't have to add the edges to the sets mentioned above, just the nodes visited: in one path, no
        # point visiting the same node twice, although you may want to visit it multiple times in the traversal the
        # node is a part of, of course.

        for neighbour, weight in adjacency_map[current_node]:
            # print(neighbour, weight)

            queue.append([neighbour, weight + distance, current_node])

    # Function would return a dictionary mentioned in the function description. My first idea was to add a key to the
    # dictionary when that node was first met in the traversal. However, inaccessible nodes would not be met, so we'd
    # still have to iterate through the nodes and add them to the dictionary afterwards, even when seeing if a node is
    # in the dictionary or not. Therefore, it might be best to simply create the dictionary at the beginning. This
    # would be an O(n) task, where n is the number of edges provided, since you'd want to iterate through all the edges
    # to make sure you've included all the nodes in the dictionary. ACTUALLY, it would probably be best to do this
    # while building the adjacency map, since you're iterating through all the edges in this case too.

    return shortest_path_map


def naive_dijkstras(graph, src):
    """From https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/. Note: just returns the shortest
    distance from src to each other node, not the nodes in the shortest path. This code makes most sense after watching
    https://www.youtube.com/watch?v=pVfj6mxhdMw&t=575s.

    Note that in this video, we take the shortest edge from A first because, had we taken the second-shortest edge and
    gone from A to B, then we'd prioritise taking the longest edge each time, and thus start taking the shorter edges
    much later, meaning there'd have been a lot of wasted pathing. For example, when we go from A to D to B and then
    realise this is quicker than going from A to B, we don't continue and then go from A to B to C. However, if we
    started with A to B to C, it we wouldn't realise this path was inefficient.

    Time complexity: O(n**2), where n is the number of nodes; O(n**2) results from O(an) (from outer for loop) * O(bn
        (from inner for loop) + cn (from looking at the neighbours) = O(n**2)
    Auxiliary space complexity: O(n)
    """
    n = len(graph)

    # Initialise distance list as all infinities. Just the distances of each node from src.
    dist = [float('inf') for _ in range(n)]

    # Initialise distance of the src node from itself to 0
    dist[src] = 0

    # Initialise list of visited nodes
    visited = [False for _ in range(n)]

    # The reason for this outer for loop is because we want to repeat the body of the for loop for each node,
    # essentially. This is equivalent to starting from each node in the video in the function description and
    # considering its neigbours.
    for _ in range(n):
        # u will be the next node whose neighbours we consider. Ultimately, this will be the node with the shortest
        # cumulative path so far. We initialise this node as -1 (which, effectively, doesn't represent any node because
        # the for loop below will always result in it being >= 0.
        u = -1

        for i in range(n):
            # Loop through all nodes (the for statement above does that) then check whether it has been visited (i.e.
            # if its neighbours have been considered); if it hasn't been visited, we see if its recorded shortest path
            # is smaller than the shortest path of the node we are currently looking at; if it is, we move to this
            # node. Ultimately, when we begin this process, 0 will be the smallest in an array of infinities and we
            # will start with u as the src node. Next time round, u will end up being src's closest neighbour. After
            # that, u will end up being the un-accessed node that is closest overall to src, which we indeed want to be
            # the case.
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        # Below will be the case if all the nodes have been visited apart from one or more nodes that are inaccessible
        # from src, because, with visitations, we choose the node with the smallest cumulative distance; if at this
        # point that is still infinity, this must mean that this node has no predecessors that are accessible,
        # otherwise its cumulative distance would be finite.
        if dist[u] == float('inf'):
            break

        # Set the node whose neighbours are being considered as visited so that we don't do the following code for the
        # same node again
        visited[u] = True

        # Compare the distance to each neighbour to the current shortest distance to that neighbour. If we find a
        # shorter distance to the neighbour through the current node, update the distance with the distance to the
        # current node + the length of the edge to the neighbour.
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l

    return dist


def lazy_dijkstras(graph, src):
    """Also from https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/. More efficient than
    naive_dijkstras for sparse graphs, where each point is not connected to every other point.

    Time complexity: O(n*log(n))
    """
    # See identical code in naive_dijkstras for an explanation of the below 4 lines
    n = len(graph)
    dist = [float('inf') for _ in range(n)]
    dist[src] = 0
    visited = [False for _ in range(n)]

    # Set up a priority queue. First element: src node with a distance of 0.
    pq = [(0, src)]

    # I think what will happen is that, instead of doing the inner for loop in naive_dijkstras, we will simply look
    # right at the front of the list, do the neighbours bit, then discard the front of the list; with the for loop,
    # we'd then take O(n) time to look for the next smallest, but with the priority queue, we make sure this is always
    # at the front of the list. However, with heapq, this will use sift_up or sift_down (see
    # C:\Users\james\PycharmProjects\heaps\youTube1.py) to make sure order is correct everytime something is added,
    # which each have a time complexity of O(log(n))
    # (While there are nodes to process)
    while len(pq) > 0:
        # Initially, get the source, discard current distance. Distance was only used to position the node in the
        # priority queue, but it is already recorded in 'dist'.
        _, u = heapq.heappop(pq)

        # If node has been visited, skip
        if visited[u]:
            continue

        # Set the node to visited
        visited[u] = True

        # Loop through nodes adjacent, like we did in naive_dijkstras. Check the node and distance.
        for v, l in graph[u]:

            # If the current node's distance + length (l) of edge to its neighbour (v) is smaller than the distance of
            # v from src that has already been recorded, replace that distance and push the node visited into the
            # priority queue.
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))

    return dist

if __name__ == '__main__':

    # For my shortest path algorithm, I am first going to let the inputs be a bunch of weighted edges. Each edge will be
    # in the form of a list, where the first element is the current node, the second element is the node the edge
    # travels to, and the third element is the weight of the edge. For this example, going to make the edges the same
    # as that used to test the function shortest_path in C:\Users\james\PycharmProjects\graphs\graphs\youTube1.py, so
    # that I can make sure both functions are consistent for the case in which the weights of the edges are both 1.

    # edges = [
    #     ['a', 'b', 1],
    #     ['b', 'c', 1],
    #     ['a', 'c', 5]
    # ]
    #
    # print(shortest_path(edges, 'a'))

    # Following https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/ -- here, the nodes are represented
    # by numbers.
    # In each value, there's a tuple containing the next node and the weight of the edge from the key to this next node
    graph = {
        0: [(1, 1)],
        1: [(0, 1), (2, 2), (3, 3)],
        2: [(1, 2), (3, 1), (4, 5)],
        3: [(1, 3), (2, 1), (4, 1)],
        4: [(2, 5), (3, 1)]
    }

    # print(naive_dijkstras(graph, 1))
    print(lazy_dijkstras(graph, 1))