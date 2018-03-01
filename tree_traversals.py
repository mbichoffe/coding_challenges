from trees_and_bsts import BinaryTree, create_parse_tree
"""
Trees  may be traversed in depth-first or breadth-first order. 
There are three common ways to traverse them in depth-first order: 
in-order, pre-order and post-order. 
Beyond these basic traversals, various more complex or hybrid schemes are 
possible, such as depth-limited searches like iterative deepening depth-first 
search.
Depth-first search is easily implemented via a stack, including recursively 
(via the call stack), while breadth-first search is easily implemented 
via a queue, including corecursively.
preorder

In a preorder traversal, we visit the root node first, then recursively do a
preorder traversal of the left subtree, followed by a recursive preorder
traversal of the right subtree.

Example: reading a book 
Root: Book
Root.Child1: Chapter1
Root.Child1.Child1: Section1.2
...
Root.Child2: Chapter2


inorder

In an inorder traversal, we recursively do an inorder traversal on the left
subtree, visit the root node, and finally do a recursive inorder traversal of
the right subtree.

postorder

In a postorder traversal, we recursively do a postorder traversal of the left
subtree and the right subtree followed by a visit to the root node.

for the tree:


            F
          /   \
         B     G
        / \     \
       A   D     I
          / \   /
         C   E H

"""

def preorder(tree):
  """Pre-order: F, B, A, D, C, E, G, I, H."""
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def iterative_preorder(node):
  if not node:
    return
  s = [] #empty stack
  s.append(node)
  while len(s) > 0:
    node = s.pop()
    iterative_preorder(node)
    #right child is pushed first so that left is processed first
    if node.right:
      s.append(node.right)
    if node.left:
      node.append(node.left)


def postorder(tree):
  """Post-order: A, C, E, D, B, H, I, G, F."""
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def iterative_postorder(node):
  s = [] #stack
  last_node_visited = None
  while (len(s) > 0) or (node is not None):
    if node:
      s.append(node)
      node = node.left
    else:
      peek_node = s[-1]
      #if right child exists and traversing node from 
      # left to right child, then move right
      if (peek_node.right and last_node_visited != peek_node.right):
        node = peek_node.right
      else:
        iterative_postorder(peek_node)
        last_node_visited = s.pop()

def inorder(tree):
  """In-order: A, B, C, D, E, F, G, H, I."""
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

"""BREADTH-FIRST SEARCH"""

def levelorder(tree):
   #Write code Here
    to_visit = []
    to_visit.append(tree)
    while len(to_visit):
        current = to_visit.pop(0)
        print current.getRootVal(),
        if current.getLeftChild():
            to_visit.append(current.getLeftChild())
        if current.getRightChild():
            to_visit.append(current.getRightChild())

"""
To traverse any tree with depth-first search, 
perform the following operations recursively at each node:

1. Perform pre-order operation.
2. For each i from 1 to the number of children do:
      1. Visit i-th, if present.
      2. Perform in-order operation.
3. Perform post-order operation.