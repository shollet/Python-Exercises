# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left



def findFirstCommonAncestor(n1, n2, root):
    if not root:
        return None

    if root == n1 or root == n2:
        return root
    
    
    left = findFirstCommonAncestor(n1,n2,root.left)
    right = findFirstCommonAncestor(n1,n2,root.right)
    

    if left and right:
        return root
    
    if left:
        return left
    
    if right:
        return right
    
    return None

        

