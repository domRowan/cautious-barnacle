# Cracking the coding interview 
# Question 1.4
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)


# Solution 1
# Description: Check the occurences of letters in the string. 
# If the word is a palindrome or permutation of a palindrome and the length of the letter map is even then ever letter should have an even count.
# If the word is a palindrome or permutation of a palindrome and the length of the letter map is odd then ever letter should have an even count except one.
# Complexity: O(n)
def palindrome_permutation(input_list):
    character_map = {}
    ignore_characters = set([" ", "!"])

    for character in input_list:
        if character in ignore_characters:
            continue
        if character not in character_map:
            character_map[character] = 0
        character_map[character] += 1

    individual_character_seen = False
    for character_count in character_map.values():
        if (character_count % 2) != 0 and individual_character_seen:
            return False
        if (character_count % 2) != 0 and not individual_character_seen:
            individual_character_seen = True
            continue
    
    return True


input = "taco cat"
print(palindrome_permutation(list(input)))

input = "tact coa"
print(palindrome_permutation(list(input)))

input = "anna"
print(palindrome_permutation(list(input)))

input = "this is not a palindrome permutation"
print(palindrome_permutation(list(input)))