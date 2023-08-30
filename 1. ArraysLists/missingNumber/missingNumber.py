# Write a function to find the missing number in a given integer array of 1 to 100.

def missing_number(arr, n):
    for number in range(1,n):
        if number not in arr:
            return number
        
print(missing_number([1, 2, 3, 4, 6], 6))