#!/usr/bin/python3
""" This module tests our console"""
import os
from io import StringIO
import unittest
from console import HBNBCommand
from unittest.mock import patch


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

    def test_create(self):
        """ Testing create method """
        with patch('sys.stdout', new=StringIO()) as mock:
            self.consola1.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", mock.getvalue())
