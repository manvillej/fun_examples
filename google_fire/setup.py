from setuptools import setup

setup(
    name='google_fire_package',
    entry_points={
        'console_scripts': [
            'hello = google_fire:main',
        ],
    }
)