"""
Setting up Pyssemble as library
"""
from setuptools import setup, find_packages

setup(
    name='Pyssemble',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'parse_assemble = Pyssemble.parser:parse',
        ],
    },
)
