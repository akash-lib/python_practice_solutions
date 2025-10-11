# 🐍 Python Practice Solutions

Welcome to my collection of **Python problem-solving exercises** — from beginner to advanced!  
Each program includes a **clear problem statement**, **clean code**, and **example output** to help learners understand Python concepts effectively.

---

## 📚 Topics Covered

- 🧠 Basics  
- 🔁 Loops  
- 🔤 Strings  
- 🧮 Lists  
- 🔂 Recursion  

---

## 🧩 Example Problem

**File:** `strings/print_sorted_substrings.py`

### Problem:
Write a function that gets a string as input and prints all its substrings, sorted by increasing length.

### Solution:
```python
def print_sorted_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    substrings.sort(key=len)
    for substring in substrings:
        print(substring)


# Example test
if __name__ == "__main__":
    print_sorted_substrings("dog")
```

### Example Output:
```
d
o
g
do
og
dog
```

---

## 💡 About

This repository is part of my **personal journey to master Python programming** through consistent daily practice and problem-solving.  
It includes real exercises covering everything from basic syntax to advanced algorithmic logic — all written and organized neatly for learners.

If you’re learning Python like me, feel free to **clone**, **fork**, or **contribute** to this repository!  
Let’s grow together through code. 🚀  

---

## 👨‍💻 Author

**Najmul Hossain Akash**  
🎓 Department of Computer Science & Engineering (CSE)  
🏫 University of Scholars  
📧 Email: [nhs46430@gmail.com](mailto:nhs46430@gmail.com)  
🌐 GitHub: [akash-lib](https://github.com/akash-lib)

---

⭐ **If you like this repository, don’t forget to give it a star!** ⭐
