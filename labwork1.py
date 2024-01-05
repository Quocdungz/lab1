# Create classes
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}

students = {}  # Dictionary to store students
courses = {}  # Dictionary to store courses

# Function to add student to the class
def add_student(id, name, dob):
    students[id] = Student(id, name, dob)

# Function to add course to the class
def add_course(id, name):
    courses[id] = Course(id, name)

# Function to enroll a student in a course
def enroll_student(student_id, course_id, marks):
    if student_id in students and course_id in courses:
        students[student_id].courses[course_id] = marks
        courses[course_id].students[student_id] = marks

# Function to list courses
def list_courses():
    for course in courses.values():
        print(f"Course ID: {course.id}, Course Name: {course.name}")

# Function to list students
def list_students():
    for student in students.values():
        print(f"Student ID: {student.id}, Student Name: {student.name}, Date of Birth: {student.dob}")

# Function to show student marks for a given course
def show_student_marks(student_id, course_id):
    if student_id in students and course_id in courses:
        print(f"Marks of student ID {student_id} in course ID {course_id}: {students[student_id].courses[course_id]}")
    else:
        print("Invalid Student ID or Course ID.")

# Testing
add_student(1, "Hiep", "2003-01-01")
add_student(2, "Ha", "2003-02-02")
add_student(3, "Phuong", "2024-29-2")
add_course(1.001, "Calculus I")
add_course(1.002, "Linear I")
enroll_student(1, 1.001, 85)
enroll_student(1, 1.002, 90)
enroll_student(2, 1.001, 95)
enroll_student(2, 1.002, 80)
enroll_student(3, 1.001, 80)
enroll_student(3, 1.002, 50)
list_courses()
list_students()
show_student_marks(1, 1.001)
show_student_marks(2, 1.002)
show_student_marks(3, 1.002)