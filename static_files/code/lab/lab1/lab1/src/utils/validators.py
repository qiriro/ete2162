from typing import Union

def validate_grade(grade: Union[str, float]) -> bool:
    """Validate grade value"""
    try:
        grade_val = float(grade) if isinstance(grade, str) else grade
        return 0 <= grade_val <= 100
    except ValueError:
        return False

def validate_course_code(code: str) -> bool:
    """Validate course code"""
    return bool(code and code.strip())

def validate_course_name(name: str) -> bool:
    """Validate course name"""
    return bool(name and name.strip())