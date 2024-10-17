def insert_string_in_middle(main_str, insert_str):
    middle_index = len(main_str) // 2
    return main_str[:middle_index] + insert_str + main_str[middle_index:]


print(insert_string_in_middle('abcdef', 'XYZ'))
print(insert_string_in_middle('123456', 'mid'))
