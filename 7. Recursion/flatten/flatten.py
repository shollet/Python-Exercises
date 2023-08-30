# Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.

def flatten(arr):
    newArray = []
    for i in arr:
        if type(i) is list:
            newArray.extend(flatten(i))
        else:
            newArray.append(i)
    return newArray

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]