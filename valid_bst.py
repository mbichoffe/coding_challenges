from trees_and_bsts import BinaryTree

"""
Write a function to check that a binary tree ↴ is a valid binary search tree. 

A binary search tree is a binary tree in which, for each node:

The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups. If the tree is balanced, we can search for a
given value in the tree in O(\lg{n})O(lgn) time.

"""

def is_balanced(tree):

    if not tree:
        return True

    nodes_stack = []
    nodes_stack.append(tree)

    while nodes_stack:
        current_node = nodes_stack.pop()
        left_node = current_node.left
        right_node = current_node.right
        if left_node:
            if current_node.value > left_node.value:
                nodes_stack.append(left_node)
            else:
               return False
        if right_node:
            if current_node.value < right_node.value:
                nodes_stack.append(right_node)
            else:
                return False
               

    return True