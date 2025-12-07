<img src="[Your GIF Banner Image]" width="100%">

<div align="center"><img src="[Your System Logo Image]" style="width: 220px; height: 220px;" alt="AI Face Attendance System Logo" /></div>

<h1 align="center">🧠 AI Face Attendance & Attribute System</h1>

<div align="center" style="margin: 10px 0 24px;">
  <a href="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/issues">🐛 Report Bug</a>
  •
  <a href="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/issues">💡 Request Feature</a>
  •
  <a href="mailto:anshulsharma7162@gmail.com">📧 Contact Author</a>
</div>

<img src="[Your GIF Banner Image]" width="100%">

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00FF7F&width=550&lines=The+Future+of+Biometric+Attendance;Real-time+Age%2C+Gender%2C+and+Emotion+Analysis;Powered+by+Deep+Learning+and+Flask;The+Next-Level+Attendance+Solution!" alt="Dynamic Text Banner" />
</div>

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="insights">📊 Project Insights & Status</h2>

|                                                                                                                 Status                                                                                                                 |                                                                                                                    Metrics                                                                                                                    |                                                                                                           Codebase                                                                                                           |                                                                                                                   License                                                                                                                  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                             [![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)                                                            | [![Visitors](https://api.visitorbadge.io/api/Visitors?path=AnshulSharma9340%2FFace-Based-Attendance-Attribute-System\&countColor=%235C3EE8\&style=for-the-badge)](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System) |                                             [![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)](https://www.python.org/downloads/)                                            |                                                             [![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg?style=for-the-badge)](LICENSE)                                                            |
| [![GitHub Stars](https://img.shields.io/github/stars/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=for-the-badge\&logo=github)](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/stargazers) |      [![GitHub Forks](https://img.shields.io/github/forks/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=for-the-badge\&logo=github)](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/network)      | [![Repo Size](https://img.shields.io/github/repo-size/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=for-the-badge\&logo=github)](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System) | [![Last Commit](https://img.shields.io/github/last-commit/AnshulSharma9340/Face-Based-Attendance-Attribute-System?style=for-the-badge\&logo=git)](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/commits/main) |

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="overview">🌟 Project Overview</h2>

> The **AI Face Attendance System** is a real-time Python & Flask-based solution for automated attendance tracking with **multi-attribute recognition**.
> Alongside facial identification, it predicts **Age**, **Gender**, and **Emotion**, storing detailed contextual information for every attendance entry. Ideal for schools, colleges, and organizations aiming for **advanced biometric attendance**.

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="features">🚀 Key Features</h2>

### 🔬 Multi-Attribute Recognition

* 😄 **Emotion Recognition** – Detects real-time emotions like `Happy`, `Sad`, `Angry`, etc.
* 🧓 **Age & Gender Classification** – Estimates approximate age and gender to enrich attendance logs.
* **Dedicated Deep Learning Models** – Each attribute uses a CNN model (`.h5`) trained for high accuracy.

### 🌐 Core Architecture

* 🎭 **Real-Time Face Recognition** – Uses `dlib`/HOG/CNN embeddings for fast identification.
* 🕒 **Verified Attendance Logging** – Attendance recorded with timestamp + all detected attributes.
* **Flask Web Interface** – Serves video stream, runs model inference, and displays results on a user-friendly frontend.

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="tech-stack">🧩 Technology Stack</h2>

| Component        | Technology                                                                                                                                                                                                    | Details                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Backend / Server | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/> | Flask server handles video stream & API endpoints           |
| Computer Vision  | <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>                                                                                                       | Captures, preprocesses frames, optimizes video streaming    |
| Deep Learning    | <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>   | Loads CNN models for age, gender, emotion prediction        |
| Face Recognition | <img src="https://img.shields.io/badge/dlib-0072C6?style=for-the-badge&logo=dlib&logoColor=white"/> / `face-recognition`                                                                                      | Efficient face detection + 128-D embeddings for recognition |
| Database         | <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>                                                                                                       | Stores attendance logs with attributes                      |
| Models           | Age, Gender, Emotion `.h5` files                                                                                                                                                                              | Pre-trained CNN models in `/models` directory               |

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="working-flow">🧭 System Architecture & Flow</h2>


Live Webcam Stream → Detect Face (OpenCV/dlib)
      │
      ├─ Yes → Recognized? → TensorFlow: Predict Age, Gender, Emotion → Attendance Logged? → SQLite DB → Web Dashboard
      │
      └─ No → Display "Unknown / Enroll"


<img src="[Your GIF Banner Image]" width="100%">

<h2 id="project-structure">📂 Repository Structure</h2>


AI-Face-Attendance-System/
├── app.py                      # Flask server & core logic
├── requirements.txt            # Python dependencies
├── models/                     # CNN models
│   ├── age_model.h5
│   ├── gender_model.h5
│   └── emotion_model.h5
├── database/
│   └── attendance.db           # SQLite DB
├── static/                     # Frontend assets
│   ├── css/
│   ├── js/
│   └── images/                 # User images & screenshots
├── templates/
│   ├── index.html              # Live attendance page
│   └── dashboard.html          # Attendance logs dashboard
└── utils/
    ├── face_recognition.py     # Face encoding & matching
    ├── database_helper.py      # DB CRUD operations
    └── preprocess.py           # Image preprocessing & model loading


<img src="[Your GIF Banner Image]" width="100%">

<h2 id="installation-setup">⚙️ Installation & Quick Start</h2>

**Prerequisites:** Python 3.x, Webcam connected

**1️⃣ Clone & Navigate**


git clone https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System
cd Face-Based-Attendance-Attribute-System


**2️⃣ Virtual Environment**


python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows


**3️⃣ Install Dependencies**


pip install -r requirements.txt


**4️⃣ Run the Application**


python app.py

Visit 👉 `http://127.0.0.1:5000/`

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="database-schema">🧾 Database Schema (SQLite)</h2>

| Column  | Type                              | Description                     |
| ------- | --------------------------------- | ------------------------------- |
| id      | INTEGER PRIMARY KEY AUTOINCREMENT | Unique attendance ID            |
| name    | TEXT                              | Recognized person               |
| gender  | TEXT                              | Detected gender                 |
| age     | INTEGER                           | Predicted age                   |
| emotion | TEXT                              | Detected emotion                |
| time    | TEXT                              | Timestamp (YYYY-MM-DD HH:MM:SS) |

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="screenshots">📸 Visual Demo</h2>

<div align="center">
<h3>Live Attendance Feed & Attributes</h3>
<img src="./static/images/screenshots/live_feed.png" alt="Live Feed" style="width:80%;border:2px solid #00FF7F;border-radius:8px;"/>
<h3>Dashboard & Attendance Log</h3>
<img src="./static/images/screenshots/dashboard_log.png" alt="Dashboard" style="width:80%;border:2px solid #5C3EE8;border-radius:8px;"/>
</div>

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="future-enhancements">💡 Roadmap</h2>

* Upgrade to FaceNet/ArcFace for higher accuracy.
* Web-based admin enrollment for new users.
* CSV/Excel export & analytics dashboards.
* Scale DB to PostgreSQL/MySQL for large deployments.

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="contributing">🤝 Contributing</h2>

* ⭐ Star the repo
* Fork & PR with well-documented code
* Report issues via GitHub Issues

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="license">📜 License</h2>

Licensed under **Apache License 2.0** – free for research & educational use.

<img src="[Your GIF Banner Image]" width="100%">

<h2 id="author">🧑‍💻 Author & Contact</h2>

Anshul Sharma | B.Tech Data Science
Email: [anshulsharma7162@gmail.com](mailto:anshulsharma7162@gmail.com)
GitHub: [@AnshulSharma9340](https://github.com/AnshulSharma9340)

<div align="center"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" width="25" height="25"/> Star this repo to show appreciation! <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" width="25" height="25"/></div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
