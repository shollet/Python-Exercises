# Write a method to insert a new element at the end of a singly linked list. The logic should cover edge cases such as empty linked list or linked list with some elements in it.

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
        newNode = Node(value)

        if self.length == 0:        # empty
            self.head = newNode
            self.tail = newNode
        else:                       # not empty
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
