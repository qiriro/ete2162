import pytest
from src.core.course_manager import CourseManager

def test_add_course():
    manager = CourseManager()
    assert manager.add_course("CS101", "Intro to Programming") == True
    assert manager.add_course("", "Invalid Course") == False
    assert manager.add_course("CS101", "Duplicate Code") == False

def test_get_course():
    manager = CourseManager()
    manager.add_course("CS101", "Intro to Programming")
    
    course = manager.get_course("CS101")
    assert course is not None
    assert course['course_name'] == "Intro to Programming"
    assert course['quizzes'] == []
    assert course['cats'] == []
    assert course['final_exam'] is None
