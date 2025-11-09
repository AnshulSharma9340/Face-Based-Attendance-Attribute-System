import sqlite3
import pickle
import numpy as np  # This will also be needed for de-serializing

# Define the database file path for this module
DB_FILE = 'attendance.db'

def load_filtered_encodings(branches, semester):
    """
    Loads face encodings only for students matching the specified branches and semester.
    
    Args:
        branches (list): A list of branches (e.g., ['CSE', 'ECE']) to filter students by.
        semester (int): The selected semester (e.g., 4) to filter students by.

    Returns:
        A tuple of (known_encodings, known_roll_numbers) for the filtered students.
    """
    conn = sqlite3.connect(DB_FILE)
    
    # Construct the query dynamically for the 'IN' clause to handle multiple branches.
    # The '?' placeholders will be filled securely by the tuple of parameters.
    query = f"""
        SELECT roll_no, face_encoding FROM students 
        WHERE branch IN ({','.join('?' for _ in branches)}) 
        AND semester = ? AND face_encoding IS NOT NULL
    """
    params = branches + [semester] # Combine branch params with semester param
    
    cursor = conn.cursor()
    cursor.execute(query, params) # Execute the query with parameters
    
    known_encodings = []
    known_roll_numbers = []
    
    for row in cursor.fetchall():
        roll_no = row[0]
        encoding_bytes = row[1]
        
        # De-serialize the BLOB data back into a numpy array (face encoding)
        encoding = pickle.loads(encoding_bytes)
        
        known_encodings.append(encoding)
        known_roll_numbers.append(roll_no)
        
    conn.close()
    print(f"Loaded {len(known_encodings)} students for this session based on filters.")
    return known_encodings, known_roll_numbers

def start_live_attendance(session_details):
    """
    This function is a placeholder and demonstrates how filtered encodings *could* be used
    if live attendance was managed directly by this module. In the current setup,
    the live attendance logic is integrated directly into app.py's Socket.IO handler.
    
    Args:
        session_details (dict): Dictionary containing 'branches' (list) and 'semester' (int).
    """
    # 1. Load ONLY the relevant faces based on session criteria
    branches = session_details['branches'] 
    semester = session_details['semester'] 
    
    known_encodings, known_roll_numbers = load_filtered_encodings(branches, semester)
    
    if not known_encodings:
        print("No students enrolled for this session matching the filter criteria. Aborting live attendance for this configuration.")
        return

    # 2. In a real application, this would then initiate the camera feed loop
    # and perform face recognition using these filtered known_encodings and known_roll_numbers.
    # The logic for this is now primarily within app.py's Socket.IO handler.
    print("Live attendance session is configured to filter students. Monitoring...")
    # ... video capture and recognition loop using filtered data would go here ...
    # A face detected that is NOT in the filtered list would simply not be matched for attendance.

