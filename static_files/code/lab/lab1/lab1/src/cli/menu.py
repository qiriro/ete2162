from ..core.course_manager import CourseManager
from ..core.grade_manager import GradeManager
from ..utils.display import clear_screen, display_courses
from ..utils.validators import validate_grade

def display_menu():
    """Display main menu"""
    print("Welcome to Grade Manager v1.0\n")
    print("1. Add a new course")
    print("2. Add a grade to a course")
    print("3. Display all courses and grades")
    print("4. Exit")

def main():
    """Main program loop"""
    course_manager = CourseManager()
    grade_manager = GradeManager()
    
    while True:
        display_menu()
        choice = input("\nPlease enter your option: ")
        
        if choice == "1":
            code = input("Enter course code: ").strip()
            name = input("Enter course name: ").strip()
            if course_manager.add_course(code, name):
                print("Course added successfully!")
            else:
                print("Failed to add course!")
                
        elif choice == "2":
            code = input("Enter course code: ").strip()
            course = course_manager.get_course(code)
            if not course:
                print("Course not found!")
                continue
                
            grade_type = input("Enter grade type (quiz/cat/final): ").lower()
            grade = input("Enter grade (0-100): ")
            
            if grade_manager.add_grade(course, grade_type, float(grade)):
                print("Grade added successfully!")
            else:
                print("Failed to add grade!")
                
        elif choice == "3":
            display_courses(course_manager.get_all_courses())
            
        elif choice == "4":
            print("\nThank you for using Grade Manager!")
            break
            
        input("\nPress Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()