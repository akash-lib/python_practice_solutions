# 🧩 Problem: Characters in Strings
# ------------------------------------------------------------
# Write a function chars_in_strings(s1, s2) that takes two strings s1 and s2 as input and returns:
# 1️⃣ A set of characters that appear in both s1 and s2.
# 2️⃣ A set of characters that appear in one string but not both.
# 3️⃣ A set of characters that do not appear in either string (considering the English alphabet).
# ------------------------------------------------------------

def chars_in_strings(s1, s2):
    # Convert each string into a set of unique characters
    set1 = set(s1)
    set2 = set(s2)

    # Define the complete lowercase English alphabet
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    # Print characters common to both strings
    print('Characters in both:', set1 & set2)

    # Print characters that appear in one string but not both
    print('Characters in one but not both:', set1 ^ set2)

    # Print characters that appear in neither of the two strings
    print('Characters in none of them:', alphabet - (set1 | set2))


# 🧪 Example test case
if __name__ == "__main__":
    chars_in_strings('abracadabra', 'bars')


# 💬 Expected Output:
#Characters in both: {'r', 'b', 'a'}
#Characters in one but not both: {'s', 'c', 'd'}
#Characters in none of them: {'e', 'k', 'y', 'n', 'j', 'f', 'x', 'l', 'i', 'o', 'g', 'u', 'w', 'v', 'h', 'q', 't', 'z', 'm', 'p'}
