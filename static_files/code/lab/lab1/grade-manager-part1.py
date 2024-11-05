import os
courses = {}
def display_menu():
    """
    Display the main menu options to the user.
    Uses simple print statements for clarity.
    """
    print("Welcome to Grade Manager v1.0\n")
    print("1. Add a new course")
    print("2. Add a grade to a course")
    print("3. Display all courses and grades")
    print("4. Exit")

def redisplay_menu(user_option):
    """
    Clear the screen and redisplay menu when invalid option is entered.
    Args:
        user_option: The invalid option that was entered
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{user_option} is an invalid option.\n Please try again.")
    display_menu()

def get_user_option():
    """
    Get and validate user's menu choice.
    Returns:
        str: The user's validated menu choice
    """
    user_option = input("\nPlease enter your option: ")
    if user_option not in ["1", "2", "3", "4"]:
        redisplay_menu(user_option)
        return get_user_option()
    return user_option

def add_course():
    """
    Add a new course to the courses dictionary.
    Handles input validation for course code and name.
    """
    course_code = input("Enter course code: ").strip()
    # Validate course code
    if not course_code:
        print("Course code cannot be empty!")
        return
    if course_code in courses:
        print("Course already exists!")
        return
    
    course_name = input("Enter course name: ").strip()
    # Validate course name
    if not course_name:
        print("Course name cannot be empty!")
        return
    
    # Create new course entry with empty grade lists
    courses[course_code] = {
        'course_name': course_name,
        'quizzes': [],
        'cats': [],
        'final_exam': None
    }
    print(f"\nCourse {course_code} ({course_name}) added successfully!")

def validate_grade(grade_str):
    """
    Validate that a grade is a number between 0 and 100.
    Args:
        grade_str: The grade input string to validate
    Returns:
        float or None: The validated grade as a float, or None if invalid
    """
    try:
        grade = float(grade_str)
        if 0 <= grade <= 100:
            return grade
        print("Grade must be between 0 and 100!")
        return None
    except ValueError:
        print("Grade must be a number!")
        return None

def add_grade():
    """
    Add a grade to an existing course.
    Handles input validation for course code, grade type, and grade value.
    """
    if not courses:
        print("No courses exist! Please add a course first.")
        return
    
    course_code = input("Enter course code: ").strip()
    if course_code not in courses:
        print("Course not found!")
        return
    
    grade_type = input("Enter grade type (quiz/cat/final): ").lower().strip()
    if grade_type not in ['quiz', 'cat', 'final']:
        print("Invalid grade type! Must be quiz, cat, or final.")
        return
    
    grade_str = input("Enter grade (0-100): ")
    grade = validate_grade(grade_str)
    if grade is None:
        return
    
    # Add grade to appropriate list/field
    if grade_type == 'quiz':
        courses[course_code]['quizzes'].append(grade)
    elif grade_type == 'cat':
        courses[course_code]['cats'].append(grade)
    else:  # final
        courses[course_code]['final_exam'] = grade
    
    print(f"\nGrade added successfully to {course_code}!")

def display_courses():
    """
    Display all courses and their grades in a formatted way.
    Handles empty course list and formatting of grade displays.
    """
    if not courses:
        print("\nNo courses exist!")
        return
    
    print("\nCurrent Courses and Grades:")
    print("-" * 50)
    for code, data in courses.items():
        print(f"\nCourse: {code} ({data['course_name']})")
        print(f"Quizzes: {data['quizzes']}")
        print(f"CATs: {data['cats']}")
        print(f"Final Exam: {data['final_exam']}")
    print("-" * 50)

def start_program():
    """
    Main program loop that handles menu navigation and user interaction.
    Continues until user chooses to exit.
    """
    while True:
        display_menu()
        option = get_user_option()
        
        if option == "1":
            add_course()
        elif option == "2":
            add_grade()
        elif option == "3":
            display_courses()
        elif option == "4":
            print("\nThank you for using Grade Manager v1.0!")
            break
        
        input("\nPress Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    start_program()
