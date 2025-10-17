# 🧩 Problem: String Lengths Dictionary
# -------------------------------------
# Write a function that takes a list of strings and returns a dictionary where:
#  - Keys are the strings from the list
#  - Values are the lengths of those strings
#
# Example:
# Input:  ['bar', 'cat', 'apple']
# Output: {'bar': 3, 'cat': 3, 'apple': 5}


def string_lengths(string_list):
    
    length_dict = {}
    
    for string in string_list:
        length_dict[string] = len(string)         # store length of each string
        
    return length_dict


#  Example test
if __name__ == "__main__":

    string_list = ['bar', 'cat', 'apple']
    result = string_lengths(string_list)
    print(result)

    # ✅ Expected Output:
    # {'bar': 3, 'cat': 3, 'apple': 5}
