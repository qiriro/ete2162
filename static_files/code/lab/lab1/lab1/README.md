# Grade Manager

A simple command-line application for managing student grades.
This is part 1 for the course on Python programming

# Features

- Add and manage courses
- Record and track different types of grades (quizzes, CATs, final exams)
- View all courses and grades in a formatted display
- Input validation and error handling

# Usage

1. Run the application:
```bash
python -m src.cli.menu
```

# Development

1. Running all tests
```bash
python -m pytest tests/

# You can also run it in a verbose mode
python -m pytest -v tests/
```

2. Run specific test
```bash
# Run just the course manager tests
python -m pytest tests/test_course_manager.py

# Run just the grade manager tests
python -m pytest tests/test_grade_manager.py

# Install pytest-cov if not already installed
pip install pytest-cov

# Run tests with coverage
python -m pytest --cov=src tests/

# For a detailed coverage report
python -m pytest --cov=src --cov-report=term-missing tests/

# Run tests with coverage report

```


### Project Structure

- `src/core/`: Core business logic
- `src/utils/`: Utility functions and helpers
- `src/cli/`: Command-line interface
- `tests/`: Test files
