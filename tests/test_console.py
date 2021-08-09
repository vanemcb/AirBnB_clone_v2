#!/usr/bin/python3
""" """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ """

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"vane\"")
        state_id = f.getvalue()
        self.assertTrue(len(state_id) >= 1)

        with patch('sys.stdout', new=StringIO()) as f2:
            HBNBCommand().onecmd("show State " + state_id)
        string = f2.getvalue()
        param = "'name': 'vane'"
        self.assertTrue(param in string)
