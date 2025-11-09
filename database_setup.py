import sqlite3
import os

DB_FILE = 'attendance.db' # Define the database file path

def create_tables():
    """
    Creates the necessary tables in the SQLite database if they don't exist.
    This function should be run once to set up the database schema.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Students Table: Stores student details and their face encodings
    # Includes branch, semester, admission_year, and subject columns.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        branch TEXT,
        semester INTEGER,
        admission_year INTEGER,
        subject TEXT,  -- Added 'subject' column
        face_encoding BLOB
    );
    """)

    # Professors Table: Stores professor details and optional photo data.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professors (
        prof_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        email TEXT,
        mobile TEXT,
        qualification TEXT,
        experience TEXT,
        achievements TEXT,
        others TEXT,
        photo_data TEXT
    );
    """)

    # Schedule Table: Stores class period information.
    # Includes 'branch' to associate periods with specific branches.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedule (
        period_id INTEGER PRIMARY KEY AUTOINCREMENT,
        period_name TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        prof_id TEXT,
        prof_name TEXT,
        description TEXT,
        branch TEXT,  -- Added 'branch' column
        FOREIGN KEY (prof_id) REFERENCES professors (prof_id)
    );
    """)

    # Attendance Logs Table: Records attendance events.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_roll_no TEXT NOT NULL,
        student_name TEXT,
        period_name TEXT NOT NULL,
        prof_name TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (student_roll_no) REFERENCES students (roll_no)
    );
    """)

    conn.commit()
    conn.close()
    print("Database tables created/verified successfully.")

if __name__ == '__main__':
    # This block ensures that if database_setup.py is run directly,
    # it attempts to create/update the necessary tables.
    create_tables()

