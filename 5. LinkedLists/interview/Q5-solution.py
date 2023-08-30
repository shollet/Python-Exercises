from LinkedList import *

def intersection(l1, l2):
    if l1.tail is not l2.tail:
        return False

    len1 = len(l1)
    len2 = len(l2)

    shorter = l1 if len1 < len2 else l2
    longer = l2 if len1 < len2 else l1

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode


def addSameNode(l1, l2, value):
    temp = Node(value)
    l1.tail.next = temp
    l1.tail = temp
    l2.tail.next = temp
    l2.tail = temp

l1 = LinkedList()
l1.generate(3,0,10)

l2 = LinkedList()
l2.generate(4,0,10)

addSameNode(l1, l2, 7)
addSameNode(l1, l2, 11)
addSameNode(l1, l2, 14)
addSameNode(l1, l2, 15)

print(l1)
print(l2)

print(intersection(l1, l2))
