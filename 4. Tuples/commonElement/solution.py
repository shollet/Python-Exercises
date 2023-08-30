def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

# def common_elements(tuple1, tuple2): - Define a function called "common_elements" that takes two tuples "tuple1" and "tuple2" as arguments.

# return tuple(set(tuple1) & set(tuple2)) - Convert both input tuples into sets using the set() constructor, then use the set intersection operator & to find the common elements between the two sets. Convert the resulting set of common elements back to a tuple and return it.