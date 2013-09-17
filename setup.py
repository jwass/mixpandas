#!/usr/bin/env python

from distutils.core import setup

setup(
    name='mixpandas',
    version='0.0.1',
    author="Jacob Wasserman",
    author_email="jwasserman@gmail.com",
    py_modules=["mixpandas"],
    url="https://github.com/jwass/mixpandas",
    description="A library to read event data from Mixpanel's Raw Data Export API",
    requires=["pandas"],
    long_description=open('README.md').read(),
    classifiers=[
    ],
)
