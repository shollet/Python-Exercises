class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
 
    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

# Line 1: def append(self, value):

# This line is defining a new method for the LinkedList class, named append. This method takes two arguments: self, a reference to the instance of the LinkedList class that this method is being called on, and value, the data for the new node that will be appended at the end of the list.

# Line 2: new_node = Node(value)

# This line creates a new instance of the Node class with the given value. The new_node variable is a local variable in the append method that holds a reference to the new node.

# Line 3-6:

# if self.head is None and self.tail is None: 
#     self.head = new_node 
#     self.tail = new_node
# These lines check if the LinkedList is empty, that is, the head and tail are both None. If it is empty, it assigns the head and tail of the LinkedList to the new_node. Essentially, the new node becomes the first and only node in the list.

# Line 7-8:

# else: 
#     self.tail.next = new_node 
#     self.tail = new_node
# These lines execute if the LinkedList is not empty. It sets the next attribute of the current tail node to new_node, meaning it connects the last node of the LinkedList to the new_node. Then, it updates the tail attribute of the LinkedList to new_node, as new_node is now the last node in the list.

# Line 9: self.length += 1

# This line increments the length attribute of the LinkedList by 1. This is because we've just added a new node to the list, increasing the total number of nodes in the list by 1.