# 🧩 Problem: Merge List of Dictionaries with Sorted Values
# ---------------------------------------------------------
# Write a function DictionaryList(dicts) that takes a list of dictionaries.
# In each dictionary, keys are integers and values are strings.
#
# The function should create and return a single dictionary that contains:
# - All keys from all dictionaries
# - Values as concatenation of all strings associated with that key across dictionaries
# - Sorted characters in the resulting strings
#
# Example:
# Input:
# dicts = [
#     {1:'iac', 2:'andrea',3:'mau', 5:'angelo'},
#     {2:'sterbini', 3:'mancini',1:'masi', 5:'spognardi'}
# ]
# Output:
# {1: 'aaciims', 2: 'aabdeeiinnrrst', 3: 'aaciimmnnu', 5: 'aadeggilnnooprs'}
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

def dicList (dicts):

    res =  {}

    # Merge dictionaries
    for i in dicts:
        for key, val in i.items():
            if key in res:
                res[key] += val  # concatenate strings if key already exists
            else:
                res[key] = val   # add new key-value pair

    # Sort characters in each value
    for key in res:
        res[key] = "".join(sorted(res[key]))

    return res


# Example Test
if __name__ == "__main__":
    dicts = [
        {1:'iac', 2:'andrea',3:'mau', 5:'angelo'},
        {2:'sterbini', 3:'mancini',1:'masi', 5:'spognardi'}
    ]
    print(dicList(dicts))

    # Expected Output:
    # {1: 'aaciims', 2: 'aabdeeiinnrrst', 3: 'aaciimmnnu', 5: 'aadeggilnnooprs'}
