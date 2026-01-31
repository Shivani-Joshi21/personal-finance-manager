# Personal Finance Manager (Standard Version)

## 📌 Project Overview

The **Personal Finance Manager** is a Python-based command-line application that helps users track daily expenses, store data persistently, and generate useful financial reports. This project demonstrates core Python concepts such as Object-Oriented Programming (OOP), file handling using CSV, modular code design, data validation, and error handling.

This project is submitted as the **Standard Version**, which includes reporting and analysis features.

---

## 🎯 Project Objectives

* Track personal expenses with amount, category, date, and description
* Store and retrieve expense data using CSV files
* Generate category-wise summaries
* Generate monthly expense reports (total and average)
* Practice clean, modular, and well-documented Python code

---

## 🛠️ Features

* Add new expenses through a menu-driven CLI
* View all recorded expenses
* Category-wise expense summary
* Monthly report (total & average)
* Input validation and error handling
* CSV-based data persistence
* Modular project structure

---

## 📂 Project Structure

```
personal-finance-manager/
│── README.md                # Project documentation
│── main.py                  # Application entry point
│── requirements.txt         # Python dependencies
│
├── src/
│   ├── expense.py           # Expense class (OOP)
│   ├── file_manager.py      # CSV read/write operations
│   ├── reports.py           # Reporting & analysis functions
│   └── utils.py             # Validation and utility functions
│
├── data/
│   └── expenses.csv         # Stored expense data
│
├── screenshots/             # Application screenshots
├── docs/                    # User documentation
└── tests/                   # Unit tests (optional)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Python

* Install **Python 3.10 or above**
* Ensure Python is added to PATH

### 2️⃣ Clone or Download the Project

```bash
git clone <repository-url>
cd personal-finance-manager
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

*(Only standard Python libraries are used.)*

### 4️⃣ Run the Application

```bash
python main.py
```

---

## 🖥️ How to Use

### Main Menu Options

1. Add New Expense
2. View All Expenses
3. Category-wise Summary
4. Monthly Report
5. Exit

### Sample Input

```
Amount: 1500
Category: Food
Date (YYYY-MM-DD): 2024-01-15
Description: Grocery shopping
```

---

## 📊 Reports & Analysis

* **Category Summary:** Displays total spending per category
* **Monthly Report:** Calculates total and average expenses for a selected month

---

## 🧠 Technical Details

### Concepts Used

* Object-Oriented Programming (Classes & Objects)
* File handling using CSV
* Error handling with try-except
* Data validation
* Modular programming

### Data Structures

* Lists for storing expenses
* Dictionaries for category summaries

---

## 🧪 Testing & Validation

* Manual testing of all menu options
* Validation for incorrect amount and date inputs
* Verified CSV file persistence

---

## 📸 Screenshots

Screenshots demonstrating:

* Application startup
* Adding an expense
* Viewing expenses
* Category-wise summary
* Monthly report

(All screenshots are available in the `screenshots/` folder.)

---

## 📦 Deliverables Checklist

* [x] Working Python application
* [x] Complete source code with comments
* [x] User documentation (README.md)
* [x] Sample data and usage examples
* [x] Error handling implementation
* [x] GitHub-ready project structure

---

## 🚀 Future Enhancements

* Budget planning
* Expense charts and visualizations
* Data export (Excel / PDF)
* Search, edit, and delete expenses



## ✅ Conclusion

This project fulfills all requirements for the **Standard Version Personal Finance Manager** and demonstrates strong Python fundamentals suitable for academic submission and portfolio use.
