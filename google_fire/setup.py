from setuptools import setup

setup(
    name='google_fire_package',
    entry_points={
        'console_scripts': [
            'hello = google_fire:simple_func',
            'calc = google_fire:simple_class',
            'counter = google_fire:complex_class',
        ],
    }
)