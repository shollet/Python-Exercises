class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def middleNode(self, head):
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            
        return head
    
# class Solution(object): We're declaring a new class named Solution. In Python, we usually encapsulate related functions and variables inside a class.

# def middleNode(self, head): We're defining a method called middleNode inside the Solution class. This method takes two parameters: self, which is a reference to the current instance of the class, and head, which is the head of the linked list.

# fast = head Here, we're initializing a variable called fast and setting it equal to head. This variable will serve as one of our pointers that will traverse through the linked list.

# while fast and fast.next: This begins a while loop that will continue until fast is None (which would mean we've reached the end of the list) or fast.next is None (which would mean we're at the second to last node).

# head = head.next Within the loop, we're moving head one step forward in the list.

# fast = fast.next.next Then, we're moving fast two steps forward. This line also implicitly checks whether fast.next is None, since Python will raise an exception if we try to access None.next.

# return head Once the loop ends, head is now at the middle node of the list, so we return head.

# The purpose of this method is to find and return the middle node of a linked list. We do this by moving fast twice as fast as head. By the time fast reaches the end of the list, head will be at the middle.