import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sqlite3
import face_recognition
import numpy as np
import pickle
from PIL import Image, ImageTk # Pillow library for image handling in Tkinter

# Define the database file path for this module
DB_FILE = 'attendance.db'

# --- Face Processing Utility ---
def generate_encoding_from_image(image_path):
    """
    Loads an image from the given path, finds face(s), and returns a single face encoding.
    Displays Tkinter message boxes for validation errors.
    """
    try:
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            messagebox.showerror("Validation Error", "No face found in the selected image. Please use a clear photo of a single person.")
            return None
        if len(encodings) > 1:
            messagebox.showerror("Validation Error", "More than one face found in the image. Please select a photo with only one person.")
            return None
        
        return encodings[0]
    except Exception as e:
        messagebox.showerror("Image Error", f"Could not process image: {e}")
        return None

# --- Add Student Window (Tkinter Toplevel) ---
class AddStudentWindow(tk.Toplevel):
    """
    A Tkinter Toplevel window to add new student records.
    This class handles collecting student details, uploading a photo,
    generating a face encoding, and saving to the database.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Student")
        self.geometry("400x650") # Adjusted geometry for more fields
        
        self.parent = parent # Reference to the parent window (e.g., MainApp)
        self.image_path = None
        self.face_encoding = None

        # --- Input Fields ---
        # Roll Number
        tk.Label(self, text="Roll Number:").pack(pady=(10,0))
        self.roll_no_entry = tk.Entry(self)
        self.roll_no_entry.pack(fill=tk.X, padx=20)

        # Name
        tk.Label(self, text="Full Name:").pack(pady=(5,0))
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(fill=tk.X, padx=20)
        
        # Branch
        tk.Label(self, text="Branch:").pack(pady=(5,0))
        self.branch_entry = tk.Entry(self)
        self.branch_entry.pack(fill=tk.X, padx=20)

        # Semester
        tk.Label(self, text="Semester (e.g., 1-8):").pack(pady=(5,0))
        self.semester_entry = tk.Entry(self)
        self.semester_entry.pack(fill=tk.X, padx=20)

        # Year of Admission
        tk.Label(self, text="Year of Admission (e.g., 2023):").pack(pady=(5,0))
        self.admission_year_entry = tk.Entry(self)
        self.admission_year_entry.pack(fill=tk.X, padx=20)

        # Subject (Optional) - Consistent with database schema
        tk.Label(self, text="Subject (Optional):").pack(pady=(5,0))
        self.subject_entry = tk.Entry(self)
        self.subject_entry.pack(fill=tk.X, padx=20)


        # --- Photo Upload Section ---
        tk.Label(self, text="Student Photo:").pack(pady=(10,0))
        self.photo_label = tk.Label(self, text="No photo selected.", fg="grey")
        self.photo_label.pack(pady=5)
        self.photo_preview_label = tk.Label(self, width=150, height=150, relief="solid", borderwidth=1)
        self.photo_preview_label.pack(pady=5)
        
        tk.Button(self, text="Upload Photo", command=self.upload_photo).pack(pady=5)

        # --- Submit Button ---
        tk.Button(self, text="Add Student", command=self.add_student, bg="#28a745", fg="white").pack(pady=20)

    def upload_photo(self):
        """Opens a file dialog for image selection and displays a preview."""
        self.image_path = filedialog.askopenfilename(
            title="Select Student Photo",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if self.image_path:
            # Generate encoding immediately on upload
            self.face_encoding = generate_encoding_from_image(self.image_path)
            if self.face_encoding is not None:
                self.photo_label.config(text=os.path.basename(self.image_path), fg="green")
                # Display image preview
                try:
                    img = Image.open(self.image_path)
                    img.thumbnail((150, 150)) # Resize for preview
                    self.photo_tk = ImageTk.PhotoImage(img)
                    self.photo_preview_label.config(image=self.photo_tk)
                except Exception as e:
                    self.photo_preview_label.config(text="Preview Error")
                    print(f"Error loading photo preview: {e}")
            else:
                self.image_path = None # Reset if encoding failed
                self.photo_label.config(text="No photo selected or face not found.", fg="red")
                self.photo_preview_label.config(image='') # Clear preview
                self.photo_tk = None # Clear image reference

    def add_student(self):
        """Collects form data, saves student to database, and closes the window."""
        roll_no = self.roll_no_entry.get().strip()
        name = self.name_entry.get().strip()
        branch = self.branch_entry.get().strip()
        semester = self.semester_entry.get().strip()
        admission_year = self.admission_year_entry.get().strip()
        subject = self.subject_entry.get().strip() # Optional subject field

        # Input validation
        if not all([roll_no, name, branch, semester, admission_year]):
            messagebox.showerror("Input Error", "Roll Number, Name, Branch, Semester, and Year of Admission are required.")
            return
        
        try:
            # Validate semester and admission_year are integers
            semester = int(semester)
            admission_year = int(admission_year)
        except ValueError:
            messagebox.showerror("Input Error", "Semester and Year of Admission must be numbers.")
            return

        if self.face_encoding is None:
            messagebox.showerror("Input Error", "A valid photo with one face must be uploaded and recognized.")
            return

        try:
            # Convert numpy array to bytes for SQLite BLOB storage
            encoding_bytes = pickle.dumps(self.face_encoding)
            
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            # Insert all student fields, including new ones
            cursor.execute("""
                INSERT INTO students (roll_no, name, branch, semester, admission_year, subject, face_encoding) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (roll_no, name, branch, semester, admission_year, subject, encoding_bytes))
            
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", f"Student {name} added successfully.")
            # In a full app, you might want to trigger a refresh of student list in parent window
            # self.parent.refresh_student_list() 
            self.destroy() # Close the add student window

        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", f"A student with Roll Number '{roll_no}' already exists. Please use a unique Roll Number.")
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

# This __name__ == '__main__' block is typically for running this module independently for testing.
# In the context of manager_app.py, this will be called as a class.
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw() # Hide the main Tkinter window
    AddStudentWindow(root)
    root.mainloop()

