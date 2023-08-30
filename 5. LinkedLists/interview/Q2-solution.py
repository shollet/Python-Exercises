from LinkedList import *

def returnKthToLast(l1, k):
    pointer1 = l1.head
    pointer2 = l1.head

    for _ in range(k):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1
    

print(returnKthToLast(customLL, 5))
