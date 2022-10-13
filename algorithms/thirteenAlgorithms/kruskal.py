# https://www.youtube.com/watch?v=Yo7sddEVONg&t=78s:

# 1. Sort edges such that smaller weights are prioritised. Pick the lowest-cost edge; if there are multiple such edges,
# then it might be a good idea to choose between them
# randomly, but using a probability distribution in which edges connecting to nodes with higher degrees (more
# neighbours) are more likely to be chosen, since in many real-world solutions such nodes tend to receive more new
# neighbours than less connected ones, meaning you would want the minimum spanning tree to connect high-degree nodes
# two-way rather than leaving them as leaves, for example.

# 2. Make sure the edge picked doesn't create any cycles in MST.
# According to https://www.programiz.com/dsa/kruskal-algorithm, the most common way of avoiding cycles is using Union
# Find. This divides vertices into clusters and lets us check if the two vertices in the edge we are considering belong
# to the same cluster, in which case adding the edge would create a cycle in the MST.
# The Union-Find method here works like this:
# -> See C:\Users\james\postgradPycharm\dataStructures\unionFind\williamFiset.py
# -> Right off the bat, make a set for each vertex in the graph, where the set contains this vertex.
# -> When considering an edge connects u and v, then if u and v belong to the same set, don't add this edge to the MST;
# otherwise, add this edge to the MST and perform the union of the sets that u and v are currently in, so that you
# get a new set containing both the original sets.
# -> Do the above for every edge in the graph.

# 3. Keep selecting the remaining lowest-weight edges that don't violate the MST until the MST contains all the nodes
# from the graph. The number of edges to be selected in total must be V-1, as necessary for a MST.

# Can run at O(Elog(V)) with binary heaps.

# May run a little vaster with Fibonacci heap O(E + Vlog(V)) if V is much smaller than E--this is because Vlog(V) has
# a higher order of growth than E, so if E is similar to V, this tends to O(E + Vlog(V)) instead of being closer to
# O(E), which would be expected to be worse than O(Elog(V)), especially since E and V are similar.

# IN CODE BELOW:

# Sorting takes O(Elog(E)) time. Afterwards, iterate through all edges (of which there are E) and apply the find-union
# algorithm, whose find and union operations can take at most O(log(V)) time (so Elog(V)) in total, so sorting and then
# iterating through the edges takes O(Elog(E) + Elog(V)) time; E can be at most V**2, so O(logV) and O(logE) are the
# same--therefore, overall time complexity can be said to be either O(ElogE) or O(ElogV).

# Auxiliary space: O(V + E), which can be simplified to O(E) for similar reasoning to above.


class Graph:
    """https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

    Time complexity: O(ElogE) == O(ElogV)
    Auxiliary complexity: O(V + E) == O(V) == O(E)
    """

    def __init__(self, vertices):
        self.v = vertices   # Number of vertices
        self.graph = [] # Default dictionary to store graph

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Utility function to find set of an element i (uses path compression technique)
    # See https://www.youtube.com/watch?v=VHRhJWacxis for path compression
    def find(self, parent, i):
        """Returns the root of the component i is in and implements path compression in that component too."""

        # # Finding root
        # root = i
        # while parent[root] != root:
        #     root = parent[root]

        # # Path compression
        # while parent[i] != root:
        #     next = parent[i]
        #     parent[i] = root
        #     i = next
        # return root

        # A recursive version of the code, which includes both finding the root and also path compression too. Much 
        # more concise than the iterative code and the path compression used prior to the last call of find() in 
        # __main__ means there probably won't be many stack frames anyway, so not too much overhead re: efficiency 
        # loss
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        """When comparing two nodes mapped to index numbers x and y, this function finds the roots of their groups and
        makes one the parent of the other, based on the rank of each. Rank is a mapping of each root to a "rank"; here,
        the root with the higher rank becomes the parent of that with the lower rank. See 'find' function description
        for what 'parent' is.
        """
        # This is commented out because in kruskalMST(), we find the roots already (there called x and y) and pass them 
        # to union(). Of course, in other implementations of the union-find, you probably want union() to take arbitrary 
        # nodes instead and then check if their roots are the same before doing anything else (simply return if they are 
        # the same in that case)
        # xroot = self.find(parent, x)
        # yroot = self.find(parent, y)

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # If the ranks are the same, then make one of the roots (arbitrarily choosing xroot here) the root of the union
        # and increment this node's rank by 1.
        else:
            parent[y] = x
            # todo: find out if you really need to do the rank incrementation shown below
            rank[x] += 1

    def kruskalMST(self):
        """Finds a minimum spanning tree in this graph using Kruskal's algorithm."""

        mst = []

        # Step 1: sort all edges in ascending order (i.e. smallest one first) of weight. Creating a new graph in case
        # not allowed to modify the given graph. Creation is O(V + E).
        self.graph = sorted(self.graph,
                            # Remember, graph contains lists items of format [u, v, w], by virtue of add_edge, where
                            # item[2] would be w (weight)
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create v number of subsets with single elements
        for node in range(self.v):
            parent.append(node) # Remember, this is just an integer in the range [0, v)
            rank.append(0)

        i = 0   # Index variable used for sorted edges
        e = 0   # Index variable used for mst[]
        # Number of edges in MST will necessarily be equal to V-1
        while e < self.v - 1:

            # Step 2: pick the smallest edge and increment the index for the next iteration
            u, v, w = self.graph[i]
            i += 1

            # If including this edge doesn't cause a cycle (i.e. if u and v belong to different groups), include it in
            # result, increment 'e' for the next edge, and unify u's and v's groups.
            x = self.find(parent, u)
            y = self.find(parent, v)
            if not x == y:
                e += 1
                mst.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print('Edges in the constructed MST:')
        for u, v, weight in mst:
            minimum_cost += weight
            print('%d -- %d: weight == %d' % (u, v, weight))
        print(f"Minimum spanning tree's total weight: {minimum_cost}")

if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskalMST()