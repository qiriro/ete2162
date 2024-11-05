from typing import List, Optional, Union
from ..utils.validators import validate_grade

class GradeManager:
    """Manages grade-related operations"""
    
    @staticmethod
    def add_grade(course_data: dict, grade_type: str, grade: float) -> bool:
        """
        Add a grade to a course
        
        Args:
            course_data: Course dictionary
            grade_type: Type of grade (quiz/cat/final)
            grade: Grade value
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not validate_grade(grade):
            return False
            
        if grade_type == 'quiz':
            course_data['quizzes'].append(grade)
        elif grade_type == 'cat':
            course_data['cats'].append(grade)
        elif grade_type == 'final':
            course_data['final_exam'] = grade
        else:
            return False
            
        return True