from datetime import datetime

def print_list_of_students(students):
    """
    Prints students in order by name
    """
    
    print("\n ================= All students ===================== \n")
    for student in sorted(students, key=lambda s:s.name):
        print(student)
    
def get_list_of_platinum_alumni_students(students):
    """
    Students admitted at least 30 years ago.
    Returned in descending order of admission date.
    """
    
    current_year = datetime.today().year
    
    platnum = [
        s for s in students
        if current_year - s.date_of_admission.year >=30
    ]
    
    platnum.sort(key=lambda s:s.date_of_admission,
                 reverse=True)
    
    return platnum

def print_hello_world(numbers):
    """
    Prints Hello, World or HelloWorld
    """
    
    print("\n========== HELLO WORLD ==========\n")
    
    for num in numbers:
        if num % 35 == 0:
            print(f"{num} -> HelloWorld")

        elif num % 5 == 0:
            print(f"{num} -> Hello")

        elif num % 7 == 0:
            print(f"{num} -> World")
            
def find_second_biggest(numbers):
    """
    Find second largest WITHOUT sorting.
    """
    
    if len(numbers)<2:
        return None
    
    largest = float("-inf")
    second  = float("-inf")
    
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        
        elif largest>num>second:
            second = num
            
    return second