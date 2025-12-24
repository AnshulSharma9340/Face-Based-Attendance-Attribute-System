# 🚀 AI Face Attendance System

### **Face-Based-Attendance-Attribute-System**

#### *Next-Gen Multi-Attribute Biometric Recognition | Flask • Deep Learning • Computer Vision*

<p align="center">
  <img src="https://img.shields.io/badge/AI%20POWERED-Facial%20Recognition-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Deep%20Learning-Attributes%20Prediction-ff69b4?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-success?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System/raw/main/static/images/face_scan_background.png" width="650"/>
</p>

---

## 🌌 **Dynamic Text Banner**

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=26&pause=1000&color=30F730&center=true&vCenter=true&width=650&lines=AI+Powered+Face+Attendance+System;Real-Time+Age+Gender+Emotion+Detection;Flask+%7C+OpenCV+%7C+TensorFlow;Advanced+Biometric+Recognition+Suite;Made+by+Anshul+Sharma+DS+Student"/>
</p>

---

# 📊 **Project Insights**

| Status                | Metrics     | Codebase      | License        |
| --------------------- | ----------- | ------------- | -------------- |
| 🔥 Active Development | 👀 Visitors | 🐍 Python 3.x | 📝 Apache-2.0  |
| ⭐ Stars               | 🍴 Forks    | 📦 Repo Size  | ⏱️ Last Commit |

---

# 🌟 **Project Overview**

The **AI Face Attendance System** is an advanced, real-time, multi-attribute biometric solution built using **Flask, OpenCV, dlib, TensorFlow, and CNN-based models**.

It doesn’t just mark attendance —
✨ It logs **Age + Gender + Emotion**
✨ It matches **Face Embeddings (128-D)**
✨ It stores **Complete Contextual Metadata**
✨ It supports **Live Dashboard + CSV/Excel export**

Ideal for:
🎓 Colleges · 🏢 Corporate Offices · 🏫 Schools · 🔬 Research Labs · 📊 Smart Entry Systems

---

# 🚀 **Key Features**

### 🔬 **Multi-Attribute Recognition**

* 😄 Emotion Detection (Happy, Sad, Angry…)
* 🧓 Age Classification
* 🚻 Gender Prediction
* 🧠 CNN-based models (`.h5`) for high accuracy

### 🌐 **Face Recognition Engine**

* 128-D embeddings (dlib/face-recognition)
* High accuracy, fast detection pipeline
* Auto-identification from stored encodings

### 📡 **Live Attendance Logging**

* Timestamped entries
* Auto-detection of faces
* Context-rich attendance metadata

### 🎛️ **Web-Based Interface**

* Flask dashboard
* Real-time video streaming
* Live logs + charts

---

# 🧩 **Technology Stack**

| Component        | Technology              | Description                         |
| ---------------- | ----------------------- | ----------------------------------- |
| Backend          | Flask                   | Video streaming, routing, templates |
| CV Engine        | OpenCV                  | Frame capture, detection            |
| Deep Learning    | TensorFlow/Keras        | CNN models for attributes           |
| Face Recognition | dlib / face-recognition | 128-D embeddings                    |
| Database         | SQLite                  | Attendance logs                     |
| UI               | HTML • CSS              | Dashboard & live feed               |

---

# 🧭 **System Architecture**

```
     ┌──────────────────────────────────────────┐
     │          LIVE WEBCAM STREAM              │
     └───────────────┬──────────────────────────┘
                     ▼
         ┌────────────────────────┐
         │  FACE DETECTION (CV)   │
         └───────────────┬────────┘
                         │ Yes
                         ▼
         ┌──────────────────────────┐
         │  FACE RECOGNIZED ?       │──No──▶ Unknown User
         └───────────────┬──────────┘
                         │ Yes
                         ▼
      ┌─────────────────────────────────────────┐
      │ TENSORFLOW MODELS (Age • Gender • Emotion) │
      └───────────────────┬───────────────────────┘
                          ▼
                Attendance Logging  
                          ▼
         ┌────────────────────────────────┐
         │     SQLite Database            │
         └────────────────────────────────┘
                          ▼
                Web Dashboard & Logs
```

---

# 📂 **Repository Structure**

```
Face-Based-Attendance-Attribute-System/
│── app.py
│── manager_app.py
│── student_manager_app.py
│── live_attendance_module.py
│── database_setup.py
│── database/
│── models/ (Age, Gender, Emotion .h5)
│── templates/ (HTML UI)
│── static/
│   ├── images/
│   ├── css/
│   └── js/
│── known_face_encodings.pkl
│── attendance.db
│── requirements.txt
│── sample.csv / sample.txt / sample.xml
│── output/
└── README.md
```

---

# ⚙️ **Installation & Quick Start**

## 1️⃣ Clone Repo

```bash
git clone https://github.com/AnshulSharma9340/Face-Based-Attendance-Attribute-System
cd Face-Based-Attendance-Attribute-System
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Server

```bash
python app.py
```

▶ Visit: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

# 🧾 **Database Schema**

| Column  | Type    | Description                |
| ------- | ------- | -------------------------- |
| id      | INTEGER | Auto-increment primary key |
| name    | TEXT    | User name                  |
| gender  | TEXT    | Predicted gender           |
| age     | INTEGER | Predicted age              |
| emotion | TEXT    | Detected emotion           |
| time    | TEXT    | Timestamp                  |

---

# 📸 **Visual Demo**

### 🎥 Live Attendance Feed

<img src="static/images/face_scan_background.png" width="500"/>

### 🖥️ Dashboard Screenshot

<img src="static/images/how_facial_recognition_works.png" width="500"/>

---

# 💡 **Future Roadmap**

* 🔥 Migrate to FaceNet / ArcFace
* 🌍 Cloud-based user enrollment
* 📊 Analytics + Power BI dashboard
* 🗄️ MySQL/PostgreSQL support
* 📱 Mobile App for student attendance
* 🎯 Model optimization (ONNX/TensorRT)

---

# 🤝 Contributing

* ⭐ Star the repo
* 🍴 Fork and PR
* 🐛 Report issues on GitHub

---

# 📜 License

Licensed under **Apache License 2.0**

---

# 🧑‍💻 Author

**Anshul Sharma**
📧 Email: *[anshulsharma7162@gmail.com](mailto:anshulsharma7162@gmail.com)*
🐙 GitHub: *@AnshulSharma9340*

<p align="center"><b>🌟 Star this repository if you like the project!</b></p>
