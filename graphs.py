#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Graphs are a more general structure than the trees we studied in the last 
chapter; in fact you can think of a tree as a special kind of graph. Graphs
can be used to represent many interesting things about our world, including
systems of roads, airline flights from city to city, how the Internet is
connected, or even the sequence of classes you must take to complete a major
in computer science.
Terms:

Vertex
A vertex (also called a “node”) is a fundamental part of a graph.
It can have a name, which we will call the “key.” A vertex may also have
additional information. We will call this additional information the “payload.”

Edge
An edge (also called an “arc”) is another fundamental part of a graph.
An edge connects two vertices to show that there is a relationship between
them. Edges may be one-way or two-way. If the edges in a graph are all one-way,
we say that the graph is a directed graph, or a digraph. The class
prerequisites graph shown above is clearly a digraph since you must take some
classes before others.

Weight
Edges may be weighted to show that there is a cost to go from one vertex to
another. For example in a graph of roads that connect one city to another,
the weight on the edge might represent the distance between the two cities.

Path
A path in a graph is a sequence of vertices that are connected by edges.
Formally we would define a path as w1,w2,...,wn such that (wi,wi+1)∈E for all
1≤i≤n−1. The unweighted path length is the number of edges in the path,
specifically n−1. The weighted path length is the sum of the weights of all
the edges in the path. For example in Figure 2 the path from V3 to V1 is the
sequence of vertices (V3,V4,V0,V1).
The edges are {(v3,v4,7),(v4,v0,1),(v0,v1,5)}.

Cycle
A cycle in a directed graph is a path that starts and ends at the same vertex.
For example, in Figure 2 the path (V5,V2,V3,V5) is a cycle.
A graph with no cycles is called an acyclic graph. A directed graph with no
cycles is called a directed acyclic graph or a DAG. We will see that we can
solve several important problems if the problem can be represented as a DAG.


The graph abstract data type (ADT) is defined as follows:

- Graph() creates a new, empty graph.

- addVertex(vert) adds an instance of Vertex to the graph.

- addEdge(fromVert, toVert) Adds a new, directed edge to the graph that
connects two vertices.

- addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the
graph that connects two vertices.

- getVertex(vertKey) finds the vertex in the graph named vertKey.

- getVertices() returns the list of all vertices in the graph.
in returns True for a statement of the form vertex in graph, if the given
vertex is in the graph, False otherwise.

Beginning with the formal definition for a graph there are several ways we can
implement the graph ADT in Python. We will see that there are trade-offs in
using different representations to implement the ADT described above.
There are two well-known implementations of a graph, the adjacency matrix and
the adjacency list. We will explain both of these options, and then implement
one as a Python class.

Adjacency Matrix: 

One of the easiest ways to implement a graph is to use a two-dimensional matrix. 
 In this matrix implementation, each of the rows and columns represent a
 vertex in the graph.


Adjacency List:

A more space-efficient way to implement a sparsely connected graph is to use
an adjacency list. In an adjacency list implementation we keep a master list
of all the vertices in the Graph object and then each vertex object in the
graph maintains a list of the other vertices that it is connected to.

Implementation:

In our implementation of the Graph abstract data type we will create two
classes (see Listing 1 and Listing 2), Graph, which holds the master list
of vertices, and Vertex, which will represent each vertex in the graph.

"""
# Each vertex uses a dictionary to keep track of the dictionaries to which it
# is connected, and the weight of each edge.
# This dictionary is called connectedTo
# The addNeighbor is used to connect one vertex to another
# the getConnections returns all of the vertices in the adjacency list
# as represented by the connectedTo instance variable
# The getWeight method returns the weight of an edge from this vertex 
# to the vertex passed as a parameter

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: '+ str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

# Maps vertex names to vertex objects
# Holds master list of vertices
# getVertices method returns the names of all vertices in the graph
# iter makes it easy to iterate over all the vertex objects in a graph

class Graph:

    def __init__(self):

        self.vertList = {}
        self.numVertices = 0 

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
g.vertList
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for vert in g:
    for w in vert.getConnections():
        print(("{}, {}").format(vert.getId(), w.getId()))

"""
THE WORD LADDER PROBLEM
To begin our study of graph algorithms let’s consider the following
puzzle called a word ladder. Transform the word “FOOL” into the word “SAGE”.
In a word ladder puzzle you must make the change occur gradually by changing
one letter at a time. At each step you must transform one word into anothe
word, you are not allowed to transform a word into a non-word. 
The word ladder puzzle was invented in 1878 by Lewis Carroll,
the author of Alice in Wonderland. The following sequence of words shows
one possible solution to the problem posed above.

FOOL
POOL
POLL
POLE
PALE
SALE
SAGE
There are many variations of the word ladder puzzle. For example you
might be given a particular number of steps in which to accomplish the
transformation, or you might need to use a particular word. In this section
we are interested in figuring out the smallest number of transformations needed
to turn the starting word into the ending word.

Not surprisingly, since this chapter is on graphs, we can solve this problem
using a graph algorithm. Here is an outline of where we are going:

Represent the relationships between the words as a graph.
Use the graph algorithm known as breadth first search to find an
efficient path from the starting word to the ending word.

We could use several different approaches to create the graph we need to solve
this problem. Let’s start with the assumption that we have a list of words that
are all the same length. As a starting point, we can create a vertex in the
graph for every word in the list. To figure out how to connect the words,
we could compare each word in the list with every other. When we compare we are
looking to see how many letters are different. If the two words in question are
different by only one letter, we can create an edge between them in the graph.
For a small set of words that approach would work fine; however let’s suppose
we have a list of 5,110 words. Roughly speaking, comparing one word to every
other word on the list is an O(n2) algorithm. 
For 5,110 words, n2 is more than 26 million comparisons.

We can do much better by using the following approach.
Suppose that we have a huge number of buckets, each of them with a four-letter
word on the outside, except that one of the letters in the label has been
replaced by an underscore. For example, consider  we might have a bucket labeled “pop_.”
As we process each word in our list we compare the word with each bucket, 
using the ‘_’ as a wildcard, so both “pope” and “pops” would match “pop_.” 
Every time we find a matching bucket, we put our word in that bucket.
Once we have all the words in the appropriate buckets we know that all
the words in the bucket must be connected.

_OPE: POPE ROPE NOPE HOPE LOPE MOPE COPE
P_PE: POPE PIPE PAPE
PO_E: POPE POLE PORE POSE POKE

"""
def buildGraph(wordfile):
    d = {}
    g = Graph()

    w = open(wordfile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)





