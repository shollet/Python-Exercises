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
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

# def remove_duplicates(self): This line is defining the function remove_duplicates within the LinkedList class.

# if not self.head: This line checks if the head of the LinkedList is None, which would indicate that the list is empty.

# return If the list is empty, the function ends execution and returns None.

# unique_values = set([self.head.value]) If the list is not empty, the function creates a set unique_values and adds the value of the head node to it.

# current_node = self.head The function sets current_node to the head of the list. This variable will be used to traverse the list.

# while current_node.next: This line starts a while loop that will continue as long as the next attribute of the current_node is not None.

# if current_node.next.value in unique_values: This line checks if the value of the next node is already in the set of unique values.

# current_node.next = current_node.next.next If the value is in the set, this line removes the next node from the list by skipping over it and setting the next attribute of the current node to the node after the next node.

# self.length -= 1 Since a node was removed, the length of the list is decremented by 1.

# else: This is the other case where the value of the next node is not in the set.

# unique_values.add(current_node.next.value) This line adds the value of the next node to the set of unique values.

# current_node = current_node.next Since the next node is unique, we move forward to the next node.

# self.tail = current_node After the loop, the current_node will be the last node in the list. So, we update the tail of the list to be current_node.