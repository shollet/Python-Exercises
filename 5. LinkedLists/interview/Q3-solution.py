from LinkedList import *

def partition(l1, x):
    current = l1.head
    l1.tail = l1.head

    while current:
        next = current.next
        current.next = None
        if current.value < x:
            current.next = l1.head
            l1.head = current
        else:
            l1.tail.next = current
            l1.tail = current
        current = next

    if l1.tail.next is not None:
        l1.tail.next = None

partition(customLL, 30)
print(customLL)