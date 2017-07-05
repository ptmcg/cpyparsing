#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Constants for cPyparsing.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

#-----------------------------------------------------------------------------------------------------------------------
# CONSTANTS:
#-----------------------------------------------------------------------------------------------------------------------

pyparsing_version = "2.2.0"
development_version = "1"

version = pyparsing_version + "-post" + development_version

file_name = "cPyparsing.pyx"
wrap_call_line = "                ret = func(*args[limit:])\n"

#-----------------------------------------------------------------------------------------------------------------------
# UPDATE FILE:
#-----------------------------------------------------------------------------------------------------------------------


def update_file():
    """Update constants in main Cython file."""

    print("Updating " + file_name + " constants...")
    with open(file_name, "r+") as f:

        wrap_call_line_num = None
        for i, line in enumerate(f):
            if line == wrap_call_line:
                wrap_call_line_num = i + 1
        if wrap_call_line_num is None:
            raise Exception("failed to find " + repr(wrap_call_line) + " in " + file_name)

        f.seek(0)

        new_lines = []
        for line in f:
            if line.startswith("__version__ ="):
                line = "__version__ = " + repr(pyparsing_version) + "\n"
            elif line.startswith("_FILE_NAME ="):
                line = "_FILE_NAME = " + repr(file_name) + "\n"
            elif line.startswith("_WRAP_CALL_LINE_NUM ="):
                line = "_WRAP_CALL_LINE_NUM = " + repr(wrap_call_line_num) + "\n"
            new_lines.append(line)

        f.seek(0)
        f.truncate()
        f.write("".join(new_lines))

    print("Constants in " + file_name + " updated.")


if __name__ == "__main__":
    update_file()