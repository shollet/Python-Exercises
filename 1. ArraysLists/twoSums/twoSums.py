# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])


twoSums([2,7,11,15], 9)
twoSums([3,2,4], 6)
twoSums([3,3], 6)
twoSums([1,2,3,2,3,4,5,6], 6)