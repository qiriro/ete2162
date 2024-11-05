import os
from typing import Dict

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_courses(courses: Dict):
    """Display formatted course data"""
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