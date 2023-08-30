class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def removeElements(self, head, val):
        dummy_head = ListNode(-1)
        dummy_head.next = head
 
        prev_node, curr_node = dummy_head, head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
 
        return dummy_head.next
    
# class ListNode(object):

# This line defines a new class named ListNode. This class represents a node in a linked list, which can store a value and a reference to the next node in the list.

# def __init__(self, val=0, next=None):

# This is the initializer method for the ListNode class. When we create a new ListNode, we can specify its value and the next node it should point to.

# self.val = val

# This line assigns the provided value to the 'val' attribute of the ListNode.

# self.next = next

# This line assigns the provided next node to the 'next' attribute of the ListNode.

# class Solution(object):

# This line defines a new class named Solution, which contains our solution to the problem.

# def removeElements(self, head, val):

# This line starts the definition of our solution method, which takes a head of a linked list and a value to remove from the list.

# dummy_head = ListNode(-1)

# Here we're creating a dummy head node. This node acts as a placeholder and helps handle cases where we need to remove the actual head of the list.

# dummy_head.next = head

# This line sets the next node of our dummy head to be the actual head of the list. This effectively places our dummy head node at the start of the list.

# prev_node, curr_node = dummy_head, head

# This line initializes two pointers that we'll use to traverse the list. 'prev_node' will keep track of the node before 'curr_node' as we move through the list.

# while curr_node:

# This line starts a loop that will continue as long as 'curr_node' is not None, i.e., until we've checked every node in the list.

# if curr_node.val == val:

# This line checks if the value of the current node is the value we want to remove.

# prev_node.next = curr_node.next

# If the current node's value is the value we want to remove, this line skips over the current node by setting the 'next' attribute of the previous node to the node after the current one.

# else: prev_node = curr_node

# If the current node's value isn't the one we want to remove, this line moves the 'prev_node' pointer to the current node.

# curr_node = curr_node.next

# This line moves the 'curr_node' pointer to the next node in the list, regardless of whether we removed the current node or not.

# return dummy_head.next

# After we've checked every node in the list, this line returns the first node after our dummy head node. This will be the head of the new list with the specified values removed.