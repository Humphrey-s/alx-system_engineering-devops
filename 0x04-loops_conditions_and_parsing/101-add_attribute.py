#!/usr/bin/python3
"""definition add_attribute"""


def add_attribute(prmObject, prmName, prmValue):
    """adds a new attribute to an object"""

    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")

    if (not hasattr(prmObject, prmName)):
        prmObject.__setattr__(prmName, prmValue)
