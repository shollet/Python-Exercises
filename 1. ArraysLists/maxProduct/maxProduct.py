# Find the maximum product of two integers in an array where all elements are positive.

arr = [1, 7, 3, 4, 9, 5] 

def maxProduct(array):
    array.sort(reverse=True)
    return array[0]*array[1]


print(maxProduct(arr))