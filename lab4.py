# domains/course.py
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# domains/student.py
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark

# input.py
def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_text(prompt):
    return input(prompt)

# output.py
import curses

def curses_output(stdscr, message):
    stdscr.addstr(message)
    stdscr.refresh()
    stdscr.getch()

# main.py
from domains.student import Student
from domains.course import Course
import input
import output

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_number_of_students(self):
        return input.input_number("Enter number of students: ")

    def input_student_information(self, num_students):
        for i in range(1, num_students + 1):
            id = str(i)
            name = input.input_text(f"Enter name for student {id}: ")
            dob = input.input_text(f"Enter DoB for student {id} (dd-mm-yyyy): ")
            self.students[id] = Student(id, name, dob)

    def input_number_of_courses(self):
        return input.input_number("Enter number of courses: ")

    def input_course_information(self, num_courses):
        for i in range(1, num_courses + 1):
            id = str(i)
            name = input.input_text(f"Enter name for course {id}: ")
            self.courses[id] = Course(id, name)

    def main(self):
        try:
            num_students = self.input_number_of_students()
            self.input_student_information(num_students)

            num_courses = self.input_number_of_courses()
            self.input_course_information(num_courses)

            # Example usage of curses_output
            curses_output(stdscr, "Information entered successfully.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    school = School()
    school.main()
