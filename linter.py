#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sergiy Kulanov,,,
# Copyright (c) 2017 Sergiy Kulanov,,,
#
# License: MIT
#

"""This module exports the Terraformlint plugin class."""

from SublimeLinter.lint import Linter, util


class Terraformlint(Linter):
    """Provides an interface to terraformlint."""

    syntax = 'terraform'
    cmd = 'terraform validate'
    executable = None
    regex = (
        r'(?P<error>^Error).+?: At (?P<line>\d+):(?P<col>\d+): (?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
