"""
 Student Management System
"""
students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter student roll number: ")
    marks = int(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!\n")

    # View Students 
    
def view_students():
        if not students:
            print("No students found.\n")
            return
        
        for student in students:
            print("Name:", student["name"])
            print("Roll:", student["roll"])
            print("Marks:", student["marks"])
            print("-------------------")

    # Search Students 

def search_student():
        roll = input("Enter roll number to search: ")

        for student in students:
            
            if student["roll"] == roll:

              print("Student Found")
              print("Name:", student["name"])
              print("Marks:", student["marks"])
              return
            
        print("Student not found.\n")


    #Average Marks 

def average_marks():
        if not students:
            print("No students available,\n")
            return
        total = 0

        for student in students:
            total += student["marks"]
        
        avg = total / len(students)
        print("Average Marks:", avg, "\n")
    

    #Main menu 

while True:
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Average Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            average_marks()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")
        