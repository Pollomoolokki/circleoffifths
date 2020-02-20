#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='circleoffifths',
    version='1.0.0',
    author='%{AUTHOR}',
    author_email='%{EMAIL}',
    description='%{DESCRIPTION}',
    url='%{URL}',
    entry_points={
        'console_scripts': ['circleoffifths = circleoffifths.main:main'],
    },
    packages=find_packages(),
)
