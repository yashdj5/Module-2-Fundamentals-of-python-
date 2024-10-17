def longest_word_length(word_list):
    if not word_list:
        return 0
    return len(max(word_list, key=len))

# Example usage
words = ['apple', 'banana', 'cherry', 'blueberry']
print(longest_word_length(words))
