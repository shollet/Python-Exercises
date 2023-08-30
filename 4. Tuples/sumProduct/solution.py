def sum_product(t):
    sum_result = 0
    product_result = 1
 
    for num in t:
        sum_result += num
        product_result *= num
 
    return sum_result, product_result
 
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

# def sum_product(t): - Define a function called "sum_product" that takes a tuple "t" as an argument.

# sum_result = 0 - Initialize a variable "sum_result" to store the sum of the elements in the tuple. Set its initial value to 0.

# product_result = 1 - Initialize a variable "product_result" to store the product of the elements in the tuple. Set its initial value to 1.

# for num in t: - Start a for loop that iterates through each element "num" in the tuple "t".

# sum_result += num - Add the current element "num" to the "sum_result".

# product_result *= num - Multiply the current element "num" with the "product_result".

# return sum_result, product_result - After the loop is done, return a tuple containing the "sum_result" and "product_result".