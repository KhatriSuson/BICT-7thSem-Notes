# **Unit 4: Object-Oriented Programming with Python**

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes. This unit explores the foundational concepts of OOP in Python, including classes, objects, inheritance, polymorphism, and data hiding.

---

## **4.1 Class and Object**

A class is a blueprint for creating objects. Objects are instances of classes, and they represent real-world entities or concepts.

### **Real-Life Example:**
Consider a **Car**. The car is the **class** that defines attributes like color, make, and model, and methods like start and stop. Each individual car, such as your red Toyota, is an **object** of the class **Car**. The **class** defines the general characteristics, while the **object** holds the actual values.

---

## **4.2 `__init__` Method**

The `__init__` method is a special method used for initializing newly created objects. It is automatically called when an object is instantiated.

### **Real-Life Example:**
Think of a **Book** being created in a library. When a new book is added to the library, details like title, author, and year of publication are provided at the time of creation. The `__init__` method is similar to this process, where we provide necessary details (attributes) for the object when it is created.

---

## **4.3 `self` Keyword**

The `self` keyword represents the instance of the class. It is used to access the attributes and methods of the current object.

### **Real-Life Example:**
Imagine a teacher teaching students. The **teacher** (self) can address each individual student (object) and provide their specific information. The `self` keyword ensures that each student’s information is specific to that particular student object, as opposed to sharing the same information across all objects.

---

## **4.4 Inheritance**

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability.

### **Real-Life Example:**
Think of an **Employee** class as a parent class. You can have different types of employees, such as **Manager**, **Engineer**, or **Clerk**. Instead of writing separate code for each type of employee, these child classes can inherit common attributes and behaviors (like name, salary, and work schedule) from the **Employee** class, and then add their specific behaviors (like special duties for a manager).

---

## **4.5 Polymorphism and Data Hiding**

### **Polymorphism:**
Polymorphism allows different classes to define methods with the same name, but with different behaviors depending on the object that is calling them.

### **Real-Life Example:**
Imagine a **Bird** class and a **Plane** class. Both classes can have a method called `fly()`. A bird's `fly()` method will describe how it flaps its wings to fly, while a plane's `fly()` method will describe how it uses engines to soar. Even though both use the same method name (`fly`), their implementations (behaviors) are different. This is polymorphism.

### **Data Hiding:**
Data hiding refers to restricting access to certain details of an object’s implementation, keeping them private, and only exposing necessary parts through public methods.

### **Real-Life Example:**
Think of a **BankAccount**. You may have private details like your account balance and PIN that should not be directly accessed by others. Instead, you provide methods like `deposit()` or `withdraw()` to modify or access the balance. These methods protect the sensitive data (balance) while still allowing authorized operations (deposits and withdrawals).

---

## **Summary**

- **Class and Object**: A class is a blueprint for creating objects, representing real-world entities like a **Car**, and objects are specific instances of that class, like your own **Toyota**.
- **`__init__` Method**: Used to initialize objects with specific attributes, like entering details when a **Book** is added to a library.
- **`self` Keyword**: Refers to the current instance of the class, ensuring each object maintains its unique attributes, just like a **teacher** addressing individual **students**.
- **Inheritance**: Allows child classes to inherit features from parent classes, like **Managers** and **Engineers** inheriting common attributes from an **Employee** class.
- **Polymorphism**: Enables different objects to use the same method name but perform different actions, like a **Bird** and **Plane** both having a `fly()` method with unique implementations.
- **Data Hiding**: Protects sensitive data in objects, like a **BankAccount** keeping your balance private but allowing access through methods like `deposit()` and `withdraw()`.

---

**Happy Coding!**
<hr>

## Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/sushan-khatri-959248259/)
<hr>