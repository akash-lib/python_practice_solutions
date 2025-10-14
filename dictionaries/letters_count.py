# 🧩 Problem: Count Letters in Text
# ------------------------------------------------------------
# Write a function LettersCount(text) that takes a string containing any text,
# and returns a dictionary where:
#   - Every key is a letter (A–Z or a–z)
#   - The value is the number of times that letter appears in the text
#
# Notes:
#   - Spaces, numbers, and symbols are ignored
#   - Uppercase and lowercase are counted separately
#
# Example:
# Input:  "Lorem ipsum! dolor, sit amet 10?"
# Output: {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, 'i': 2, 'p': 1,
#          's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}
# ------------------------------------------------------------

def Check_Letters_Count (text):
    # initialize an empty dictionary
    letter_count = {}

    # loop through every character
    for char in text:
        # check if the character is an alphabet letter
        
        if  char.isalpha():
            # if the letter is already in dictionary, increment its count
            if char in  letter_count:
                letter_count[char] += 1
                
            # otherwise, add it with count 1
            else :
                letter_count[char] = 1
    
    return letter_count


# Example test
if __name__ == "__main__":
    text = "Lorem ipsum! dolor, sit amet 10?"
    
    print(Check_Letters_Count(text))


# Expected Output:
# {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, 'i': 2, 'p': 1,
#  's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}
