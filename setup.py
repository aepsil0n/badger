#!/usr/bin/env python
"""
Setup script for badger

"""

from setuptools import setup


if __name__ == '__main__':
    setup(
        name='badger',
        version='0.1.0',
        description='',
        author='Eduard Bopp',
        author_email='eduard.bopp@aepsil0n.de',
        packages=['badger'],
        install_requires=['docopt'],
    )
