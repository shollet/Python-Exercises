from LinkedList import *

def sumLists(l1, l2):
    temp1 = l1.head
    temp2 = l2.head
    carry = 0
    newLL = LinkedList()

    while temp1 or temp2:
        result = carry
        if temp1:
            result += temp1.value
            temp1 = temp1.next
        if temp2:
            result += temp2.value
            temp2 = temp2.next
        newLL.add(int(result % 10))
        carry = result / 10

    return newLL

l1 = LinkedList()
l1.add(7)
l1.add(1)
l1.add(6)
print(l1)
l2 = LinkedList()
l2.add(5)
l2.add(9)
l2.add(2)
print(l2)

print(sumLists(l1, l2))

    