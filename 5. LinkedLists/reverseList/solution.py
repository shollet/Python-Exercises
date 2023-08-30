class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def reverseList(self, head):
        prev_node = None
        curr_node = head
 
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node
    
# class Solution(object):

# This line is declaring a new class called Solution. Classes are a way of grouping related bits of code together, including methods, which are just functions that belong to a class.

# def reverseList(self, head):

# This line is defining a method of the Solution class called reverseList. This method will take in two parameters: self, which is a reference to the instance of the class, and head, which is the head node of the linked list you want to reverse.

# prev_node = None

# This line initializes a variable prev_node to None. This variable will be used to keep track of the previous node as we traverse the linked list.

# curr_node = head

# This line initializes another variable curr_node to the head of the linked list. This variable will be used to traverse the linked list.

# while curr_node is not None:

# This line starts a while loop that will continue until curr_node is None. This is essentially saying "keep going until we've visited every node in the linked list".

# next_node = curr_node.next

# Inside the while loop, this line saves the next node of curr_node before changing the next of curr_node. This is crucial because once we reverse curr_node.next, we lose the reference to the next node in the original list.

# curr_node.next = prev_node

# This line reverses the direction of the link between the current and the previous node. Instead of curr_node pointing to the next node in the original list, it now points back to the node before it.

# prev_node = curr_node

# This line shifts prev_node one step forward (to the right in the original list). Now, prev_node is the curr_node.

# curr_node = next_node

# This line also shifts curr_node one step forward. However, this uses next_node, which we saved before, to move curr_node to its original next node in the list.

# return prev_node

# After the while loop has completed, which means we have traversed and reversed all nodes in the list, curr_node is None (as this condition breaks the while loop) and prev_node is at the last node visited, which is the head of the reversed list. So, we return prev_node.