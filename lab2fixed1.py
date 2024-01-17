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

    def input_number_of_students(self):
        while True:
            try:
                num_students = int(input("Enter number of students: "))
                return num_students
            except ValueError:
                print("Invalid input. Please enter a number.")

    def input_student_information(self, num_students):
        for i in range(1, num_students + 1):
            id = str(i)
            name = input(f"Enter name for student {id}: ")
            dob = input(f"Enter DoB for student {id} (dd-mm-yyyy): ")
            self.students[id] = Student(id, name, dob)

    def input_number_of_courses(self):
        while True:
            try:
                num_courses = int(input("Enter number of courses: "))
                return num_courses
            except ValueError:
                print("Invalid input. Please enter a number.")

    def input_course_information(self, num_courses):
        for i in range(1, num_courses + 1):
            id = str(i)
            name = input(f"Enter name for course {id}: ")
            self.courses[id] = Course(id, name)

    def select_course_and_enter_marks(self, num_students, num_courses):
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

    def show_student_marks(self, id):
        if id in self.students:
            print(f"\nMarks for student {id}:")
            for course_id, course in self.courses.items():
                if course_id in self.students[id].marks:
                    print(f"Course {course_id}, Name: {course.name}: {self.students[id].marks[course_id]}")
                else:
                    print(f"Course {course_id}, Name: {course.name}: Not available")
        else:
            print("Invalid student ID.")

    def main(self):
        num_students = self.input_number_of_students()
        self.input_student_information(num_students)

        num_courses = self.input_number_of_courses()
        self.input_course_information(num_courses)

        self.select_course_and_enter_marks(num_students, num_courses)

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
                id = input("Enter student ID to show marks: ")
                self.show_student_marks(id)
            elif choice == '4':
                break
            else:
                print("Invalid choice.")


if __name__ == '__main__':
    school = School()
    school.main()