# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prevNode = None
        while slow:
            nextNode = slow.next
            slow.next = prevNode
            prevNode = slow
            slow = nextNode

        while prevNode:

            if head.val != prevNode.val:
                return False
            
            head = head.next
            prevNode = prevNode.next

        return True