
# Student Data Management System

class Student:
    def __init__(self, name, roll_number, course, grade):
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number, course, grade):
        self.students[roll_number] = Student(name, roll_number, course, grade)
        print(f"Student {name} added successfully!")

    def delete_student(self, roll_number):
        if roll_number in self.students:
            del self.students[roll_number]
            print(f"Student with roll number {roll_number} deleted successfully!")
        else:
            print(f"Student with roll number {roll_number} not found!")

    def update_student(self, roll_number, name=None, course=None, grade=None):
        if roll_number in self.students:
            if name:
                self.students[roll_number].name = name
            if course:
                self.students[roll_number].course = course
            if grade:
                self.students[roll_number].grade = grade
            print(f"Student with roll number {roll_number} updated successfully!")
        else:
            print(f"Student with roll number {roll_number} not found!")

    def search_student(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print(f"Course: {student.course}")
            print(f"Grade: {student.grade}")
        else:
            print(f"Student with roll number {roll_number} not found!")

    def display_students(self):
        if self.students:
            for student in self.students.values():
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll_number}")
                print(f"Course: {student.course}")
                print(f"Grade: {student.grade}\n")
        else:
            print("No students in the database!")

def main():
    database = StudentDatabase()

    while True:
        print("\nStudent Data Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            roll_number = input("Enter student's roll number: ")
            course = input("Enter student's course: ")
            grade = input("Enter student's grade: ")
            database.add_student(name, roll_number, course, grade)
        elif choice == "2":
            roll_number = input("Enter student's roll number: ")
            database.delete_student(roll_number)
        elif choice == "3":
            roll_number = input("Enter student's roll number: ")
            name = input("Enter new name (optional): ")
            course = input("Enter new course (optional): ")
            grade = input("Enter new grade (optional): ")
            database.update_student(roll_number, name or None, course or None, grade or None)
        elif choice == "4":
            roll_number = input("Enter student's roll number: ")
            database.search_student(roll_number)
        elif choice == "5":
            database.display_students()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


