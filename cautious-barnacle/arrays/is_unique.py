# Cracking the coding interview 
# Question 1.1 
# Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# Solution 1
# Description: Use a set to keep track of unique letters.
# Compare length of set to length of string under test. 
# If lengths are not equal then the string under test does not contain unique characters.
# Could be improved by not using built in conversion and exiting as soon as a duplicate is found.
# Complexity: O(n)
def is_unqique(string_under_test):
    unique_characters = set(string_under_test)
    is_unique = len(unique_characters) is len(string_under_test)
    return is_unique

print(is_unqique("banana"))
print(is_unqique("cat"))

# Solution 2
# Description: Compare every letter to every other letter in the string
# Complexity: O(n^2)
def is_unique_no_additional_storage(string_under_test):
    for first_index in range(len(string_under_test)):
        second_index = first_index + 1
        while second_index < len(string_under_test):
            if string_under_test[second_index] is not None and string_under_test[second_index] == string_under_test[first_index]:
                return False
            second_index += 1

    return True

print(is_unique_no_additional_storage("banana"))
print(is_unique_no_additional_storage("cat"))

# Solution 3
# Description: Sort the string and compare neighboring letters.
# If these are the same then there are duplicate characters in the string. 
# WARNING some sorting algos may use additional space.
# Complexity: O(n(log(n)))
def is_unique_no_additional_storage_sorting(string_under_test):
    sorted_string_under_test = sorted(string_under_test)

    for first_index in range(len(sorted_string_under_test)):
        second_index = first_index + 1
        if second_index < len (string_under_test):
            if sorted_string_under_test[first_index] == sorted_string_under_test[second_index]:
                return False

    return True

print(is_unique_no_additional_storage_sorting("banana"))
print(is_unique_no_additional_storage_sorting("cat"))