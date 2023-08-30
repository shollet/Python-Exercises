# Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree. You may assume that each node has a link to its parent.

class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node


def inOrderSuccessor(root, n):
    def minValue(node):
        current = node
        while current:
            if not current.left:
                break
            current = current.left
        return current
    
    if n.right:
         return minValue(n.right)
    
    parent = n.parent
    while parent:
        if n != parent.right:
            break
        n = parent
        parent = parent.parent
    return parent 