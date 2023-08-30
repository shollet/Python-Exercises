# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = ListNode(-1)
 
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next
 
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
 
        return prehead.next
    
# class ListNode:: This line is declaring a class named ListNode. This class will be used to create nodes for the linked lists.

# def __init__(self, val=0, next=None):: The __init__ method is a special method in Python classes, it's the constructor method which is automatically called when an object of a class is instantiated. Here, it's used to initialize the val and next attributes of a ListNode.

# self.val = val: This sets the value of the node to the val argument provided.

# self.next = next: This sets the next attribute of the node to the next argument provided. This attribute will point to the next node in the linked list.

# def mergeTwoLists(l1, l2):: This is the function definition for mergeTwoLists which takes two sorted linked lists l1 and l2 as arguments.

# prehead = ListNode(-1): Here, we're creating a new node prehead with a value of -1. This is a dummy node, and the merged linked list will start from this node.

# prev = prehead: We're creating a pointer prev that will be used to traverse and build the new sorted list. We initially point it to prehead.

# while l1 and l2:: This loop will continue as long as there are nodes left in both l1 and l2.

# if l1.val <= l2.val:: This line compares the values of the current nodes of l1 and l2.

# prev.next = l1 and l1 = l1.next: If the value of the current node in l1 is less than or equal to the current node in l2, then we add l1's current node to the new list and move forward in l1.

# else:: If the value of the current node in l1 is greater than the current node in l2.

# prev.next = l2 and l2 = l2.next: Then we add l2's current node to the new list and move forward in l2.

# prev = prev.next: After adding a node from either l1 or l2 to the new list, we need to move forward in the new list as well.

# prev.next = l1 if l1 is not None else l2: After exiting the while loop, at least one of l1 and l2 is null, so we need to connect the non-null list to the end of the merged list.

# return prehead.next: We're returning prehead.next because prehead is a dummy node. The sorted, merged list starts from prehead.next.