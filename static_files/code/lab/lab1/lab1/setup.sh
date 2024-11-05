#!/bin/bash

# Create main project directory
mkdir -p grade_manager

# Create the directory structure
cd grade_manager

# Create root level files
touch README.md
touch requirements.txt
touch setup.py

# Create src directory and its __init__.py
mkdir -p src
touch src/__init__.py

# Create core directory and its files
mkdir -p src/core
touch src/core/__init__.py
touch src/core/course_manager.py
touch src/core/grade_manager.py

# Create utils directory and its files
mkdir -p src/utils
touch src/utils/__init__.py
touch src/utils/validators.py
touch src/utils/display.py

# Create cli directory and its files
mkdir -p src/cli
touch src/cli/__init__.py
touch src/cli/menu.py

# Create tests directory and its files
mkdir -p tests
touch tests/__init__.py
touch tests/test_course_manager.py
touch tests/test_grade_manager.py
touch tests/test_validators.py

# Print success message
echo "Grade Manager project structure has been created successfully!"
echo "Project structure:"
tree grade_manager

# Make the script executable
chmod +x setup.sh
