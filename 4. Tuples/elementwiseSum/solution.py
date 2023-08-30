def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result

# def tuple_elementwise_sum(t1, t2): - Define a function called "tuple_elementwise_sum" that takes two tuples "t1" and "t2" as arguments.

# if len(t1) != len(t2): - Check if the lengths of the input tuples are not equal.

# raise ValueError("Input tuples must have the same length.") - If the lengths of the tuples are not equal, raise a ValueError with a descriptive message.

# result = tuple(a + b for a, b in zip(t1, t2)) - Use the zip function to pair corresponding elements of the input tuples, then use a generator expression to compute the element-wise sum, and finally pass the generator expression to the tuple constructor to create a new tuple with the sums.

# return result - Return the resulting tuple containing the element-wise sums.