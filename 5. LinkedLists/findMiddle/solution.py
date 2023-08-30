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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
#     The approach, often called the "fast and slow pointer" technique or "tortoise and hare" algorithm, allows you to traverse the list only once, instead of first counting the elements and then accessing the middle one.



# def find_middle(self): - This line defines a new method find_middle in the LinkedList class. This method will be used to find the middle node of the linked list.

# if not self.head: - This line checks if the head of the linked list is None. If it is, that means the list is empty and there is no middle node to find.

# return None - If the linked list is empty (i.e., if self.head is None), this line will end the function and return None. This is because there is no middle node in an empty list.

# slow = self.head - This line initializes the slow pointer at the head of the linked list. This pointer will move one node at a time through the list.

# fast = self.head - This line initializes the fast pointer also at the head of the linked list. This pointer will move two nodes at a time through the list.

# while fast and fast.next: - This line starts a while loop that will continue as long as both fast and fast.next are not None. This ensures that we do not try to access a None value in the next line, which would raise an error.

# slow = slow.next - This line moves the slow pointer one node forward in the list.

# fast = fast.next.next - This line moves the fast pointer two nodes forward in the list. Because fast moves twice as fast as slow, by the time fast reaches the end of the list, slow will be at the middle.

# return slow - After the while loop, the slow pointer will be at the middle of the linked list. This line returns the slow node, which is the middle node of the list.