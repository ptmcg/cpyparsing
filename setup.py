#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Installer for cPyparsing.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys
import os.path
import setuptools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from constants import (
    version,
    file_name,
    base_name,
    c_name,
)

#-----------------------------------------------------------------------------------------------------------------------
# SETUP:
#-----------------------------------------------------------------------------------------------------------------------

try:
    from Cython.Build import cythonize
except ImportError:
    ext_modules = [setuptools.Extension(base_name, [c_name])]
else:
    ext_modules = cythonize(
        str(file_name),
        compiler_directives={
            "language_level": 3,
            "overflowcheck": True,
            "cdivision": True,
            "infer_types": True,
        },
    )

setuptools.setup(
    name=base_name,
    version=version,
    ext_modules=ext_modules,
    include_package_data=True,
    description="Cython implementation of PyParsing for use in Coconut.",
    url="https://github.com/evhub/cpyparsing",
    author="Evan Hubinger",
    author_email="evanjhub@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
    ],
    document_names={
        "description": "README.md",
        "license": "LICENSE.txt",
    },
)
