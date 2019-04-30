#!/usr/bin/env python3
"""PenIn setup script."""
from setuptools import setup, find_packages
from penin.core.version import get_version

VERSION = get_version()

readme_file = open('README.md', 'r')
LONG_DESCRIPTION = readme_file.read()
readme_file.close()

setup(
    name='penin',
    version=VERSION,
    description='Information gathering and penetration testing framework',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Fabian Affolter',
    author_email='fabian@affolter-engineering.ch',
    url='https://github.com/fabaff/penin',
    license='Apache 2.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'penin': ['templates/*']},
    include_package_data=True,
    install_requires=['cement', 'pyyaml', 'colorlog', 'jinja2', 'tinydb'],
    entry_points="""
        [console_scripts]
        penin = penin.main:main
    """,
)
