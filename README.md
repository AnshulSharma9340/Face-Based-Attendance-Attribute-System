<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<div align="center">
    <img src="./static/images/face_scan_background.png" style="width: 220px; height: 220px; border-radius: 50%;" alt="AI Face Attendance System Logo" />
</div>

<h1 align="center">🧠 AI FACE ATTENDANCE SYSTEM 🧑‍ attendance</h1>

<div align="center" style="margin: 10px 0 24px;">
  <a href="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/issues">🐛 Report Bug</a>
  •
  <a href="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/issues">💡 Request Feature</a>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="overview">🔍 Overview</h2>

> The **AI Face Attendance System** is an advanced, real-time solution built with **Python** and **Deep Learning** models. It goes beyond simple identification by integrating **Age, Gender, and Emotion Detection** with automated attendance marking. The system features an interactive web interface powered by **Flask** and a **SQLite** database for robust data management.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=007ACC&width=535&lines=Real-Time+Attendance+Powered+by+AI!%F0%9F%A7%A0;Automate+Your+Routines;Integrate+Face%2C+Age%2C+Gender%2C+and+Emotion%F0%9F%91%8D;Happy+Coding%20with+Deep+Learning%E2%9C%A8!" alt="Thanks Banner Typing SVG" />
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="project-insights">📊 Project Insights</h2>

<table align="center">
  <thead align="center">
    <tr>
      <td><b>🌟 Stars</b></td>
      <td><b>🍴 Forks</b></td>
      <td><b>📚 Main Language</b></td>
      <td><b>📄 License</b></td>
      <td><b>🧑‍💻 Activity</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img alt="Stars" src="https://img.shields.io/github/stars/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=flat&logo=github"/></td>
      <td><img alt="Forks" src="https://img.shields.io/github/forks/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=flat&logo=github"/></td>
      <td><img alt="Python" src="https://img.shields.io/github/languages/top/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=flat&color=blue&logo=python"></td>
      <td><img alt="License" src="https://img.shields.io/github/license/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=flat"/></td>
      <td><img alt="Last Commit" src="https://img.shields.io/github/last-commit/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=flat"/></td>
    </tr>
  </tbody>
</table>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="key-features">🌟 Key Features</h2>

The system leverages deep learning and computer vision to provide a multi-faceted attendance solution:

* **🎭 Real-time Face Recognition**: Detects and identifies registered individuals via live camera feed using **dlib** and `face-recognition`.
* **🕒 Automated Attendance Marking**: Automatically marks **Present** in the SQLite database upon successful face verification.
* **🧓 Attribute Detection**: Predicts **Age**, **Gender** (Male/Female), and **Emotion** (Happy, Sad, Angry, Neutral, etc.) for deeper insights.
* **💾 Robust Data Storage**: Utilizes a **SQLite database (`attendance.db`)** to securely store user profiles and attendance logs.
* **🌐 Interactive Web Interface**: A full **Flask** application with **HTML/CSS/JS** for:
    * Admin/Professor Dashboards (`admin_dashboard.html`, `professor_dashboard.html`).
    * Student/Professor Management (`add_student.html`, `professors.html`).
    * Live Attendance View (`live.html`).
    * Manual Attendance and Log Tracking (`manual_attendance.html`, `log.html`).
* **⚙️ Pre-trained Deep Learning Models**: Uses specialized **TensorFlow/Keras** models for highly accurate attribute prediction.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

## 🏗️ Project Architecture & Flow

The system follows a typical MVC pattern, facilitated by the **Flask** framework, to manage the data flow from the camera to the database and back to the web interface.

### 🧭 Working Flow
1.  **Capture**: `live_attendance_module.py` captures the live video stream using **OpenCV**.
2.  **Detection & Encoding**: Faces are detected, and their embeddings are compared against pre-calculated encodings stored in `known_face_encodings.pkl`.
3.  **Attribute Prediction**: Deep learning models are used to determine age, gender, and emotion.
4.  **Database Update**: Upon successful recognition, the `attendance.db` database is updated by the utility scripts.
5.  **Web Display**: The `app.py`, `manager_app.py`, and `student_manager_app.py` Flask routes render the results to the various HTML templates in the `/templates` folder.

### 📁 Core Structure

├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── __pycache__
    ├── database_utils.cpython-312.pyc
    ├── shared_state.cpython-312.pyc
    └── utils.cpython-312.pyc
├── app.py
├── attendance.db
├── data
    ├── sample.csv
    ├── sample.txt
    ├── sample.xlsx
    ├── sample.xml
    └── sample_excel.xlsx
├── database_setup.py
├── dlib-19.22.99-cp39-cp39-win_amd64.whl
├── git
├── known_face_encodings.pkl
├── live_attendance_module.py
├── manager_app.py
├── output
    ├── output.csv
    ├── output.txt
    ├── output_excel.xlsx
    └── web_data.csv
├── requirements.txt
├── static
    ├── images
    │   ├── face_scan_background.png
    │   └── how_facial_recognition_works.png
    ├── style-3d.css
    └── style.css
├── student_manager_app.py
├── templates
    ├── add_professor.html
    ├── add_student.html
    ├── admin_dashboard.html
    ├── base.html
    ├── configure_session.html
    ├── dashboard.html
    ├── edit_professor_profile.html
    ├── edit_student.html
    ├── landing.html
    ├── layout.html
    ├── live.html
    ├── log.html
    ├── login.html
    ├── manual_attendance.html
    ├── professor_dashboard.html
    ├── professor_profile.html
    ├── professors.html
    ├── schedule.html
    └── students.html
└── tesnorflow.ipynb


<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="technologies-used"> 🛠️ Technologies Used</h2>

### Backend & Core Logic
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![TensorFlow/Keras](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-00AEEF?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

### Frontend & Utilities
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="installation-setup"> ⚙️ Installation & Setup </h2>

### 📋 Prerequisites

Ensure you have **Python 3.x** installed. The project relies on specific versions of libraries like `dlib`, which can sometimes require system-level dependencies.

### 1. Clone the Repository


git clone [https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System.git](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System.git)
cd Face-Based-Attendance-Attribute-System
2. Create and Activate Virtual Environment
It is highly recommended to use a virtual environment.



python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate
3. Install Dependencies
Install all required packages. Note: dlib can take a while to install. The provided .whl file (dlib-19.22.99-cp39-cp39-win_amd64.whl) is for Python 3.9 on Windows 64-bit; you may need to install the library directly if your setup differs.


pip install -r requirements.txt
4. Run the Application
Execute the main Flask application file.



python app.py
Then open your browser and visit 👉 http://127.0.0.1:5000/ to access the web interface.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="screenshots"> 📸 Screenshots </h2>

Placeholder: Add your project screenshots here (e.g., dashboard, live feed, etc.)

<div align="center"> <img src="./static/images/how_facial_recognition_works.png" alt="Facial Recognition Screenshot Example"/> </div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="future-enhancements">💡 Future Enhancements</h2>

Improve age/gender/emotion model accuracy with transfer learning on a larger, domain-specific dataset.

Implement real-time reporting via WebSockets for the live attendance page.

Integrate a richer database like PostgreSQL or MySQL.

Add multi-factor authentication for admin and professor logins.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="contribution-guidelines">🤝👤 Contribution Guidelines</h2>

We welcome all contributions! Please check out the existing guidelines:

Code of Conduct: CODE_OF_CONDUCT.md

Contributing: CONTRIBUTING.md

Ways to Contribute
🐛 Bug Fixes: Help squash bugs in the recognition module or the web application.

✨ New Features: Suggest and implement new features (e.g., real-time graphs, advanced reporting).

📚 Documentation: Improve guides and explanations.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="license">📄 License</h2>

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="author">🧑‍🏫 Author</h2>

Anshul | B.Tech in Data Science | AI & Software Engineering and Machine Learning Enthusiast

📧 Contact: anshulsharma7162@gmail.com

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 align="center"> <p style="font-family:var(--ff-philosopher);font-size:3rem;"><b> Show some <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Red%20Heart.png" alt="Red Heart" width="40" height="40" /> by starring this awesome repository! </p> </h2>

<p align="center"> <a href="#top" style="font-size: 18px; padding: 8px 16px; display: inline-block; border: 1px solid #ccc; border-radius: 6px; text-decoration: none;"> ⬆️ Back to Top </a> </p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
