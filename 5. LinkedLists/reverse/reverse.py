# Write a function to reverse a singly linked list. The function should return a new linked list that is the reverse of the original list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def reverse(self):
        # empty or one elem
        if self.length == 0 or self.length == 1:
            return self
        # multi
        else:
            prevNode = None
            current = self.head
            while current:
                nextNode = current.next
                current.next = prevNode
                prevNode = current
                current = nextNode
            temp = self.head
            self.head = self.tail
            self.tail = temp
            return self
        