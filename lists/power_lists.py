# 🧩 Problem: Generate Power Lists
# ------------------------------------------------------------
# Write a function that takes two integers n and p,
# and returns a list containing n sublists.
# Each sublist contains the powers of that number from 0 to  p.
#
# Example :
# Input:  n = 3 ,  p = 4
# Output: [[1, 1, 1, 1, 1], [1, 2, 4, 8, 16], [1, 3, 9, 27, 81] ]
# ------------------------------------------------------------

# Solution :
#-----------

# Function to generate a list of powers for a single number

def powers (n, p):
    p_list = []
    for i in range(0, p + 1):
    
        p_list.append(n ** i)  # Add n raised to the power i
        
        
    return p_list


# Function to generate a list of all power lists
def power_lists(n,  p):

    final_list = []
    for i in range(1, n + 1):
    
        final_list.append(powers(i, p))  # Add power list for each number
        
    return final_list


# Example test

if __name__ == "__main__":
    output = power_lists(3, 4)
    print(output)


#  Expected Output:
# [[1, 1, 1, 1, 1],
#  [1, 2, 4, 8, 16],
#  [1, 3, 9, 27, 81]]
