# BMI Calculator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/Oasis%20Infobyte-Internship-orange?style=for-the-badge)

> A clean and professional command-line based **Body Mass Index (BMI) Calculator** developed as part of the Oasis Infobyte Python Programming Internship.

---

## 📌 Project Overview

This project is a simple yet well-structured Python application that calculates a user’s Body Mass Index (BMI) based on their weight and height.  

The program not only computes the BMI value but also classifies the result into standard health categories and includes proper input validation to ensure reliability and user-friendliness.

**Key Highlights:**
- Accurate BMI calculation using the standard formula
- Clear health category classification
- Robust input validation
- Clean and readable code structure
- Professional documentation

---

## 🗂️ Project Structure

Task1_BMI_Calculator/
│
├── bmi_calculator.py      # Main application file
└── README.md              # Project documentation


---

## 🛠️ Technologies Used

| Technology           | Purpose                                   |
|----------------------|-------------------------------------------|
| Python 3             | Core programming language                 |
| Built-in functions   | Input handling, calculations, and logic   |

---

## ✨ Features

- Accepts weight (in kilograms) and height (in meters)
- Calculates BMI using the formula:  
  **BMI = weight / (height²)**
- Classifies the result into the following categories:
  
    Category      BMI Range       Indicator 
  - Underweight   (< 18.5)          ❌     
  - Normal        (18.5 – 24.9)     ✅     
  - Overweight    (25 – 29.9)       ⚠️     
  - Obese         (≥ 30)            🚨     
    
- Displays BMI value rounded to 2 decimal places
- Includes strong input validation (rejects non-numeric and negative values)
- User-friendly command-line interface

---

## 🚀 How to Run the Project

1. Ensure **Python 3** is installed on your system.
2. Open a terminal or command prompt in the project directory.
3. Execute the following command:

```bash
python bmi_calculator.py
```
##  Usage Example

=============== BMI CALCULATOR ===============

Enter your weight ⚖️  in kilograms : 70
Enter your height 📏 in meters    : 1.75

Great!💪 You are in a healthy range.

------------------- RESULTS ------------------
Your BMI is : 22.86.
Your are classified as : Normal weight ✅ .
----------------------------------------------
