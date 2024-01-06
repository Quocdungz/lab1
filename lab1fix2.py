def input_number_of_students():
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            return num_students
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_student_information(num_students):
    students = {}
    for i in range(1, num_students + 1):
        id = str(i)
        name = input(f"Enter name for student {id}: ")
        dob = input(f"Enter DoB for student {id} (dd-mm-yyyy): ")
        students[id] = {'name': name, 'dob': dob, 'marks': {}}
    return students

def input_number_of_courses():
    while True:
        try:
            num_courses = int(input("Enter number of courses: "))
            return num_courses
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_course_information(num_courses):
    courses = {}
    for i in range(1, num_courses + 1):
        id = str(i)
        name = input(f"Enter name for course {id}: ")
        courses[id] = {'name': name}
    return courses

def select_course_and_enter_marks(students, courses, num_students, num_courses):
    for id, data in students.items():
        for course_id, course_data in courses.items():
            mark = float(input(f"Enter mark for student {id} in course {course_id}: "))
            data['marks'][course_id] = mark
    return students, courses

def list_courses(courses):
    print("\nCourses:")
    for id, data in courses.items():
        print(f"ID: {id}, Name: {data['name']}")

def list_students(students):
    print("\nStudents:")
    for id, data in students.items():
        print(f"ID: {id}, Name: {data['name']}, DOB: {data['dob']}")

def show_student_marks(students, courses):
    id = input("Enter student ID to show marks: ")
    if id in students:
        print(f"\nMarks for student {id}:")
        for course_id, course_data in courses.items():
            if course_id in students[id]['marks']:
                print(f"Course {course_id}, Name: {course_data['name']}: {students[id]['marks'][course_id]}")
            else:
                print(f"Course {course_id}, Name: {course_data['name']}: Not available")
    else:
        print("Invalid student ID.")

def main():
    num_students = input_number_of_students()
    students = input_student_information(num_students)

    num_courses = input_number_of_courses()
    courses = input_course_information(num_courses)

    students, courses = select_course_and_enter_marks(students, courses, num_students, num_courses)

    while True:
        print("\nOptions:")
        print("1. Courses List")
        print("2. Students List")
        print("3. Student Marks")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            show_student_marks(students, courses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()