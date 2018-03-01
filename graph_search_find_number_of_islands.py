"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1} 
Output : 5

This is an variation of the standard problem: “Counting number of connected
components in a undirected graph”.

Before we go to the problem, let us understand what is a connected component. 
A connected component of an undirected graph is a subgraph in which every
two vertices are connected to each other by a path(s), and which is connected
to no other vertices outside the subgraph.
A graph where all vertices are connected with each other, has exactly one
connected component, consisting of the whole graph. Such graph with only
one connected component is called as Strongly Connected Graph.

The problem can be easily solved by applying DFS() on each component. 
In each DFS() call, a component or a sub-graph is visited.
 We will call DFS on the next un-visited component. 
 The number of calls to DFS() gives the number of connected components. 
 BFS can also be used.

 A cell in 2D matrix can be connected to 8 neighbors. 
 So, unlike standard DFS(), where we recursively call for all adjacent 
 vertices, here we can recursive call for 8 neighbors only. 
 We keep track of the visited 1s so that they are not visited again.

 """
 # Count islands on a boolean 2D matrix:
class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isSafe(self, i, j, visited):
        # check for corner indexes and valid range
        # check if value is one
        # check if not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])

    def DFS(self, i, j, visited):
        # These arrays are used to get row and column numbers
        # of eight neighbors
        # of a given cell

        # These arrays are used to get row and column index
        # of all possible neighbors on a given cell
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # mark this cell as visited
        visited[i][j] = True
        count_cells = 1

        # Recur for all connected neighbors:
        for k in range(8):
            if self.isSafe(i + row_nbr[k], j + col_nbr[k], visited):
                count_cells += self.DFS(i + row_nbr[k], j + col_nbr[k], visited)

        return count_cells


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    # main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # make a bool list to mark visited cells
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        #initialize count as 0 and traverse 
        # through all the cells of given matrix
        count = 0
        max_connected_cells = 0

        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cel with value 1 is not visited yet,
                # then a new island was found
                if visited[i][j] == False and self.graph[i][j] == 1:
                    #visit all the cells in this island
                    # and increment island count
                    count_cells = self.DFS(i, j, visited)
                    max_connected_cells = max(max_connected_cells, count_cells)
                    count += 1
        return count, max_connected_cells


#Time complexity: O(ROW x COL)


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g= Graph(row, col, graph)
 
print("Number of islands is :")
print(g.countIslands())