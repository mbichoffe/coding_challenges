"""
A topological sort takes a directed acyclic graph and produces a linear
ordering of all its vertices such that if the graph G contains an edge (v,w)
then the vertex v comes before the vertex w in the ordering. Directed acyclic
graphs are used in many applications to indicate the precedence of events.
Making pancakes is just one example; other examples include software project
schedules, precedence charts for optimizing database queries,
and multiplying matrices.
"""
#Python program to print topological sorting of a DAG
from collections import defaultdict

#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) #dictionary containing adjacency List
        self.V = vertices #No. of vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):
 
        # Mark the current node as visited.

        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Push current vertex to stack which stores result
        stack.insert(0,v)
 
    # The function to do Topological Sort. It uses recursive 
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        # Print contents of stack
        print(stack)

class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        """
        A defaultdict works exactly like a normal dict,
        but it is initialized with a function (“default factory”)
        that takes no arguments and provides the default value for
        a nonexistent key.
        """
        self.V = num_vertices # number of vertices

    def addEdge(self, vertex, connected_vertex):
        self.graph[vertex].append(connected_vertex)


    def topologicalSortUtil(v, visited, stack):
        visited[v] = True

        for _ in self.graph[v]:
            if visited[_] == False:
                self.topologicalSortUtil(_, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        #initiate a list where we can keep track of visited 
        visited = [False]*self.V
        stack = []

        for v in range(self.V):
            if visited[v] == False:
                self.topologicalSortTool(v, visited, stack)

        print(stack)



g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g)
print("Following is a Topological Sort of the given graph")
g.topologicalSort()
