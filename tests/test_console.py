#!/usr/bin/ỳthon3
"""test for the console"""

import unittest

from models.base_model import BaseModel

class TestConsole(unittest.TestCase):

    def test_class_docstring(self):
        """Test classes doctring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")   
