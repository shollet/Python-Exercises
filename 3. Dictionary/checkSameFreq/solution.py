def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)

# Define an inner function count_elements(lst) that counts the frequency of elements in a list lst. The function creates an empty dictionary counter, iterates through the list, and increments the count for each element using the get() method. The get() method takes O(1) average time complexity. The function returns the counter dictionary. The time complexity of count_elements() is O(n), where n is the number of elements in the input list lst. The space complexity is also O(n), as the dictionary counter has as many keys as there are distinct elements in the list.

# Call the count_elements() function on both input lists list1 and list2. This operation has a time complexity of O(n1 + n2), where n1 and n2 are the lengths of list1 and list2, respectively. The space complexity is O(m1 + m2), where m1 and m2 are the numbers of distinct elements in list1 and list2, respectively.

# Compare the resulting dictionaries using the == operator. This operation has a time complexity of O(min(m1, m2)), as it compares the keys and values of both dictionaries.

# Return the result of the comparison (True if the dictionaries are equal, False otherwise).