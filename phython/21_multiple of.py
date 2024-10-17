def reverse_if_multiple_of_four(s):
    if len(s) % 4 == 0:
        return s[::-1]  
    return s

# Example usage
print(reverse_if_multiple_of_four('abcd'))
print(reverse_if_multiple_of_four('hello'))
