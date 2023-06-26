#!/usr/bin/python3
"""
test module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class test_Base(unittest.TestCase):
    """
    tests and stuff
    """
    def test_is_instance(self):
        """Check if creates"""
        instance = Base()
        self.assertTrue(isinstance(instance, Base))

    def test_id(self):
        """checks id"""
        instance = Base(4)
        self.assertEqual(instance.id, 4)
