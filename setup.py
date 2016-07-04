from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name         = 'FaBo9Axis_MPU9250',
    version      = '1.0.0',
    author       = 'FaBo',
    author_email = 'info@fabo.io',
    description  = "This is a library for the FaBo 9AXIS I2C Brick.",
    url          = 'https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python/',
    license      = 'MIT',
    classifiers  = classifiers,
    packages     = find_packages()
)
