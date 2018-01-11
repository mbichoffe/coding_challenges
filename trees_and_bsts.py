import operator
"""
List of lists representation of a tree
"""

# tree = ['a', #node
#         ['b', # left subtree
#             ['d', [], []],
#             ['e', [], []]]
#         ['c', # right subtree
#             ['f', [], []],
#             []
#         ]
#     ]

# print('left subtree =', tree[1])
# print('root', tree[0])
# print('right subtree=', tree[2])

"""
One very nice property of this list of lists approach is that the structure 
of a list representing a subtree adheres to the structure defined for a tree;
the structure itself is recursive! A subtree that has a root value and two 
empty lists is a leaf node. Another nice feature of the list of lists approach 
is that it generalizes to a tree that has many subtrees. In the case where the
tree is more than a binary tree, another subtree is just another list.
"""
# def BinaryTree(r):
#     return [r, [], []]

# def insertLeft(root, NewBranch):
#     current_left = root.pop(1) 
#     if len(current_left) > 0:
#         root.insert(1, [NewBranch, current_left, [], []])
#     else:
#         root.insert(1, [NewBranch, [], []])
#     return root

# def insertRight(root, NewBranch):
#     current_right = root.pop(2)
#     if len(current_right)>0:
#         root.insert(2, [NewBranch, current_right, [], []])
#     else:
#         root.insert(2, [NewBranch, [], []])

#     return root

# def getRootVal(root):
#     return root[0]

# def setRootVal(root,newVal):
#     root[0] = newVal

# def getLeftChild(root):
#     return root[1]

# def getRightChild(root):
#     return root[2]

###REPRESENTING A TREE WITH OOP###

class BinaryTree(object):

    def __init__(self, root):

        self.key = root
        self.rightChild = None
        self.leftChild = None


    def insertLeft(self, newNode):

        if self.leftChild:
            new_left_child = BinaryTree(newNode)
            new_left_child.leftChild = self.leftChild
            self.leftChild = new_left_child

        else:
            self.leftChild = BinaryTree(newNode)

    def insertRight(self, newNode):

        if self.rightChild:
            new_right_child = BinaryTree(newNode)
            new_right_child.rightChild = self.rightChild
            self.rightChild = new_right_child
        else:
            self.rightChild = BinaryTree(newNode)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, obj):
        self.key = obj


# r = BinaryTree('a')
# r.insertLeft('b')
# r.insertRight('c')
# r.getLeftChild().insertRight('d')
# r.getRightChild().insertLeft('e')


############PARSE TREES #########################

"""
Parse trees can be used to represent real-world constructions
like sentences or mathematical expressions.
I.E. ((7+3)∗(5−2))

How to build a parse tree from a fully parenthesized mathematical expression.
How to evaluate the expression stored in a parse tree.
How to recover the original mathematical expression from a parse tree.

STEP 1 = split expression string into a list of tokens



"""

def create_parse_tree(math_expression):

    tokens = math_expression.split()
    print(tokens)
    #start with an empty Binary tree
    parse_tree = BinaryTree('')

    # We need to keep track of current node as well as the parent
    # The tree interface provides us with a way to get children of a node
    # But how can we keep track of the parent?
    # A simple solution is to use a stack
    # Whenever we want to descend to a child of the current node, we push 
    # the current node to the stack. Whenever we want to return to the
    # parent of the current node, we pop the parent off the stack.
    # parent node stack

    parent_node = []
    parent_node.append(parse_tree)
    current_node = parse_tree
    for token in tokens:

        if token == '(':
            # add a new node as the left child of the current node, and
            current_node.insertLeft('')
            #push node to stack
            parent_node.append(current_node)
            # descend to the left child
            current_node = current_node.getLeftChild()

        elif token in ('+', '-', '/', '*'):
            current_node.setRootVal(token)
            current_node.insertRight('')
            parent_node.append(current_node)
            current_node = current_node.getRightChild()
            #  set the root value of the current node to the operator
            # represented by the current token. Add a new node as the right
            # child of the current node and descend to the right child.
        elif token not in ('+', '-', '/', '*', ')'):
            #set root value of current node to number and return to parent
            current_node.setRootVal(int(token))
            current_node = parent_node.pop()
        elif token == ')':
            current_node = parent_node.pop()
            #go to parent of current node
        else:
            raise ValueError

    return parse_tree


 #How to evaluate this tree?
# We can parse a tree by recusively evaluating each subtree
# Design for the recursive evaluation begins with identifying the base case
# A natural base case for recursive algorithms that operate on trees is to 
# check for a leaf node
# In a parse tree, the leaf nodes will always be operands (numbers)

def evaluate(parse_tree):

    operators = {
        '+': operator.add,  #add(2,2) returns 4
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    left_c = parse_tree.getLeftChild()
    right_c = parse_tree.getRightChild()

    if left_c and right_c:
        print(parse_tree.getRootVal())
        print(right_c.getRootVal())
        print(left_c.getRootVal())
        f = operators[parse_tree.getRootVal()]
        return f(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.getRootVal()

