# Write a function to remove the duplicate numbers on given integer array/list.

def removeDuplicates(array):
    newArray = []
    for i in array:
        if i not in newArray:
            newArray.append(i)
    return newArray
        

    


print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))