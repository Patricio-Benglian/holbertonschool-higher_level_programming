#!/usr/bin/python3
"""
test module
"""
import unittest
from models.base import Base

class test_Base(unittest.TestCase):
    """
    tests and stuff
    """
    def test_is_instance(self):
        """Check if creates"""
        instance = Base()
        self.assertTrue(isinstance(instance, Base))
