#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A priority queue acts like a queue in that you dequeue an item by removing it
from the front. However, in a priority queue the logical order of items inside
a queue is determined by their priority.

Thus when you enqueue an item on a priority queue, the new item may move all
the way to the front. We will see that the priority queue is a useful data
structure for some of the graph algorithms we will study in the next chapter.

You can probably think of a couple of easy ways to implement a priority queue
using sorting functions and lists. However, inserting into a list is O(n)
and sorting a list is O(nlogn). We can do better. The classic way to implement
a priority queue is using a data structure called a binary heap. 
A binary heap will allow us both enqueue and dequeue items in O(logn).

The binary heap is interesting to study because when we diagram the heap it 
looks a lot like a tree, but when we implement it we use only a single list as
an internal representation. The binary heap has two common variations: the min
heap, in which the smallest key is always at the front, and the max heap,
in which the largest key value is always at the front.
"""

"""
In order to make our heap work efficiently, we will take advantage of the
logarithmic nature of the binary tree to represent our heap.
In order to guarantee logarithmic performance, we must keep our tree balanced.
 A balanced binary tree has roughly the same number of nodes in the left and
right subtrees of the root. In our heap implementation we keep the tree
balanced by creating a complete binary tree.

**The exception to this is the bottom level of the tree, which we fill in from
left to right.**

"""

class MinBinHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0
# The next method we will implement is insert. The easiest, and most efficient,
# way to add an item to a list is to simply append
# the item to the end of the list.
# We will probably violate the heap structure property.
# But we can write a method that will allow us to regain the heap structure
# property by comparing the newly added item with its parent.
# if the newly added item is less than its parent, then we can swap the item
# with its parent
# Here is where the wasted element in heap is importand
# The parent of any current node can be computed by dividing the index of the
# current node by 2.
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize+1
        self.percUp(self.currentSize)

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            # no right child
            return i * 2
        else:
            # if left child is greater than right child
            # return i of smaller child
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2 + 1
            else:
                return i * 2

    def percDown(self, i):
        # left child of a parent is found at 2p
        # right child is found at 2p + 1
        # while there are children left
        # get min child index
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            # swap the indexes
            i = mc

    def delMin(self):
        # root of the tree is the smallest item
        # restore the root item by taking the last item in the list and
        # moving it to the root position
        return_val = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return return_val

    def buildHeap(self, alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1


bh = MinBinHeap()
bh.buildHeap([9,5,6,2,3])


print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())


"""
to implement max heap, invert the value of the keys