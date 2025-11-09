# --- manager_app.py ---
# This is a separate, optional Tkinter application intended as a control panel
# for managing the database (students, sessions, and starting the web server).
# You can run this file to manage certain aspects of your attendance system
# instead of relying solely on the web interface.

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import pickle
import os
import face_recognition # Needed if generating encodings in this app
import cv2 # Needed if generating encodings in this app
import numpy as np # Needed if generating encodings in this app
import subprocess # To run the Flask web app in a separate process

# --- Configuration ---
DB_FILE = 'attendance.db' # Path to your database file

# --- Database Helper Functions (copied from app.py/database_setup.py as needed for this app) ---
def get_distinct_from_db(column_name):
    """Helper function to fetch unique values for filter dropdowns (e.g., branches, semesters)."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            if column_name in ['semester', 'admission_year']:
                query = f"SELECT DISTINCT {column_name} FROM students WHERE {column_name} IS NOT NULL ORDER BY CAST({column_name} AS INTEGER)"
            else:
                query = f"SELECT DISTINCT {column_name} FROM students WHERE {column_name} IS NOT NULL ORDER BY {column_name}"
            cursor.execute(query)
            return [item[0] for item in cursor.fetchall()]
    except Exception as e:
        messagebox.showerror("DB Error", f"Could not fetch {column_name}: {e}")
        return []

# --- Face Processing Utility (if used for student management directly in Tkinter) ---
def generate_encoding_from_image(image_path):
    """Loads an image, finds the face, and returns the encoding (for Tkinter usage)."""
    try:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) == 1:
            return encodings[0]
        else:
            messagebox.showerror("Validation Error", f"Found {len(encodings)} faces. Please use a clear photo with exactly one face.")
            return None
    except Exception as e:
        messagebox.showerror("Image Error", f"Could not process image: {e}")
        return None

# --- GUI Windows (Tkinter Toplevel windows for specific functionalities) ---

class AddStudentWindow(tk.Toplevel):
    """
    A Tkinter Toplevel window for adding new student records.
    (This class is mostly a placeholder as the web UI handles student addition better)
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Student (Tkinter)")
        self.geometry("400x200") # Smaller for placeholder
        ttk.Label(self, text="This window could offer student management if needed.").pack(padx=20, pady=20)
        ttk.Label(self, text="For full student management, please use the web interface at /students and /add_student.").pack(padx=20, pady=10)
        
        # Example: Link to open web browser
        def open_web_add_student():
            import webbrowser
            webbrowser.open("http://127.0.0.1:5000/add_student")
        
        ttk.Button(self, text="Open Web Add Student Page", command=open_web_add_student).pack(pady=10)


class SessionConfigWindow(tk.Toplevel):
    """
    A Tkinter Toplevel window for configuring a live attendance session.
    This mirrors the functionality of /configure web route.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Configure Attendance Session")
        self.geometry("450x400")
        self.transient(parent) # Makes it appear on top of parent
        self.grab_set() # Prevents interaction with other windows until this is closed

        # Fetch available options from DB
        self.available_branches = get_distinct_from_db('branch')
        self.available_semesters = get_distinct_from_db('semester')
        self.available_subjects = get_distinct_from_db('subject')

        # Tkinter variables to hold selected values
        self.branch_vars = {branch: tk.BooleanVar(value=False) for branch in self.available_branches}
        self.semester_var = tk.StringVar(value="")
        self.subject_var = tk.StringVar(value="")

        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Branch Selection (Checkbuttons)
        branch_frame = ttk.LabelFrame(main_frame, text="Select Branch(es)")
        branch_frame.pack(fill=tk.X, pady=10)
        if self.available_branches:
            for branch in self.available_branches:
                ttk.Checkbutton(branch_frame, text=branch, variable=self.branch_vars[branch]).pack(anchor=tk.W, padx=10)
        else:
            ttk.Label(branch_frame, text="No branches found. Add students first.").pack(padx=10, pady=5)
            
        # Semester Selection (Combobox)
        ttk.Label(main_frame, text="Select Semester:").pack(anchor=tk.W, pady=(10,0))
        semester_combobox = ttk.Combobox(main_frame, textvariable=self.semester_var, 
                                        values=self.available_semesters, state="readonly")
        semester_combobox.pack(fill=tk.X, pady=5)
        if self.available_semesters:
            semester_combobox.set("-- Choose a semester --") # Default placeholder
        else:
            semester_combobox.set("No semesters found.")

        # Subject Selection (Combobox - Optional)
        ttk.Label(main_frame, text="Select Subject (Optional):").pack(anchor=tk.W, pady=(10,0))
        subject_combobox = ttk.Combobox(main_frame, textvariable=self.subject_var, 
                                       values=self.available_subjects, state="readonly")
        subject_combobox.pack(fill=tk.X, pady=5)
        if self.available_subjects:
            subject_combobox.set("-- All Subjects --")
        else:
            subject_combobox.set("No subjects found.")

        # Button to start session (would interact with Flask session indirectly)
        ttk.Button(main_frame, text="Start Live Attendance (via Web)", command=self.start_session).pack(pady=20)
        ttk.Label(main_frame, text="This opens the web app's live page.").pack(pady=(0, 5))


    def start_session(self):
        """
        Gathers selected criteria and opens the web application's live attendance page.
        This Tkinter app itself does NOT manage the Flask session directly.
        It simply points the user to the web UI.
        """
        selected_branches = [branch for branch, var in self.branch_vars.items() if var.get()]
        selected_semester = self.semester_var.get()
        selected_subject = self.subject_var.get()

        if not selected_branches or not selected_semester:
            messagebox.showwarning("Selection Missing", "Please select at least one branch and a semester.")
            return

        # In a real integrated scenario, this Tkinter app would trigger an API call
        # to the Flask backend to set the session details, then open the browser.
        # For simplicity here, we instruct the user to use the web /configure page.
        
        # Open web browser to the configure page first so Flask session is set.
        # Then the user would click 'Start Filtered Attendance Session' on the web page.
        
        messagebox.showinfo("Action Required", 
                            "Please navigate to 'http://127.0.0.1:5000/configure' in your web browser, "
                            "select the exact same branch(es) and semester you chose here, "
                            "and then click 'Start Filtered Attendance Session'.")
        
        # It's better to open the /configure page directly
        import webbrowser
        webbrowser.open(f"http://127.0.0.1:5000/configure?branches={','.join(selected_branches)}&semester={selected_semester}&subject={selected_subject}")

        self.destroy()


# --- Main Application Window (Tkinter) ---
class MainApp(tk.Tk):
    """The main Tkinter application window, serving as a control panel."""
    def __init__(self):
        super().__init__()
        self.title("Attendance Management Control Panel (Tkinter)")
        self.geometry("500x400")

        # Configure styling for ttk widgets
        style = ttk.Style(self)
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 14), padding=10)

        # Main title label
        ttk.Label(self, text="Management Control Panel").pack(pady=20)

        # Buttons to open various functionalities
        ttk.Button(self, text="Manage Students (via Web UI)", command=self.open_student_manager).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(self, text="Start Live Attendance Session (via Web UI)", command=self.open_session_config).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(self, text="Run Flask Web Server", command=self.run_web_server).pack(fill=tk.X, padx=50, pady=10)
    
    def open_student_manager(self):
        """Opens the web-based student management page."""
        import webbrowser
        webbrowser.open("http://127.0.0.1:5000/students")
        # In a full Tkinter app, this would ideally open a new Tkinter window
        # AddStudentWindow(self) # Replaced with web link for simplicity and completeness

    def open_session_config(self):
        """Opens the Tkinter session configuration window."""
        SessionConfigWindow(self)

    def run_web_server(self):
        """Starts the Flask web server (app.py) in a separate process."""
        print("Starting the Flask web server...")
        try:
            # Use sys.executable to ensure the current Python interpreter is used
            # We don't wait for it to finish, so it runs in the background.
            subprocess.Popen([tk.sys.executable, 'app.py'])
            messagebox.showinfo("Server Status", "Web server has been started in the background.\nYou can now access it at http://127.0.0.1:5000")
        except FileNotFoundError:
            messagebox.showerror("Error", "Could not find 'app.py'. Make sure it's in the same folder as this manager.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start web server: {e}")

if __name__ == "__main__":
    # Ensure Tkinter is initialized with sys.executable for subprocess safety
    import sys
    tk.sys = sys # Attach sys to tk module for cleaner access in subprocess.Popen
    app = MainApp()
    app.mainloop()

