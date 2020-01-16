# Cracking the coding interview 
# Question 1.3
# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
# (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)



# Solution 1
# Description: Split string into an array of words. 
# Iterate over the array of words to create the output string. 
# If the index is greater than 0 (after the first word) insert the space delimiter
# Complexity: O(n)

def urlify(input, input_length):
    space_delimiter = "%20"
    words = input.split()
    urlified_string = ""

    for index in range(len(words)):
        if index > 0:
            urlified_string += space_delimiter
        urlified_string += words[index]
    
    return urlified_string

input = "Well I hope this works"
print(urlify(input, len(input)))

# Solution 2
# Description: Count the number of spaces in the input list. 
# Increase the length of the list by 2 * the number of spaces 
# (this means we can add 3 extra characters, one for the existing space and 2 extra).
# Go through the list with 2 pointers, one starting at the end of the list, one starting at the end of the original text. 
# If the character is not " " then just copy the character to the end of the list
# If the character is a " " then add 0, 2, % to replace the space with %20
# Complexity: O(n)

def urlify_array_of_characters(input_list, input_length):
    space_count = 0
    index = 0
    for i in range(input_length):
        if input_list[i] == ' ':
            space_count += 1
    
    index = input_length + space_count * 2
    difference_in_length = index - input_length

    for i in range(difference_in_length):
        input_list.append("!")

    for i in reversed(range(input_length)):
        if input_list[i] == ' ':
            input_list[index - 1] = '0'
            input_list[index - 2] = '2'
            input_list[index - 3] = '%'
            index = index - 3
        else:
            input_list[index - 1] = input_list[i]
            index -= 1

    return input_list

input_list = list(input)
print(urlify_array_of_characters(input_list, len(input_list)))