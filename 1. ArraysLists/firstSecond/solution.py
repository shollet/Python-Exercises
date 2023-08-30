def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')
 
    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num
 
    return max1, max2
 
my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)

# def first_second(my_list):

# Define a function called first_second that takes a list called my_list as an argument.

# max1, max2 = float('-inf'), float('-inf')

# Initialize two variables max1 and max2 to store the first and second best scores. Set their initial values to negative infinity.

# for num in my_list:

# Start a for loop that iterates through each element in my_list.

# if num > max1:

# Check if the current element is greater than max1.

# max2 = max1

# If the current element is greater than max1, update max2 to the current value of max1.

# max1 = num

# Set max1 to the current element, as it is now the highest value found so far.

# elif num > max2 and num != max1:

# If the current element is greater than max2 but not equal to max1, update max2.

# max2 = num

# Set max2 to the current element, as it is now the second-highest value found so far.

# return max1, max2

# After the for loop is done, return the first and second best scores as a tuple.