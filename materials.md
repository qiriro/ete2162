---
layout: page
title: Course Materials && Resources
permalink: /materials/
---


## Required Textbook
   {% assign book = site.data.books.required %}
   <div class="card mb-3">
     <div class="row g-0">
       <div class="col-md-4">
         <img src="{{ book.image | relative_url }}" class="img-fluid rounded-start" alt="{{ book.title }} Cover">
       </div>
       <div class="col-md-8">
         <div class="card-body">
           <h5 class="card-title">{{ book.title }}</h5>
           <p class="card-text">
             <strong>Author:</strong> {{ book.author }}<br>
             <strong>ISBN:</strong> {{ book.isbn }}<br>
             <strong>Publisher:</strong> {{ book.publisher }} ({{ book.year }})
           </p>
           <a href="{{ book.link }}" class="btn btn-primary">More info</a>
         </div>
       </div>
     </div>
   </div>

## Suggested Textbooks
   
<div class="card mb-3">
   {% for book in site.data.books.suggested %}
    <div class="row g-0">
       <div class="col-md-4">
         <img src="{{ book.image | relative_url }}" class="img-fluid rounded-start" alt="{{ book.title }} Cover">
       </div>
       <div class="col-md-8">
         <div class="card-body">
           <h5 class="card-title">{{ book.title }}</h5>
           <p class="card-text">
             <strong>Author:</strong> {{ book.author }}<br>
             <strong>ISBN:</strong> {{ book.isbn }}<br>
             <strong>Publisher:</strong> {{ book.publisher }} ({{ book.year }})
           </p>
           <a href="{{ book.link }}" class="btn btn-primary">More info</a>
         </div>
       </div>
     </div>
   {% endfor %}
   </div>

## Online Documentation

- [Official Python Documentation](https://docs.python.org/3/) - The official and most comprehensive source of Python documentation.
- [Python Wiki](https://wiki.python.org/moin/) - A collaborative space for Python documentation and community resources.
- [Real Python](https://realpython.com/) - Tutorials and articles on Python programming.

## Free online courses 
- [Harvard's Introduction to Python](https://cs50.harvard.edu/python/2022/)
- [Introduction to Python](https://profound.academy/python-introduction) - In this course, you will learn a lot about the language and programming in general.
- [Codecademy](https://www.codecademy.com/learn/learn-python-3) - Interactive Python courses for beginners.
- [Coursera](https://www.coursera.org/courses?query=python) - Python courses from top universities and institutions.
- [edX](https://www.edx.org/learn/python) - Python programming courses from various universities.
- [Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)
- [Python Programming MOOC ](https://programming-24.mooc.fi/) - This is the course material page for the Introduction to Programming course and the Advanced Course in Programming from the Department of Computer Science at the University of Helsinki.

## YouTube Channels
- [Python Tutorial - Python Full Course for Beginners](https://youtu.be/_uQrJ0TkZlc?si=BXzavVfLhGLTD5jS)
- [Corey Schafer](https://www.youtube.com/user/schafer5) - Python tutorials and programming tips.
- [Programming with Mosh](https://www.youtube.com/user/programmingwithmosh) - Python tutorials for beginners and advanced learners.
- [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) - Python tutorials and projects.

## GitHub Repositories

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) - A collection of algorithms and data structures implemented in Python.
- [vinta/awesome-python](https://github.com/vinta/awesome-python) - A curated list of awesome Python frameworks, libraries, software, and resources.
- [realpython/materials](https://github.com/realpython/materials) - Code samples and materials from Real Python tutorials.

## Online IDEs and Notebooks

- [Repl.it](https://repl.it/~) - An online IDE for Python and other programming languages.
- [Google Colab](https://colab.research.google.com/) - A free Jupyter notebook environment that runs in the cloud.
- [Jupyter Notebook](https://jupyter.org/) - An open-source web application for creating and sharing documents with live code.

## Practice Platforms

- [LeetCode](https://leetcode.com/) - Coding challenges and interview preparation.
- [HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-python) - Python challenges and competitions.
- [Codewars](https://www.codewars.com/) - Coding challenges to improve your skills.

## Python-Related Blogs and Websites

- [Real Python](https://realpython.com/) - Tutorials, articles, and resources for Python developers.
- [Python Insider](https://blog.python.org/) - Official blog of the Python Software Foundation.
- [Mouse Vs Python](https://www.blog.pythonlibrary.org/) - Python tutorials and articles.

## Community Forums

- [Stack Overflow Python Tag](https://stackoverflow.com/questions/tagged/python) - A community of Python developers answering questions and sharing knowledge.
- [Reddit r/learnpython](https://www.reddit.com/r/learnpython/) - A subreddit for Python learners.
- [Python Discord](https://pythondiscord.com/) - A large community of Python enthusiasts.

## Additional Books

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart - Practical programming for total beginners.
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python/9781491946237/) by Luciano Ramalho - Clear, concise, and effective programming.
- [Python for Data Analysis](https://www.oreilly.com/library/view/python-for-data/9781491957653/) by Wes McKinney - Data wrangling with Pandas, NumPy, and IPython.

## Python Package Index (PyPI)

- [PyPI](https://pypi.org/) - The Python Package Index is a repository of software for the Python programming language.

## Version Control Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - A comprehensive guide to Git.
- [GitHub Learning Lab](https://lab.github.com/) - Interactive courses to learn Git and GitHub.
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) - Tutorials and guides for using Git.

## Python Style Guide

- [PEP 8](https://www.python.org/dev/peps/pep-0008/) - The official style guide for Python code.