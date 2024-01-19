class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_mark(self, course_id, mark):
        self.marks[course_id] = mark


class School:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_number(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def input_student_information(self):
        num_students = self.input_number("Enter number of students: ")
        for i in range(1, num_students + 1):
            id = str(i)
            name = input(f"Enter name for student {id}: ")
            dob = input(f"Enter DoB for student {id} (dd-mm-yyyy): ")
            self.students[id] = Student(id, name, dob)

    def input_course_information(self):
        num_courses = self.input_number("Enter number of courses: ")
        for i in range(1, num_courses + 1):
            id = str(i)
            name = input(f"Enter name for course {id}: ")
            self.courses[id] = Course(id, name)

    def select_course_and_enter_marks(self):
        for id, student in self.students.items():
            for course_id, course in self.courses.items():
                mark = float(input(f"Enter mark for student {id} in course {course_id}: "))
                student.add_mark(course_id, mark)

    def list_courses(self):
        print("\nCourses:")
        for id, course in self.courses.items():
            print(f"ID: {id}, Name: {course.name}")

    def list_students(self):
        print("\nStudents:")
        for id, student in self.students.items():
            print(f"ID: {id}, Name: {student.name}, DOB: {student.dob}")

    def show_student_marks(self):
        id = input("Enter student ID to show marks: ")
        if id in self.students:
            print(f"\nMarks for student {id}:")
            for course_id, course in self.courses.items():
                mark = self.students[id].marks.get(course_id, "Not available")
                print(f"Course {course_id}, Name: {course.name}: {mark}")
        else:
            print("Invalid student ID.")

    def menu(self):
        while True:
            print("\nOptions:")
            print("1. Courses List")
            print("2. Students List")
            print("3. Student Marks")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.list_courses()
            elif choice == '2':
                self.list_students()
            elif choice == '3':
                self.show_student_marks()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def run(self):
        self.input_student_information()
        self.input_course_information()
        self.select_course_and_enter_marks()
        self.menu()


if __name__ == '__main__':
    school = School()
    school.run()