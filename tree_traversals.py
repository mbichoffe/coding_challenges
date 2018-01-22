from trees_and_bsts import BinaryTree, create_parse_tree
"""

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

"""

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def levelorde(tree):
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
