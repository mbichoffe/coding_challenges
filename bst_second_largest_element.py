"""Write a function to find the 2nd largest element in a binary search tree."""

  class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# check if root has right child
    # if yes, continue checking right until reach leaf
    # else, return root value

def find_largest_element(tree):

    nodes_stack = []
    nodes_stack.append(tree)

    while nodes_stack:
        current_node = nodes_stack.pop()
        if current_node.right:
            if current_node.right.right:
                nodes_stack.append(current_node.right)
            else:
                return current_node.value

    return current_node.value

### Recursive solution ###
#this recursion finds the largest element in a tree:
def find_largest_element(tree):
    if root_node.right:
        return find_largest_element(root_node.right)
    return root_node
"""
Our first thought might be, "it's simply the parent of the largest element!" 
That seems obviously true when we imagine a nicely balanced tree like this one:

  .      ( 5 )
        /     \
      (3)     (8)
     /  \     /  \
   (1)  (4) (7)  (9)
But what if the largest element itself has a left subtree?

  .      ( 5 )
        /     \
      (3)     (8)
     /  \     /  \
   (1)  (4) (7)  (12)
                 /
               (10)
               /  \
             (9)  (11)

Here the parent of our largest is 8, but the second largest is 11.

Drat, okay so the second largest isn't necessarily the parent of the largest...
back to the drawing board...

Wait. No. The second largest is the parent of the largest if the largest does 
not have a left subtree. If we can handle the case where the largest does have 
a left subtree, we can handle all cases, and we have a solution.

So let's try sticking with this. How do we find the second largest when the
largest has a left subtree?

It's the largest item in that left subtree! Whoa, we freaking just wrote a
function for finding the largest element in a tree. We could use that here!

"""

#always check for edge cases
# in this case, if we're looking for second largest item, it means there must 
# be at least two items
def find_second_largest_item(root_node):

    current = root_node

    while current: 

    if current.left and not current.right:
        # if there are no right nodes in the subtree
        #the second largest item will be the largest item in that left subtree
            second_largest = find_largest_element(largest_item)

    if not current.left and current.right:


        #current is parent of the largest, and largest has no children:
        if current.right and not current.right.left and not current.right.right:
            return current.value

    current = current.right

"""
Complexity:
We are doing one walk down our BST, which means O(h) time, where h is the 
height of the tree (that's O(log n) if the tree is balanced, O(n) otherwise.
O(1)space.
