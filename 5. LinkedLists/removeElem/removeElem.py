# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = ListNode(-1)
        temp.next = head

        prevNode = temp
        current = head
        while current:
            if current.val == val:
                prevNode.next = current.next
            else:
                prevNode = current
            current = current.next 
        return temp.next