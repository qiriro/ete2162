#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Grade Manager Test Runner${NC}\n"

# Function to run tests with a header
run_test() {
    echo -e "${GREEN}$1${NC}"
    echo "----------------------------------------"
    $2
    echo -e "\n"
}

# Run all tests
run_test "Running all tests:" "python -m pytest tests/"

# Run tests with verbose output
run_test "Running tests with verbose output:" "python -m pytest -v tests/"

# Run specific test file
run_test "Running course manager tests:" "python -m pytest tests/test_course_manager.py"

# Run with coverage
run_test "Running tests with coverage:" "python -m pytest --cov=src tests/"

# Run with detailed coverage report
run_test "Running tests with detailed coverage:" \
"python -m pytest --cov=src --cov-report=term-missing tests/"
