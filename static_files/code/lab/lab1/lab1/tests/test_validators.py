import pytest
from src.utils.validators import validate_grade, validate_course_code, validate_course_name

def test_validate_grade():
    assert validate_grade(85) == True
    assert validate_grade("85") == True
    assert validate_grade(-1) == False
    assert validate_grade(101) == False
    assert validate_grade("abc") == False

def test_validate_course_code():
    assert validate_course_code("CS101") == True
    assert validate_course_code("") == False
    assert validate_course_code("  ") == False

def test_validate_course_name():
    assert validate_course_name("Introduction to Programming") == True
    assert validate_course_name("") == False
    assert validate_course_name("  ") == False