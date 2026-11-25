
# Course Eligibility Expert System

def check_eligibility(course, math, programming, english):

    if course == "computer_science":
        if math >= 60 and programming >= 65 and english >= 50:
            print("Student is eligible for Computer Science")
        else:
            print("Student is not eligible for Computer Science")

    elif course == "data_science":
        if math >= 70 and programming >= 60 and english >= 50:
            print("Student is eligible for Data Science")
        else:
            print("Student is not eligible for Data Science")

    elif course == "information_technology":
        if math >= 50 and programming >= 55 and english >= 50:
            print("Student is eligible for Information Technology")
        else:
            print("Student is not eligible for Information Technology")

    else:
        print("Invalid Course")


# Get student details
math = int(input("Enter Mathematics marks: "))
programming = int(input("Enter Programming marks: "))
english = int(input("Enter English marks: "))

course = input("Enter course name: ").lower()

# Check eligibility
check_eligibility(course, math, programming, english)
