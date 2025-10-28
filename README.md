# 🧠 AI Face Attendance System

An **Advanced Python-based Face Recognition Attendance System** integrated with **Age, Gender, and Emotion Detection**, powered by **OpenCV, Deep Learning models**, and a **SQLite database**.  
The system captures a person’s face in real-time, detects their identity, marks attendance automatically, and displays their mood, age, and gender — all through an interactive web interface built using **HTML, CSS, and JavaScript**.

---

## 🚀 Features

- 🎭 **Face Detection & Recognition** – Detects and identifies individuals using live camera feed.
- 🧓 **Age Prediction** – Estimates the person’s approximate age.
- 🚹 **Gender Detection** – Classifies the detected face as male or female.
- 😄 **Emotion Detection** – Recognizes the facial emotion (Happy, Sad, Angry, Neutral, etc.).
- 🕒 **Automated Attendance** – Records attendance in real-time once a face is verified.
- 💾 **SQLite Database Integration** – Stores user details, attendance records, and timestamps.
- 🌐 **Frontend Interface** – Built using HTML, CSS, and JS for displaying live results and logs.
- 📸 **Real-time Processing** – Uses OpenCV to process video frames efficiently.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Programming Language** | Python |
| **Libraries** | OpenCV, NumPy, TensorFlow/Keras, dlib, face-recognition |
| **Database** | SQLite |
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask / Python (for server integration) |
| **Models Used** | Pre-trained Age, Gender, and Emotion models |

---

## 📂 Project Structure

AI-Face-Attendance-System/
├── app.py # Main Python backend
├── models/
│ ├── age_model.h5
│ ├── gender_model.h5
│ └── emotion_model.h5
├── database/
│ └── attendance.db
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── templates/
│ ├── index.html
│ ├── dashboard.html
│ └── report.html
├── utils/
│ ├── face_recognition.py
│ ├── database_helper.py
│ └── preprocess.py
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/<your-username>/AI-Face-Attendance-System.git
cd AI-Face-Attendance-System
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy code
python app.py
Then open your browser and visit 👉 http://127.0.0.1:5000/

🧠 Working Flow
System captures live video from webcam.

Detects and recognizes faces using the stored dataset.

Predicts Age, Gender, and Emotion using deep learning models.

Once a registered face is recognized, it marks attendance automatically in the SQLite database.

Dashboard displays:

Current date & time

Recognized faces

Emotion/Age/Gender details

Attendance records

🧾 Database Schema (SQLite)
Table: attendance

Column	Type	Description
id	INTEGER	Primary key
name	TEXT	Person name
gender	TEXT	Gender detected
age	INTEGER	Predicted age
emotion	TEXT	Detected emotion
time	TEXT	Timestamp

🧠 Example Models Used
Age Model: Predicts age group from face (using CNN trained on IMDB-WIKI dataset)

Gender Model: Detects gender (Male/Female)

Emotion Model: Detects emotion (Happy, Sad, Angry, Neutral, etc.)

Face Recognition: Uses face_recognition (dlib-based HOG + CNN)

🧑‍💻 Screenshots
(Add your screenshots here after uploading to /static/images/screenshots/)

scss
Copy code
![Dashboard](static/images/screenshots/dashboard.png)
![Live Detection](static/images/screenshots/live_detection.png)
💡 Future Enhancements
Add attendance export (CSV/Excel)

Integrate email notification for absentees

Cloud database (MySQL / Firebase)

Face registration through the web UI

Improve accuracy using deep learning-based facial embeddings

📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it for educational and research purposes.

🧑‍🏫 Author
Anshul [@<your-github-username>]
B.Tech in Data Science | AI & Software Engineering Enthusiast
📧 Contact: your.email@example.com

“Artificial Intelligence is not just about automation — it’s about making systems that think, adapt, and evolve like humans.”

⭐ If you like this project, give it a star on GitHub!

yaml
Copy code

---

Would you like me to:
1. 🧩 Generate a **`requirements.txt`** file for this project (Python libs like `opencv-python`, `face-recognition`, `tensorflow`, etc.)  
2. Or 🖥️ also include a **preview of Flask routes & database schema code snippet** for GitHub completeness?

Which one do you want next?











Cha
