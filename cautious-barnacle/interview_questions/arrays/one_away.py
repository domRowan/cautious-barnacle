# Cracking the coding interview 
# Question 1.5
# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false


# Solution 1
# Description: Create a map of characters for each of the strings that holds a count of the number of times the character appears. 
# Loop over one of the character maps. Check if the character appears in the other character map.
# If it does, check the count is the same.
# Either of these conditions can fail once, if more than one fail is seen, return false. Otherwise return true. 
# Complexity: O(n*m)
def get_character_map_from_string(input_string):
    character_map = {}

    for character in input_string:
        if character not in character_map:
            character_map[character] = 0
        character_map[character] += 1
    
    return character_map


def one_away(initial_string, comparison_string):
    initial_string_character_map = get_character_map_from_string(initial_string)
    comparison_string_character_map = get_character_map_from_string(comparison_string)

    missing_character_seen = False 
    for character, character_count in initial_string_character_map.items():
        if character not in comparison_string_character_map and missing_character_seen:
            return False
        
        if character not in comparison_string_character_map and not missing_character_seen:
            missing_character_seen = True
            continue

        if character in comparison_string_character_map:
            if comparison_string_character_map[character] != character_count and missing_character_seen:
                return False
            
            if comparison_string_character_map[character] != character_count and not missing_character_seen:
                missing_character_seen = True
                continue

    return True

input = "pale"
comparison = "bale"
print(one_away(input, comparison))

input = "pal"
comparison = "pale"
print(one_away(input, comparison))

input = "pale"
comparison = "bake"
print(one_away(input, comparison))

# Solution 2
# Description: 
# 
# Complexity: O(n)
def one_edit_replace(initial_character_list, comparison_character_list):
    different_character_seen = False
    for index in range(len(initial_character_list)):
        if initial_character_list[index] != comparison_character_list[index]:
            if different_character_seen:
                return False
            else:
                different_character_seen = True
    
    return True


# Loop over both lists, if the character at the index does not match, increment only one of the indexes
# This will then check the same character against the next character in the other string (if a character was missing)
# If this happens more than once return false, otherwise return true
def one_edit_insert(initial_character_list, comparison_character_list):
    index_1 = 0
    index_2 = 0

    while index_1 < len(initial_character_list) and index_2 < len(comparison_character_list):
        if initial_character_list[index_1] != comparison_character_list[index_2]:
            if index_1 != index_2:
                return False
            index_2 += 1
        else:
            index_1 += 1
            index_2 += 1
        return True

def one_away_separate_replace_and_insert_checks(initial_character_list, comparison_character_list):
    if len(initial_character_list) == len(comparison_character_list):
        one_edit_replace(initial_character_list, comparison_character_list)
    elif len(initial_character_list) + 1 == len(comparison_character_list):
        one_edit_insert(initial_character_list, comparison_character_list)
    elif len(initial_character_list) - 1 == len(comparison_character_list):
        one_edit_insert(comparison_character_list, initial_character_list)
    return False

input = "pale"
comparison = "bale"
print(one_away(list(input), list(comparison)))

input = "pal"
comparison = "pale"
print(one_away(list(input), list(comparison)))

input = "pale"
comparison = "bake"
print(one_away(list(input), list(comparison)))