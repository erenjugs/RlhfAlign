# test_rlhfalign.py
"""
Tests for RlhfAlign module.
"""

import unittest
from rlhfalign import RlhfAlign

class TestRlhfAlign(unittest.TestCase):
    """Test cases for RlhfAlign class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RlhfAlign()
        self.assertIsInstance(instance, RlhfAlign)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RlhfAlign()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
