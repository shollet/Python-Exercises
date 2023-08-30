# You are given the heads of two sorted linked lists list1 and list2. 

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.   

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
        temp = ListNode(-1)
        prevNode = temp
        # l1, l2 same length
        while l1 and l2:

            if l1.val > l2.val:
                prevNode.next = l2
                l2 = l2.next

            else:
                prevNode.next = l1
                l1 = l1.next        

            prevNode = prevNode.next
 
        # extra
        prevNode.next = l1 if l1 else l2
 
        return temp.next