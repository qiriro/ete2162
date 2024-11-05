import pytest
from src.core.grade_manager import GradeManager

@pytest.fixture
def course_data():
    return {
        'course_name': 'Test Course',
        'quizzes': [],
        'cats': [],
        'final_exam': None
    }

def test_add_grade(course_data):
    assert GradeManager.add_grade(course_data, 'quiz', 85) == True
    assert len(course_data['quizzes']) == 1
    assert course_data['quizzes'][0] == 85

def test_invalid_grade(course_data):
    assert GradeManager.add_grade(course_data, 'quiz', -1) == False
    assert GradeManager.add_grade(course_data, 'quiz', 101) == False
    assert len(course_data['quizzes']) == 0