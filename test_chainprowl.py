# test_chainprowl.py
"""
Tests for ChainProwl module.
"""

import unittest
from chainprowl import ChainProwl

class TestChainProwl(unittest.TestCase):
    """Test cases for ChainProwl class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = ChainProwl()
        self.assertIsInstance(instance, ChainProwl)

    def test_run_method(self):
        """Test the run method."""
        instance = ChainProwl()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
