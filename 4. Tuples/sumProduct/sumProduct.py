# Write a function that calculates the sum and product of all elements in a tuple of numbers.


input_tuple = (1, 2, 3, 4)


def sumProduct(tuple):
    product = 1
    for i in tuple:
        product *= i
    return (sum(tuple), product)


sum_result, product_result = sumProduct(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24