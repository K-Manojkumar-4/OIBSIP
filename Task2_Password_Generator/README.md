# Random Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/Oasis%20Infobyte-Internship-orange?style=for-the-badge)

> A secure and customizable **Random Password Generator** built in Python as part of the Oasis Infobyte Python Programming Internship.

---

## 📌 Project Overview

This project is a command-line based password generator that allows users to create strong and random passwords based on their preferred criteria.  

Users can define the password length and select which character types to include (uppercase, lowercase, digits, and symbols). The program ensures that at least two character types are selected and generates a secure password accordingly.

**Key Highlights:**
- Customizable password length (minimum 8 characters)
- Multiple character type options
- Enforced security rules
- Clean and user-friendly interface
- Option to generate multiple passwords in one session

---

## 🗂️ Project Structure

Task2_Password_Generator/
│
├── password_generator.py   # Main application file
└── README.md               # Project documentation

---

## 🛠️ Technologies Used

| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| Python 3       | Core programming language                    |
| `random`       | For generating random characters             |
| `string`       | Provides predefined character sets           |

---

## ✨ Features

- User can specify desired password length (minimum 8 characters enforced)
- Option to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (!@#$%^&* etc.)
- At least two character types must be selected
- Generates a random password matching all selected criteria
- Input validation for invalid length or insufficient character types
- Option to generate another password without restarting the program

---

## 🚀 How to Run the Project

1. Ensure **Python 3** is installed on your system.
2. Open a terminal or command prompt in the project directory.
3. Execute the following command:

```bash
python password_generator.py
```
## Screenshots Outputs

![BMI Output](screenshots/)
