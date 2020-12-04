# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="advent2020",
    version="0.1.0",
    description="advent2020 solutions",
    long_description=readme,
    author="Gustaf Hallberg",
    author_email="ghallberg@gmail.com",
    url="https://github.com/ghallberg/advent2020",
    license=license,
    packages=find_packages(exclude=("tests")),
)
