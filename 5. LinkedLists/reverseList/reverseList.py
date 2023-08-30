# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prevNode = None
        current = head
        while current:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode
        return prevNode