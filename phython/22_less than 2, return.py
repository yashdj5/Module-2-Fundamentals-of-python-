def first_and_last_two(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]


print(first_and_last_two('spring'))
print(first_and_last_two('abc'))
print(first_and_last_two('a'))
