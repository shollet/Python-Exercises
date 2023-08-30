class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head
 
        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return head


# class ListNode(object):

# This creates a new class named ListNode. In the context of linked lists, each 'node' or instance of this class will hold a value and a reference to another ListNode instance.

# def __init__(self, val=0, next=None):

# This line defines the initializer method for instances of the ListNode class. When a new ListNode is created, it can be given a value (val) and a reference to the next node (next).

# self.val = val

# Here, the value provided when the ListNode instance is created is assigned to the instance's 'val' attribute.

# self.next = next

# Similar to the line above, the 'next' argument provided when the ListNode instance is created is assigned to the instance's 'next' attribute.

# class Solution(object):

# This line declares a new class named Solution. This class will include methods to solve the problem, in this case, removing duplicates from a sorted linked list.

# def deleteDuplicates(self, head):

# This line defines a method in the Solution class that will take in the head of a linked list and remove any duplicates from it.

# current_node = head

# This line initializes a variable current_node to the head of the linked list. This variable will be used to traverse the list.

# while current_node is not None and current_node.next is not None:

# This line starts a while loop that will run as long as there are nodes left in the linked list to check. This prevents an error that would occur if we tried to access the 'next' attribute of a None node.

# if current_node.val == current_node.next.val:

# This line checks if the current node and the next node have the same value. If they do, it means there's a duplicate that needs to be removed.

# current_node.next = current_node.next.next

# If the current and next node are duplicates, this line removes the next node by skipping over it and pointing the current node's 'next' attribute to the node after the next one.

# else: current_node = current_node.next

# If the current node and the next node aren't duplicates, this line moves on to the next node in the list.

# return head

# This line returns the head of the linked list. At this point, any duplicates that were in the list have been removed.