# 🧩 Problem: Character Index Extractor
# -------------------------------------
# Write a function that takes:
#   - str_list: a list of strings
#   - int_list: a list of integers (positions)
# The function should return a string formed by concatenating
# the characters from each string in str_list at the positions
# specified by int_list.
#
# Example:
# str_list = ['hello', 'world', 'python']
# int_list = [1, 2, 4]
# Output: "e r h"


def check(str_list, int_list):
    
    s = ""
    
    for i, word in enumerate(str_list):
        pos = int_list[i]      #  position for current word
        s = s + word[pos]        # concatenate the character
        
    return s


#  Example test
if __name__ == "__main__":
    str_list = ['hello', 'world', 'python']
    int_list = [1, 2, 4]
    print(check(str_list, int_list))

    # Expected Output: ero
