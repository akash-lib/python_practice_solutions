# Problem:
# You are given a list of integers with potential duplicates.
# Write a function remove_duplicates3(a_list) that removes all duplicate
# elements from the list by modifying the list in place
# (without using extra memory such as a set or another list).
# The order of the elements should be preserved.

def remove_duplicates(a_list):
    
    i = 0
    while i < len(a_list):
        
        if a_list[i] in a_list[:i]:
            del a_list[i]
            
        else:
            i += 1
            
    return a_list


# Example
if __name__ == "__main__":
    
    a_list = [1, 2, 3, 2, 4, 5, 1, 6]
    remove_duplicates(a_list)
    print(a_list)  # Output: [3,2,4,5,1,6]
