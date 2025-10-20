# 🧩 Problem: Binary to Integer List
# ----------------------------------
# Write a function binary_to_int_list(str_list) that takes a list of binary
# strings and returns a list of integers, where each integer is the decimal
# equivalent of the corresponding binary string.

def binary_to_int_list(str_list):
    
    result = []
    for string in str_list:
        total = 0
        # Reverse the string to process from least significant bit
        for pos, char in enumerate(string[::-1]):
            if char in ('0', '1'):             # valid binary digits
                total += int(char) * (2 ** pos)
            else:
               
                total = None
                break
        result.append(total)
    return result


#  Example Test
if __name__ == "__main__":
    str_list = ['101', '210', '421', '10001']
    output = binary_to_int_list(str_list)
    print(output)

    # Expected Output:
    # [5, None, None, 17]
