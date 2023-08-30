def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
 
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")

""" def two_sum(nums, target): Define a function called two_sum that takes a list of integers nums and an integer target as input.

seen = {} Create an empty dictionary seen to store the numbers you have seen so far and their indices. Dictionary operations (adding and searching) have an average-case time complexity of O(1).

for i, num in enumerate(nums): Iterate through the input list nums using the enumerate function, which returns both the index i and the value num for each element in the list. The loop runs n times, where n is the length of the input list nums.

complement = target - num Calculate the complement of the current number num with respect to the target.

if complement in seen: Check if the complement is present in the seen dictionary. This operation has an average-case time complexity of O(1).

return [seen[complement], i] If the complement is found in the seen dictionary, return the index of the complement (seen[complement]) and the current index i.

seen[num] = i If the complement is not found, add the current number num and its index i to the seen dictionary. This operation has an average-case time complexity of O(1). """