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
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

# def reverse(self): Defines a method named reverse in the LinkedList class.

# prev_node = None: Initializes prev_node to None. It keeps track of the previous node during traversal.

# current_node = self.head: Initializes current_node with the head of the linked list. The reverse operation starts from here.

# while current_node is not None: Starts a while loop that continues until the end of the linked list is reached.

# next_node = current_node.next: Saves the next node before overwriting current_node.next in the next step.

# current_node.next = prev_node: Reverses the link by setting the next of current_node to prev_node.

# prev_node = current_node: Updates prev_node to current_node for the next iteration.

# current_node = next_node: Moves the current_node one step forward for the next iteration.

# self.head, self.tail = self.tail, self.head: After the end of the loop, the head and tail are swapped to complete the reversal of the linked list.