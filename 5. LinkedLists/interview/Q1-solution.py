# Write a function to remove duplicates from an unsorted linked list. Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5

from LinkedList import *

def remove_duplicates(ll):
    if ll.head is None:
        return
 
    current = ll.head
    prev = None
 
    while current:
        temp = current
        while temp.next:
            if temp.next.value == current.value:
                temp.next = temp.next.next
            else:
                temp = temp.next
        prev = current
        current = current.next
 
    ll.tail = prev  
    return ll

print(remove_duplicates(customLL))


