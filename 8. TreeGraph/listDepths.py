# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (ie , if you have a tree with depth D, you’ll have D linked lists)

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1
    else:
        left = 1 + depth(tree.left)
        right = 1 + depth(tree.right)
        if left > right:
            return left
        else:
            return right

def treeToLinkedList(tree, custDict = {}, d = None):
    if d is None:
        d = depth(tree)
    if custDict.get(d) is None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left is not None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right is not None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict

mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)

mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
for depthLevel, linkedList in custDict.items():
    print("{0} {1}".format(depthLevel, linkedList))
    
