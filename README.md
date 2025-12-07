<img src="[Your GIF Banner Image]" width="100%">

<div align="center"><img src="[Your System Logo Image]" style="width: 220px; height: 220px;" alt="AI Face Attendance System Logo" /></div>

<h1 align="center">🧠 AI Face Attendance & Attribute System</h1>

<div align="center" style="margin: 10px 0 24px;">
  <a href="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/issues">🐛 Report Bug</a>
  •
  <a href="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/issues">💡 Request Feature</a>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00FF7F&width=500&lines=Face+Recognition+%7C+Age+%7C+Gender+%7C+Emotion+Detection;Powered+by+OpenCV,+Keras,+and+Flask;The+Next-Level+Attendance+Solution!" alt="Dynamic Text Banner" />
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="overview">🌟 Project Overview</h2>

> The **AI Face Attendance System** is an advanced, real-time Python-based solution for automated attendance tracking. It goes beyond simple recognition by integrating **Age**, **Gender**, and **Emotion** detection attributes, offering rich contextual data for every attendance record. The entire system is managed via an interactive, user-friendly **Flask web interface**.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="features">🚀 Key Features</h2>

The system leverages deep learning models to provide comprehensive insights in real-time.

### 👤 Core Biometrics & Recognition
* 🎭 **Face Detection & Recognition**: Utilizes robust Deep Learning models (dlib/face-recognition) and **OpenCV** to accurately identify registered individuals from a live video stream.
* 🕒 **Automated Attendance**: Marks attendance **instantly** in the database upon successful identity verification, complete with a timestamp.

### 📈 Attribute Detection (Deep Learning)
* 🧓 **Age Prediction**: Estimates the person’s approximate age using a dedicated **CNN model**.
* 🚹 **Gender Classification**: Accurately classifies the detected face as male or female.
* 😄 **Emotion Recognition**: Identifies the facial emotion (e.g., Happy, Sad, Angry, Neutral), providing insights into the user's state.

### 🌐 Web Interface & Database
* 💾 **SQLite Database Integration**: Seamlessly stores and manages **user details** and **real-time attendance records** (Name, Time, Age, Gender, Emotion).
* 🌐 **Interactive Frontend**: A modern interface built with **HTML, CSS, and JavaScript** for live video feed display, real-time attribute predictions, and an attendance dashboard.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="tech-stack">🧩 Technology & Models</h2>

A breakdown of the core technologies and libraries powering the system.

<table align="center">
  <thead>
    <tr>
      <th>Component</th>
      <th>Technology Used</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Backend / Core Logic</b></td>
      <td><img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/></td>
      <td>Primary programming language, Flask for server integration.</td>
    </tr>
    <tr>
      <td><b>Computer Vision</b></td>
      <td><img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/></td>
      <td>Real-time video stream processing and frame handling.</td>
    </tr>
    <tr>
      <td><b>Deep Learning</b></td>
      <td><img alt="TensorFlow/Keras" src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/></td>
      <td>Models for Age, Gender, and Emotion prediction.</td>
    </tr>
    <tr>
      <td><b>Face Recognition</b></td>
      <td><img alt="dlib" src="https://img.shields.io/badge/dlib-0072C6?style=for-the-badge&logo=dlib&logoColor=white"/> / <img alt="face-recognition" src="https://img.shields.io/badge/face--recognition-black?style=for-the-badge&logo=face-recognition&logoColor=white"/></td>
      <td>HOG/CNN-based facial embedding generation for identification.</td>
    </tr>
    <tr>
      <td><b>Database</b></td>
      <td><img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/></td>
      <td>Lightweight and integrated database for attendance logs.</td>
    </tr>
    <tr>
      <td><b>Frontend</b></td>
      <td><img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/> <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/></td>
      <td>Web interface for displaying results and interacting with the system.</td>
    </tr>
  </tbody>
</table>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%">

<h2 id="working-flow">🧭 System Flowchart</h2>

This chart illustrates the real-time process from video capture to attendance logging and dashboard update.

<div align="center">

```mermaid
flowchart TD
    A[Start Live Webcam Stream] --> B{Detect Face?};
    B -- Yes --> C[Extract Face Embeddings & Attributes];
    B -- No --> A;
    C --> D{Recognize ID?};
    C --> E[Predict Age, Gender, Emotion (DL Models)];
    D -- Yes --> F[Check if Already Attended Today];
    D -- No --> G[Display: "Unknown User"];
    F -- No --> H[Log Attendance to SQLite DB];
    F -- Yes --> G;
    G --> I[Update Web Dashboard];
    H --> I;
    E --> I;
    I --> J[Display: Live Results, Attendance Log];
</div><img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="project-structure">📂 Project Structure</h2>The repository is organized for clarity and modularity.BashAI-Face-Attendance-System/
├── app.py                      # Main Flask backend application
├── models/
│   ├── age_model.h5            # Pre-trained CNN for Age Prediction
│   ├── gender_model.h5         # Pre-trained CNN for Gender Prediction
│   └── emotion_model.h5        # Pre-trained CNN for Emotion Recognition
├── database/
│   └── attendance.db           # SQLite Database file
├── static/
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript for frontend logic
│   └── images/                 # Store screenshots and user images
├── templates/
│   ├── index.html              # Main attendance page / Live feed
│   └── dashboard.html          # Attendance log and statistics
├── utils/
│   ├── face_recognition.py     # Helper functions for face processing
│   ├── database_helper.py      # Functions for database interaction
│   └── preprocess.py           # Data preprocessing and model loading
└── README.md
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="installation-setup">⚙️ Installation & Setup</h2>📋 PrerequisitesEnsure you have Python 3.x installed on your system.1️⃣ Clone the RepositoryBashgit clone [https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System](https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System)
cd Face-Based-Attendance-Attribute-System
2️⃣ Create Virtual EnvironmentIt is highly recommended to use a virtual environment.Bashpython -m venv venv
source venv/bin/activate    # Linux/Mac
.\venv\Scripts\activate     # Windows (PowerShell/CMD)
3️⃣ Install DependenciesInstall all necessary Python packages. This may take a few minutes as it includes heavy libraries like TensorFlow and dlib (via face-recognition).Bashpip install -r requirements.txt
4️⃣ Run the ApplicationStart the Flask server:Bashpython app.py
Then, open your web browser and navigate to: 👉 http://127.0.0.1:5000/<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="database-schema">🧾 Database Schema (SQLite)</h2>TableColumnTypeDescriptionattendanceidINTEGERPrimary Key, Auto-incrementnameTEXTPerson's name (from recognition)genderTEXTGender detected (Male/Female)ageINTEGERPredicted ageemotionTEXTDetected emotion (Happy, Sad, Angry, etc.)timeTEXTAttendance timestamp<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="screenshots">📸 Screenshots</h2>(Add your eye-catching screenshots here for the login, live feed, and dashboard.)<div align="center"><img src="./static/images/screenshots/live_feed.png" alt="Live Attendance Screenshot"/></div><div align="center"><img src="./static/images/screenshots/dashboard_log.png" alt="Attendance Dashboard Screenshot"/></div><img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="future-enhancements">💡 Future Enhancements</h2>Improve accuracy of Face Recognition using a more robust Deep Learning-based facial embeddings network (e.g., FaceNet, ArcFace).Add a User Registration module within the web interface to enroll new users without manual file handling.Implement a CSV/Excel Export feature for attendance reports.Migrate from SQLite to a full-fledged database like PostgreSQL or MySQL for scalability.<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="contributing">🤝 Contributing</h2>We welcome contributions! If you have suggestions or want to report a bug, please check out our CONTRIBUTING.md.⭐ Star the Repository.Fork the project and create your Feature Branch.Submit a Pull Request with clear details of your changes.<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="license">📜 License</h2>This project is licensed under the Apache License 2.0—you are free to use, modify, and distribute it for educational and research purposes.<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%"><h2 id="author">🧑‍💻 Author & Contact</h2>Anshul * Role: B.Tech in Data Science | AI & Software Engineering and Machine Learning EnthusiastEmail: anshulsharma7162@gmail.com<div align="center"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" alt="Glowing Star" width="25" height="25" /> Show your appreciation by starring this repository! <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" alt="Glowing Star" width="25" height="25" /></div><img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=65&section=footer"/>
