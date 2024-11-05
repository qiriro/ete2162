from setuptools import setup, find_packages

setup(
    name="grade_manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
    ],
    author="Kizito Nkurikiyeyezu",
    description="A grade management system for students",
    keywords="education, grades, management",
    python_requires=">=3.8",
)