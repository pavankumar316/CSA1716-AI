
# Course Registration Database

# Student facts
students = {
    101: "john",
    102: "david",
    103: "alice",
    104: "peter"
}

# Course facts
courses = {
    "c101": "python",
    "c102": "java",
    "c103": "artificial_intelligence"
}

# Faculty facts
faculty = {
    "f1": "ramesh",
    "f2": "kumar",
    "f3": "priya"
}

# Enrolment facts
enrolments = [
    (101, "c101"),
    (102, "c101"),
    (103, "c102"),
    (104, "c103"),
    (103, "c101")
]

# Function to find students in a course
def students_in_course(course_name):

    found = False

    for student_id, course_id in enrolments:

        if courses[course_id] == course_name:
            print("Student:", students[student_id])
            found = True

    if not found:
        print("No students enrolled in this course")


# Display course registration details
print("Available Courses:")
for course in courses.values():
    print(course)

# Get course name
course_name = input("\nEnter course name: ").lower()

# Find enrolled students
print("\nStudents enrolled in", course_name, ":")
students_in_course(course_name)
