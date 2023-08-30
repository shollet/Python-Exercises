# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,2,3]

def containsDuplicate(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True
    return False

print(containsDuplicate(nums))