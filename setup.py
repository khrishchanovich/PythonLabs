from setuptools import setup, find_packages

setup(
    name='Lab3',
    version='1.0.0',
    packages=find_packages(include=['Lab3', 'Lab3.*', 'main.py']),
    install_requires=['argparse'],
    entry_points={
        'console_scripts': [
            'my_util=lib_for_lab3.cli:main',
        ],
    },
)
