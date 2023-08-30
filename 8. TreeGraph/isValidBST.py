# Implement a function to check if a binary tree is a Binary Search Tree.

class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None


def isValidBST(root):
    
    def checkValidity(node, leftBound = float("-inf"), rightBound = float("inf")):
        if not node:
            return True
        val = node.val
        if val <= leftBound or val >= rightBound:
            return False
        if not checkValidity(node.right, val, rightBound) or not checkValidity(node.left, leftBound, val):
            return False
        return True

    return checkValidity(root)