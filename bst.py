"""
A binary search tree is a binary tree in which, for each node:

The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups. If the tree is balanced, we can search for
a given value in the tree in O(\lg{n})O(lgn) time.

"""

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, currentNode): 

        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)

        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(self, key, val, parent=currentNode)
        else:
            currentNode.replaceNodeData(self, self.key)

    def __setitem__(self, key, val):  # overloads [] operator for assignment
        self.put(key, val)


    def get(self, key):
        if self.root:
            result = self._get(key, self.root)

            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):

        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            self._get(key, currentNode.leftChild)
        else:
            self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):  #overloads in operator
        if self._get(self, key, self.root):
            return True
        return False


    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')

        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1 

        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(currentNode):

        #node has no children:
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            successor = currentNode.findSuccessor()
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload

        else: #has only one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                if currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.rightChild.rightChild)
           else:
              if currentNode.isLeftChild():
                  currentNode.rightChild.parent = currentNode.parent
                  currentNode.parent.leftChild = currentNode.rightChild
              elif currentNode.isRightChild():
                  currentNode.rightChild.parent = currentNode.parent
                  currentNode.parent.rightChild = currentNode.rightChild
              else:
                  currentNode.replaceNodeData(currentNode.rightChild.key,
                                     currentNode.rightChild.payload,
                                     currentNode.rightChild.leftChild,
                                     currentNode.rightChild.rightChild)

    def findSuccessor(self):
        successor = None
        if self

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild and self.leftChild)

    def hasAnyChildren(self):
        return any(self.rightChild, self.leftChild)

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
