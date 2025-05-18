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

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
📌 Example Output:
If the file exists:
This is a sample text file.
It contains multiple lines.


If the file does not exist:
Error: The file 'sample.txt' was not found


'''Task 2 Explanation

## 🔧 Task 2: Write and Append Data to a File
📁 Filename: assign_4_b.py

### ✅ Objective:
1.Take user input and write it to a file named output.txt.

2.Take additional input and append it to the same file.

3.Finally, read and display the complete content of the file.

###🧠 Logic:
1.Uses input() function to capture user input.

2.Uses write mode ('w') to write data and append mode ('a') to add more content.

3.Reads the file again to show the final output.
'''
###📜 Code:
# assign_4_b.py

# Step 1: Write to the file
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append to the file
append_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display the content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

'''
📌 Example Output:

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in python.
Data successfully appended.
Final content of output.txt:
Hello, Python!
Learning file handling in python.


---

## 🚀 How to Run

Make sure you have Python installed (version 3.x). Run the files using:

```bash
python assign_4_a.py
python assign_4_b.py


📚 Topics Covered
File I/O in Python

Exception Handling (try-except)

User Input

File Reading/Writing/Appending

🌟 Author
   amr935

📬 Feedback
If you find this helpful or have any suggestions, feel free to open an issue or pull request. Contributions are welcome!
Let me know if you want to include a demo image, badges, or link this to your actual GitHub repo.

'''

