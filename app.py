from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox

# saves student info to the text file 
def save_student_info(name,title):
    with open("data/students.txt", "a") as file:
        file.write(title + "," + name +  "\n")

# validates first name  and last name 
def validate_name():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    if not first_name or not last_name:
        messagebox.showwarning("Warning", "Please enter both first name and last name.")
        return False
    return True

# validates title 
def validate_title():
    title = entry_title.get()
    if not title:
        messagebox.showwarning("Warning", "Please select a title.")
        return False
    return True

# validates age 
def validate_age():
    age = entry_age.get()
    if not age:
        messagebox.showwarning("Warning", "Please enter the age.")
        return False
    if not age.isdigit():
        messagebox.showwarning("Warning", "Age must be a number.")
        return False
    return True

def validate_nationality():
    nationality = entry_nationality.get()
    if not nationality:
        messagebox.showwarning("Warning", "Please select a nationality.")
        return False
    return True

def validate_registration_status():
    registration_status = entry_registration_status.get()
    if not registration_status:
        messagebox.showwarning("Warning", "Please select the registration status.")
        return False
    return True

def validate_completed_courses():
    completed_courses = entry_completed_courses.get()
    if not completed_courses:
        messagebox.showwarning("Warning", "Please enter the number of completed courses.")
        return False
    if not completed_courses.isdigit():
        messagebox.showwarning("Warning", "Number of completed courses must be a positive integer.")
        return False
    return True

def validate_num_semesters():
    num_semesters = entry_num_semesters.get()
    if not num_semesters:
        messagebox.showwarning("Warning", "Please enter the number of semesters.")
        return False
    try:
        num_semesters = int(num_semesters)
        if num_semesters < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Warning", "Number of semesters must be a positive integer.")
        return False
    return True

def validate_terms():
    if not check_terms.get():
        messagebox.showwarning("Warning", "Please agree to the terms and conditions.")
        return False
    return True

def register_student():
    if (
        validate_name() and
        validate_title() and
        validate_age() and
        validate_nationality() and
        validate_registration_status() and
        validate_completed_courses() and
        validate_num_semesters() and
        validate_terms()
    ):
        name = entry_first_name.get() + " " + entry_last_name.get()
        num_semesters = entry_num_semesters.get()
        completed_courses = entry_completed_courses.get()
        registration_status = entry_registration_status.get()
        nationality = entry_nationality.get()
        age = entry_age.get()
        title = entry_title.get()
        
        save_student_info(name,title)
        messagebox.showinfo("Success", "Student registered successfully!")

root = Tk()
root.title("Student Registration System")

frame = ttk.Frame(root, padding="20")
frame.pack()

fieldset_one = ttk.Labelframe(frame, text="Fieldset")
fieldset_one.pack(pady=10)

label_first_name = ttk.Label(fieldset_one, text="First Name:")
label_first_name.grid(row=0, column=0, sticky=W, padx=10, pady=10)

entry_first_name = ttk.Entry(fieldset_one)
entry_first_name.grid(row=0, column=1)

label_last_name = ttk.Label(fieldset_one, text="Last Name:")
label_last_name.grid(row=0, column=2, sticky=W, padx=10, pady=10)

entry_last_name = ttk.Entry(fieldset_one)
entry_last_name.grid(row=0, column=3)

label_title = ttk.Label(fieldset_one, text="Title:")
label_title.grid(row=0, column=4, sticky=W, padx=10, pady=10)

entry_title = ttk.Combobox(fieldset_one, values=["MR", "MRS", "Dr"])
entry_title.grid(row=0, column=5)

label_age = ttk.Label(fieldset_one, text="Age:")
label_age.grid(row=1, column=0, sticky=W, padx=10, pady=10)

entry_age = ttk.Entry(fieldset_one)
entry_age.grid(row=1, column=1)

label_nationality = ttk.Label(fieldset_one, text="Nationality:")
label_nationality.grid(row=1, column=2, sticky=W, padx=10, pady=10)

entry_nationality = ttk.Combobox(fieldset_one, values=["USA", "UK", "Canada", "Australia", "India"])
entry_nationality.grid(row=1, column=3)

fieldset_two = ttk.Labelframe(frame, text="Fieldset 2")
fieldset_two.pack(pady=10)

label_registration_status = ttk.Label(fieldset_two, text="Registration status:")
label_registration_status.grid(row=0, column=0, sticky=W, padx=5, pady=5)

entry_registration_status = ttk.Combobox(fieldset_two, values=["Active", "Inactive"])
entry_registration_status.grid(row=0, column=1)

label_completed_courses = ttk.Label(fieldset_two, text="# Completed Courses:")
label_completed_courses.grid(row=0, column=2, sticky=W, padx=5, pady=5)

entry_completed_courses = ttk.Entry(fieldset_two)
entry_completed_courses.grid(row=0, column=3)

label_num_semesters = ttk.Label(fieldset_two, text="Number of Semesters:")
label_num_semesters.grid(row=1, column=0, sticky=W, padx=5, pady=5)

entry_num_semesters = ttk.Entry(fieldset_two)
entry_num_semesters.grid(row=1, column=1)

check_terms = BooleanVar()
check_terms.set(False)

check_terms_box = ttk.Checkbutton(frame, text="I agree to the terms and conditions", variable=check_terms)
check_terms_box.pack(padx=10, pady=10)

button_register = ttk.Button(root, text="Register", command=register_student)
button_register.pack(pady=10)

root.mainloop()
