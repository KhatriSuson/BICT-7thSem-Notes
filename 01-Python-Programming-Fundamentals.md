# **Unit 1: Python Programming Fundamentals**

## **1.1 Python Introduction**
- **What is Python?**
  - Python is a high-level, interpreted, and dynamically-typed programming language.
  - Known for its **simplicity**, **readability**, and **versatility**.
- **Key Features:**
  - **Interpreted:** Executes code directly without compilation.
  - **Cross-Platform:** Runs on Windows, macOS, Linux, etc.
  - **Extensive Libraries:** Built-in modules for tasks like web development, data analysis, and more.
- **Applications:**
  - Web Development
  - Data Science & Machine Learning
  - Automation
  - GUI Development

---

## **1.2 Data Types and Type Conversion**
- **Common Data Types:**
  - `int` (Integer): Whole numbers (e.g., `5`, `-10`).
  - `float` (Floating Point): Numbers with decimals (e.g., `3.14`, `-0.01`).
  - `str` (String): Text (e.g., `"Hello, World!"`).
  - `bool` (Boolean): `True` or `False`.
- **Type Conversion:**
  - Convert data between types using built-in functions:
    - `int("10")` → Converts a string to an integer.
    - `float("3.14")` → Converts a string to a float.
    - `str(42)` → Converts a number to a string.

---

## **1.3 Comments**
- **Purpose of Comments:**
  - Explain code for readability and maintainability.
  - Prevent specific code from executing.
- **Syntax:**
  - Single-line comment: `# This is a comment`
  - Multi-line comment:
    ```python
    """
    This is a 
    multi-line comment.
    ```
---

## **1.4 Variables, Constants, Operators, and Performing Calculations**
- **Variables:**
  - Used to store data in memory.
  - Example: `name = "Python"`
- **Constants:**
  - Represent fixed values; typically written in uppercase.
  - Example: `PI = 3.14`
- **Operators:**
  - Arithmetic: `+`, `-`, `*`, `/`, `%`
  - Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Logical: `and`, `or`, `not`
- **Performing Calculations:**
  - Use operators for math:
    ```python
    result = (10 + 5) * 3
    print(result)  # Output: 45
    ```

---

## **1.5 Reading Input from Keyboard**
- Use the `input()` function to take input as a string:
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}!")
