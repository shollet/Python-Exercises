# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isBalanced(root):
    if not root:
        return 0
    left = isBalanced(root.left)
    if left == -1:
        return -1
    right = isBalanced(root.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return max(left, right) > -1