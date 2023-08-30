# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

def checkSameFrequency(list1, list2):
    def count(list):
        counted = {}
        for element in list:
            counted[element] = counted.get(element, 0) + 1
        return counted
    return count(list1) == count(list2)



print(checkSameFrequency(list1, list2))