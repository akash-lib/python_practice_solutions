
"""
Problem:
Write a function that gets a string as input and prints all substrings of it,
sorted by increasing length.

Example:
Input:  "dog"
Output:
d
o
g
do
og
dog
"""

def print_sorted_substrings(string):
    # Generate all possible substrings
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    
    # Sort substrings by length (shortest first) – key step
    substrings.sort(key=len)
    
    # Print each sorted substring
    for substring in substrings:
        print(substring)

# Example usage
if __name__ == "__main__":
    print_sorted_substrings("dog")
