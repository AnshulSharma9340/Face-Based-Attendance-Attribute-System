
# 🤝 Contributing to AI Face Attendance System

Welcome to the **AI Face Attendance System** project!
We’re excited that you're interested in contributing.
This guide will help you understand how to report issues, propose improvements, and submit high-quality pull requests.

---

## 📌 Before You Start

Please ensure you:

* Read the **README.md**
* Understand the project structure
* Have Python (3.8+) installed
* Know the basics of Git & GitHub

---

## 🛠️ How to Contribute

### 1️⃣ Fork the Repository

Click the **Fork** button at the top-right of the repo.

### 2️⃣ Clone Your Fork

```bash
git clone https://github.com/<your-username>/Face-Based-Attendance-Attribute-System
cd Face-Based-Attendance-Attribute-System
```

### 3️⃣ Create a New Branch

Use meaningful names:

```bash
git checkout -b feature-improve-ui
```

or

```bash
git checkout -b fix-database-error
```

---

## 🐛 Reporting Issues

If you find a bug or want a feature added:

1. Go to **Issues** tab
2. Click **New Issue**
3. Choose the correct template:

   * 🐞 Bug Report
   * ✨ Feature Request
   * 📘 Documentation Improvement

Provide clear details:

* Expected behavior
* Actual behavior
* Steps to reproduce
* Screenshots (if applicable)

---

## 🧪 Running the Project Locally

1. Create a virtual environment
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:

   ```bash
   python app.py
   ```

---

## ✍️ Submitting Pull Requests (PRs)

### ✔️ Follow These Steps:

1. **Commit changes** with clear messages:

   ```bash
   git commit -m "Fix: Resolved face detection lag" 
   ```
2. **Push your branch**:

   ```bash
   git push origin feature-improve-ui
   ```
3. Open a **Pull Request** from GitHub:

   * Describe what you changed
   * Add screenshots if UI-related
   * Mention linked issue using:

     ```
     Closes #IssueNumber
     ```

---

## 📏 Code Guidelines

### 💡 Python

* Follow **PEP8** styling
* Keep functions modular & small
* Add comments for complex logic
* Use meaningful variable names

### 🎨 Frontend

* Follow clean HTML structure
* Keep CSS in `/static/css`
* Use separate JS files (no inline scripts)

### 🧠 Models & AI

* Avoid uploading heavy models (>25MB)
* If needed, provide a **Google Drive link**
* Add documentation for how the model works

---

## 🗃️ Project Structure Reference

```
AI-Face-Attendance-System/
├── app.py
├── models/
├── database/
├── static/
├── templates/
├── utils/
└── README.md
```

---

## ✔️ Contribution Types Accepted

| Type             | Description                                        |
| ---------------- | -------------------------------------------------- |
| 🐞 Bug Fix       | Fix detection errors, crashes, wrong predictions   |
| ✨ New Feature    | Add new models, UI enhancements, dashboard updates |
| 📝 Documentation | Improve README, tutorials, screenshots             |
| 🎨 UI/UX         | Better design, animations, responsiveness          |
| ⚡ Optimization   | Faster prediction, cleaner code                    |
| 📦 Database      | New schema, indexing, normalization                |

---

## 🙌 Contributor Recognition

All accepted contributors will be:

* Added to the **Contributors Section**
* Credited on the **project dashboard** (future update)

---

## 📜 Code of Conduct

Be respectful and kind.
Harassment, spam, or harmful behavior will not be tolerated.

---

## 💌 Need Help?

Open an issue or contact the maintainer:

**Anshul Sharma**
📧 *[anshulsharma7162@gmail.com](mailto:anshulsharma7162@gmail.com)*

---

## ⭐ Thank You!

Your contributions help improve this AI project for the entire community.
Let’s build something amazing together! 😊
