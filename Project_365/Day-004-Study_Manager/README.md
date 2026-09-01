# 📚 Study Manager

A practical **Study Manager** designed to help users record, manage, search, and analyze their study sessions.

This project was built as part of my **Project 365 journey — Day 004**, where I consistently build projects to strengthen my programming, problem-solving, and software development skills.

🌐 **Live Website:** [**study-manageer.netlify.app**](https://study-manageer.netlify.app/)

---

## 🚀 Features

* ➕ Add new study sessions
* 📚 Store subject and topic
* ⏱️ Record study duration
* 📅 Store study date
* 📋 View all study sessions
* 🔍 Search sessions by subject or topic
* 📊 Calculate total study time
* 📈 Calculate average study duration
* 📚 View subject-wise study statistics
* ✏️ Edit existing study sessions
* 🗑️ Delete study sessions
* 💾 Persist study data
* 🆔 Automatically generate unique session IDs
* ✅ Input validation for duration and dates
* 📱 Responsive design for different screen sizes

---

## 🌐 Live Demo

Try the Study Manager online:

### 👉 [**study-manageer.netlify.app**](https://study-manageer.netlify.app/)

No installation is required — open the website and start tracking your study sessions.

---

## 🛠️ Technologies Used

### Original CLI Version

* **Python**
* **JSON**
* **datetime**
* **os**
* **File Handling**
* **Lists & Dictionaries**
* **Functions**
* **Exception Handling**

### Web Version

* **HTML**
* **CSS**
* **JavaScript**
* **Local Storage**

---

## 🖥️ Study Manager

The project started as a Python command-line application and was later transformed into a functional web-based Study Manager.

The web version provides a cleaner interface for managing study sessions while keeping the same core functionality of the original project.

---

## 📊 Dashboard

The Study Manager provides an overview of study activity, including:

* Total study sessions
* Total study time
* Average session duration
* Number of subjects
* Subject-wise study time
* Longest study session
* Most recent study session

These statistics update based on the user's actual study data.

---

## 📚 Study Sessions

Each study session contains:

```text
ID
Subject
Topic
Duration
Date
```

Users can:

* Add sessions
* Search sessions
* Edit sessions
* Delete sessions
* Review previous study activity

---

## 📝 Example Study Session

```text
Subject: Python
Topic: Functions
Duration: 90 minutes
Date: 2026-09-01
```

Example statistics:

```text
Study Statistics:

Total Study Sessions: 5
Total Duration: 420 minutes
Average Duration: 84 minutes per session

Subject-wise Duration:

Python            → 180 minutes
SQL               → 120 minutes
Machine Learning  → 120 minutes
```

---

## 💾 Data Persistence

The web version uses browser storage to preserve study-session data.

This means your study records remain available after:

* Refreshing the page
* Closing the browser
* Reopening the website

The project also maintains a simple session-data structure:

```json
{
    "id": 1,
    "subject": "Python",
    "topic": "Functions",
    "duration": 90,
    "date": "2026-09-01"
}
```

---

## 🔄 CRUD Operations

Study Manager supports the complete CRUD workflow:

| Operation  | Feature                |
| ---------- | ---------------------- |
| **Create** | Add Study Session      |
| **Read**   | View & Search Sessions |
| **Update** | Edit Study Session     |
| **Delete** | Delete Study Session   |

---

## 🧠 Concepts Practiced

This project helped me practice:

* Python programming
* JavaScript
* HTML & CSS
* Functions
* Lists & Dictionaries
* Loops
* Conditional statements
* List comprehensions
* File handling
* JSON
* Local storage
* Exception handling
* Input validation
* Date validation
* CRUD operations
* Data persistence
* Responsive web design
* UI/UX development

---

## 🎯 Project Goal

The goal of this project was to build a practical tool while improving my understanding of **programming fundamentals, data management, CRUD operations, persistence, and web development**.

This project is part of my ongoing **Project 365** challenge — building consistently, learning through projects, and progressing toward my long-term goal of becoming an **AI Engineer**.

---

## 📈 Project 365 Progress

### Week 01

* ✅ Day 001 — LogForge
* ✅ Day 002 — Task Manager
* ✅ Day 003 — Expense Tracker
* 🚀 Day 004 — Study Manager

### Day 004 Status

**✅ Completed**

---

## 👨‍💻 Author

**Depesh Kumar**

Building. Learning. Improving.

**One project at a time. 🚀**

---

⭐ If you find this project useful, consider giving the repository a star!

🌐 **Live Demo:** [**study-manageer.netlify.app**](https://study-manageer.netlify.app/)
