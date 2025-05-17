✅ Task 1: Basic Mathematical Operations
math_operations.py
python
Copy
Edit
# Task 1: Basic Mathematical Operations

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Displaying results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
✅ Task 2: Personalized Greeting
personalized_greeting.py
python
Copy
Edit
# Task 2: Personalized Greeting

# Taking input from the user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenating names
full_name = first_name + " " + last_name

# Printing personalized greeting
print("Hello, " + full_name + "! Welcome to the python program.")
📝 README.md (Full Content)
markdown
Copy
Edit
# Python Tasks Repository

This repository contains two beginner-level Python scripts for practicing basic programming concepts such as user input, arithmetic operations, and string manipulation.

---

## ✅ Task 1: Basic Mathematical Operations

**📄 File**: `Assign_1_a.py`

### 🔹 Problem Statement:
Write a Python program that:
1. Takes two numbers as input from the user.
2. Performs the following mathematical operations:
   - Addition
   - Subtraction
   - Multiplication
   - Division
3. Displays the results of each operation on the screen.

### 🔹 Expected Output:
Enter first number: 10
Enter second number: 5
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

yaml
Copy
Edit

---

## ✅ Task 2: Personalized Greeting

**📄 File**: `Assign_1_b.py`

### 🔹 Problem Statement:
Write a Python program that:
1. Takes the user's first name and last name as input.
2. Concatenates them into a full name.
3. Prints a personalized greeting message using the full name.

### 🔹 Expected Output:
Enter your first name: John
Enter your last name: Doe
Hello, John Doe! Welcome to the python program.

yaml
Copy
Edit

---

## 📁 Repository Structure
python-tasks/
├── math_operations.py
├── personalized_greeting.py
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run

Use any Python IDE or terminal:
```bash
python math_operations.py
python personalized_greeting.py
vbnet
Copy
Edit

Let me know if you'd like me to zip the files or walk you through uploading them to GitHub.







