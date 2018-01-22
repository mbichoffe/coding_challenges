"""
Write a function to see if a binary tree ↴ is "superbalanced" (a new tree
property we just made up).

A tree is "superbalanced" if the difference between the depths of any two leaf
nodes is no greater than one.

"The difference between the min leaf depth and the max leaf depth is 1 or less"
"There are at most two distinct leaf depths, and they are at most 1 apart"

"""

class BinaryTreeNode:
    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """Debugging-friendly representation."""

        return "<BinaryNode %s>" % self.value

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_super_balanced(TreeNode):
    #a tree without nodes is superbalanced by definition
    if not treeNode:
        return True

    depths = [] # there are more than 2 items we return false

    #let's create a stack to be able to return to the parent nodes
    # a
    node_and_depth = []
    node_and_depth.append(TreeNode)

    while len(node_and_depth):

        #unpack node and depth from stack
        node, depth = node_and_depth.pop()

        #base case: leaf found
        if (not node.left) and (not node.right):

            if depth not in depths: 
                depths.append(depth)

            if len(depths) > 2 or \
                len(depths) == 2 and abs(depths[0]-depth[1]) > 1:

                return False

        else:

            if node.left:
                node_and_depth.append(node.left, depth+1)
            if node.right:
                node_and_depth.append(node.right, depth+1)

    return True



