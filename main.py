from datetime import datetime

from model.student import Student
from utils import (
    print_list_of_students,
    get_list_of_platinum_alumni_students,
    print_hello_world,
    find_second_biggest,
)

def main():
    students = [
        Student(110001,
            "Dave",
            datetime.strptime("11/18/1951", "%m/%d/%Y")),
        
        Student(
            110002,
            "Anna",
            datetime.strptime("12/07/1990", "%m/%d/%Y")
        ),

        Student(
            110003,
            "Erica",
            datetime.strptime("01/31/1974", "%m/%d/%Y")
        ),

        Student(
            110004,
            "Carlos",
            datetime.strptime("08/22/2009", "%m/%d/%Y")
        ),

        Student(
            110005,
            "Bob",
            datetime.strptime("03/05/1990", "%m/%d/%Y")
        ),
    ]
    
    # Question 3.3
    print_list_of_students(students)

    # Question 3.4
    platinum = get_list_of_platinum_alumni_students(students)

    print("\n========== PLATINUM ALUMNI ==========\n")

    for student in platinum:
        print(student)

    # Question 3.5.1
    numbers = [5, 7, 10, 14, 35, 50, 70, 11]

    print_hello_world(numbers)

    # Question 3.5.2

    print("\n========== SECOND BIGGEST ==========\n")

    print(find_second_biggest([1, 2, 3, 4, 5]))
    print(find_second_biggest([19, 9, 11, 0, 12]))


if __name__ == "__main__":
    main()