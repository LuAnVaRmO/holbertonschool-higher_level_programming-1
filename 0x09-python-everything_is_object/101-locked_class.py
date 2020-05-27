#!/usr/bin/python3
"""
Module with a class LockedClass with no class or object attribute
"""


class LockedClass:
    """
    Class that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
