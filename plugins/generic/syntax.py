#!/usr/bin/env python2

"""
Copyright (c) 2006-2013 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import re

from lib.core.exception import SqlmapUndefinedMethod

class Syntax:
    """
    This class defines generic syntax functionalities for plugins.
    """

    def __init__(self):
        pass

    @staticmethod
    def _escape(expression, quote=True, escaper=None):
        retVal = expression

        if quote:
            for item in re.findall(r"'[^']*'+", expression, re.S):
                retVal = retVal.replace(item, escaper(item[1:-1]))
        else:
            retVal = escaper(expression)

        return retVal

    @staticmethod
    def escape(expression, quote=True):
        errMsg = "'escape' method must be defined "
        errMsg += "inside the specific DBMS plugin"
        raise SqlmapUndefinedMethod(errMsg)
