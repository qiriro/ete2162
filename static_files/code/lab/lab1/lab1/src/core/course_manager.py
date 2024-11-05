from typing import Dict, Optional

class CourseManager:
    """Manages course-related operations"""
    
    def __init__(self):
        self.courses: Dict = {}

    def add_course(self, code: str, name: str) -> bool:
        """
        Add a new course to the system
        
        Args:
            code: Course code
            name: Course name
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not code or not name:
            return False
            
        if code in self.courses:
            return False
            
        self.courses[code] = {
            'course_name': name,
            'quizzes': [],
            'cats': [],
            'final_exam': None
        }
        return True

    def get_course(self, code: str) -> Optional[Dict]:
        """Get course data by code"""
        return self.courses.get(code)

    def get_all_courses(self) -> Dict:
        """Get all courses"""
        return self.courses