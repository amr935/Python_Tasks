# 📂 Python File Handling Tasks – Assignment 4

Welcome to **Assignment 4** of Python Programming!  
This repository contains two Python programs that demonstrate basic file handling operations such as **reading**, **writing**, **appending**, and **error handling**.

---

## 🔧 Task 1: Read a File and Handle Errors

📁 **Filename:** `assign_4_a.py`

### ✅ Objective:
- Open and read a text file named `sample.txt`.
- Print its contents **line by line**.
- Gracefully handle the error if the file is **not found**.

### 🧠 Logic:
- Uses `try-except` block to catch `FileNotFoundError`.
- Reads the file using a `with open(...)` context manager for clean and safe file access.

### 📜 Code:

```python
# assign_4_a.py

file_2=open('sample.txt','r')
reading_file=file_2.read()
print(reading_file)
file_2.close()
#Let sample1.txe file does not exit, for this the error handling would be like:
try:
    file_2 = open('sample1.txt', 'r')
    reading_file = file_2.read()
    print(reading_file)
    file_2.close()
except FileNotFoundError:
    print("Error:The file 'sample1.txt' was not found")

```

### 📌 Example Output:
If the file exists:
```
This is a sample text file.
It contains multiple lines.
```

If the file does not exist:
```
Error: The file 'sample.txt' was not found
```

---

## 🔧 Task 2: Write and Append Data to a File

📁 **Filename:** `assign_4_b.py`

### ✅ Objective:
1. Take user input and write it to a file named `output.txt`.
2. Take additional input and append it to the same file.
3. Finally, read and display the complete content of the file.

### 🧠 Logic:
- Uses `input()` function to capture user input.
- Uses write mode (`'w'`) to write data and append mode (`'a'`) to add more content.
- Reads the file again to show the final output.

### 📜 Code:

```python
# assign_4_b.py

a=input("Enter text to write to the file:")

file_3=open('output.txt','w')
writing_file=file_3.write(a)
file_3.close()

print('Data successfully written to output.txt.')

b=input("Enter additional text to append:")

file_3=open('output.txt','a')
appending_file=file_3.write('\n'+b)
file_3.close()

print('Data successfully appended.')


print('Final content of output.txt:')

file_3=open('output.txt','r')
appending_file=file_3.read()
print(appending_file)
file_3.close()
```

### 📌 Example Output:
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in python.
Data successfully appended.
Final content of output.txt:
Hello, Python!
Learning file handling in python.
```

---

## 🚀 How to Run

Make sure you have Python installed (version 3.x). Run the files using:

```bash
python assign_4_a.py
python assign_4_b.py
```

---

## 📄 Files in the Repository

| File Name       | Description                                |
|----------------|--------------------------------------------|
| `assign_4_a.py` | Handles reading from a file with error checks |
| `assign_4_b.py` | Demonstrates writing, appending, and reading a file |

---

## 📚 Topics Covered

- File I/O in Python
- Exception Handling (`try-except`)
- User Input
- File Reading/Writing/Appending

---

## 🌟 Author

**amr935**

---

## 📬 Feedback

If you find this helpful or have any suggestions, feel free to open an issue or pull request. Contributions are welcome!
