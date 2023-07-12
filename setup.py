"""
Setup script for PyResponse package.
"""

from setuptools import setup, find_packages

setup(
    name='Pyresponse',
    version='0.1.0',
    description='Package for creating success and error responses in Python Projects',
    author='Ibrahim Oluwapeluwa',
    author_email='ipeluwa@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
        'rollbar',
        'sentry-sdk',
        'python-dotenv',
        'pydantic',
        'marshmallow'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
