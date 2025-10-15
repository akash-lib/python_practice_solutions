# 🧩 Problem: Count Repeating Characters in a List
# ------------------------------------------------------------
# Write a function that takes:
#   - a list of single-character strings
#   - an integer value k > 0
#
# The function should return the number of ***distinct character groups***
# that repeat k or more times consecutively.
#
# Example:
#   Input: ['a','a','z','b','b','b','a','a','a','z','c','c']
#   For k = 1 → returns 6  (a, z, b, a, z, c)
#   For k = 2 → returns 4  (a, b, a, c)
#   For k = 3 → returns 2  (b, a)
#   For k = 4 → returns 0
# ----------------------------------------------------------------------

def count_repeats(chars, k):


    count = 0        # number of groups
    curr_char = None # current character
    streak = 0       # consecutive count          

    # loop through each character in the list
    for char in chars:
        if char == curr_char:
            streak += 1
        else:
            
            if streak >=  k:
                count  += 1
                
            # reset for new character
            curr_char = char
            streak = 1

    # check the final streak at the end
    if streak >= k:
        count += 1

    return  count


#  Example Tests
if __name__ == "__main__":

    chars = ['a', 'a', 'z', 'b', 'b', 'b', 'a',  'a', 'a', 'z', 'c',  'c']
    
    print(count_repeats(chars, 1))  #  6
    print(count_repeats(chars, 2))  #  4
    print(count_repeats(chars, 3))  #  2
    print(count_repeats(chars, 4))  #  0
