#!/usr/bin/python3
""" This module tests our console"""
import os
from io import StringIO
import unittest
from console import HBNBCommand
from unittest.mock import patch
import pep8


class TestConsole(unittest.TestCase):
    """This class tests our console"""
    @classmethod
    def setUpClass(self):
        """ Sets the class for testing"""
        self.consola1 = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """ This deletes the class we created """
        del self.consola1

    def test_do_create(self):
        """ Testing create method """
        with patch('sys.stdout', new=StringIO()) as mock:
            self.consola1.onecmd("create State numb=2")
            self.assertTrue(len(mock.getvalue()) >= 1)

        with patch('sys.stdout', new=StringIO()) as mock2:
            self.consola1.onecmd("show State " + mock.getvalue())
            self.assertTrue("numb" in mock2.getvalue())
     def test_pep8(self):
        """Test Pep8 styling."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, "fix Pep8")

