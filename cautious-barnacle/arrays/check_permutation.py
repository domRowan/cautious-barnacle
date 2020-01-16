# Cracking the coding interview 
# Question 1.2
# Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.


# Solution 1
# Description: Sort both strings and check if the values of the sorted strings are equal
# Complexity: O(n(log(n)))
def check_permutation(original_string, potential_permutation):
    sorted_original_string = sorted(original_string)
    sorted_potential_permutation = sorted(potential_permutation)

    return sorted_original_string == sorted_potential_permutation

print(check_permutation("fader", "redaf"))
print(check_permutation("foo", "bar"))

# Solution 2
# Description: Create a set of the characters in the first string
# Check if all the values are the present in the second string.
# Early exit on length equality to avoid one string being longer than the other. 
# Complexity: O(n)
def check_permutation_with_set(original_string, potential_permutation):
    if len(original_string) != len(potential_permutation):
        # Can't be a permutation if the length is not the same
        return False

    original_string_characters = set(original_string)

    for character in potential_permutation:
        if character not in original_string_characters:
            return False
    return True

print(check_permutation_with_set("fader", "redaf"))
print(check_permutation_with_set("foo", "bar"))
