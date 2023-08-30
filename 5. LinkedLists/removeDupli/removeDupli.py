# Given a singly linked list, write a function that removes all the duplicates. use this linked list .

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
    
    def remove_duplicates(self):
        # empty and one elem
        if self.length == 0 or self.length == 1:
            return
        # multi elem
        else:
            nodes = set()
            current = self.head
            nodes.add(current.value)
            while current.next:
                if current.next.value in nodes:
                    current.next = current.next.next
                    self.length -= 1
                else:
                    nodes.add(current.next.value)
                    current = current.next
            self.tail = current

newlink = LinkedList()
newlink.remove_duplicates()
print(newlink)
newlink.append(10)
newlink.remove_duplicates()
print(newlink)
newlink.append(20)
newlink.remove_duplicates()
print(newlink)
newlink.append(40)
newlink.append(20)
newlink.append(40)
newlink.append(50)
newlink.append(10)
print(newlink)
newlink.remove_duplicates()
print(newlink)
