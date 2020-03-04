from setuptools import setup

setup(
    name='HappyTickets',
    version='1.0',
    py_modules=['hw1', 'ticket_generator'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        happytickets=hw1:cli
        gentickets=ticket_generator:main
    ''',
)