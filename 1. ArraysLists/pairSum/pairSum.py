# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

def pairSum(array, value):
    newArray = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == value:
                newArray.append(str(array[i]) + "+" + str(array[j]))
    return newArray


print(pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))