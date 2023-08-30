def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Define a function count_word_frequency(words) that takes a list of words as its input.

# Initialize an empty dictionary word_count to store the frequency of each word in the list.

# Iterate through the list of words using a for loop.

# For each word, use the get() method to retrieve the current count of the word in the word_count dictionary. If the word is not yet present in the dictionary, get() returns the default value (0). Then, increment the count by 1 and update the dictionary.

# After iterating through all the words, return the word_count dictionary containing the word frequencies.