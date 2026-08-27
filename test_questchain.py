# test_questchain.py
"""
Tests for QuestChain module.
"""

import unittest
from questchain import QuestChain

class TestQuestChain(unittest.TestCase):
    """Test cases for QuestChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuestChain()
        self.assertIsInstance(instance, QuestChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuestChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
