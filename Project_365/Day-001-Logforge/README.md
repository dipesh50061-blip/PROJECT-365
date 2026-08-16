# 🔍 LogForge

**Day 01 of Project 365 — 365 Days of Building**

LogForge is a lightweight Python-based log analysis tool that reads application logs and generates a structured summary of system activity.

It analyzes log entries, counts different log levels, extracts errors and warnings, and identifies the most frequently occurring error.

---

## 🎯 Project Goal

The goal of this project was to practice core Python programming by building a useful tool from scratch using **functions, file handling, loops, dictionaries, lists, and string manipulation**.

This project is intentionally built without external libraries.

---

## ✨ Features

* 📂 Read logs from a `.logs` file
* 📊 Count `INFO`, `WARNING`, and `ERROR` entries
* ❌ Extract all error logs
* ⚠️ Extract all warning logs
* 🔥 Find the most common error
* 📋 Generate a summarized log report
* 🛡️ Handle missing log files using exception handling

---

## 🧠 Concepts Practiced

* Python functions
* Function arguments and return values
* File handling with `open()`
* `try` / `except`
* Lists
* Dictionaries
* `for` loops
* Conditional statements
* String methods
* `.split()`
* `.splitlines()`
* `.join()`
* List slicing
* Dictionary `.items()` and `.values()`
* Frequency counting
* Finding maximum values
* Basic modular program design
* `if __name__ == "__main__"`

---

## 📁 Project Structure

```text
day-01-logforge/
│
├── main.py       # Main Python program
├── app.logs      # Sample application logs
└── README.md     # Project documentation
```

---

## ⚙️ How It Works

LogForge follows a simple processing pipeline:

```text
app.logs
   ↓
Read log file
   ↓
Parse log entries
   ↓
Count log levels
   ↓
Extract errors & warnings
   ↓
Analyze error frequency
   ↓
Generate report
```

---

## 📊 Example Output

```text
======= LOG REPORT =======

Total Logs: 30

INFO: 16
WARNING: 7
ERROR: 7

Most Common Error: Database connection failed

Total Errors: 7
Total Warnings: 7
```

---

## 🚀 How to Run

Make sure Python is installed on your system.

Clone the repository and navigate to the project directory:

```bash
cd day-01-logforge
```

Run the program:

```bash
python main.py
```

LogForge will read `app.logs` and generate the analysis report in the terminal.

---

## 🛠️ Tech Stack

**Language:** Python
**Libraries:** Python Standard Library only
**Interface:** Command Line / Terminal

---

## 📈 Future Improvements

This is the first version of LogForge. Possible future upgrades include:

* [ ] Support additional log levels
* [ ] Better log parsing and validation
* [ ] Export reports to JSON/CSV
* [ ] Analyze errors by date and time
* [ ] Add command-line arguments
* [ ] Add automated tests
* [ ] Refactor into an OOP architecture
* [ ] Add a graphical/web interface
* [ ] Add real-time log monitoring

---

## 📚 Project 365

**Day:** 01 / 365
**Project:** LogForge
**Status:** ✅ Completed
**Focus:** Python Fundamentals & File-Based Data Analysis

Project 365 is a long-term challenge to build something meaningful every day while progressively developing real-world software and AI engineering skills.

> **Build → Break → Debug → Improve → Repeat.**

---

## 👨‍💻 Author

**Depesh Kumar**

Built as part of **Project 365** — a journey toward becoming a production-ready AI engineer.
