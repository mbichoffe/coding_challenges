
"""
Write a function to check that a binary tree ↴ is a valid binary search tree. 

A binary search tree is a binary tree in which, for each node:

The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups. If the tree is balanced, we can search for a
given value in the tree in O(\lg{n})O(lgn) time.

"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right

    def insert_left(self, value):

        self.left = TreeNode(value)
        return self.left

def is_balanced(tree):

    if not tree:
        return True

    node_and_bounds = [(tree, float("-inf"), float("inf"))]

    while node_and_bounds:

        curr_node, lower_bound, upper_bound = node_and_bounds.pop()

        if (curr_node.value < lower_bound) or (curr_node.value > upper_bound):
            return False

        if curr_node.left:
            node_and_bounds.append((curr_node.left, lower_bound, curr_node.value))

        if curr_node.right:
            node_and_bounds.append((curr_node.right, curr_node.value, upper_bound))


    return True



    
a= TreeNode(50)
b = a.insert_right(80)
c = b.insert_right(90)
d = b.insert_left(70)
e = a.insert_left(30)
f = e.insert_left(20)
g = e.insert_right(40)


    
print(is_balanced(a))


a= TreeNode(50)
b = a.insert_right(80)
c = b.insert_right(90)
d = b.insert_left(70)
e = a.insert_left(30)
f = e.insert_left(20)
g = e.insert_right(60)


    
print(is_balanced(a))

