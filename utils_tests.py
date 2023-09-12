import unittest
from utils import utils


class utilsTesting(unittest.TestCase):

    def testReversed(self):
        self.assertEqual(utils.reversed(12),21)
        self.assertEqual(utils.reversed(12.1), None)
        self.assertEqual(utils.reversed("1"), None)
    
    def testFormatter(self):
        self.assertEqual(utils.formatter(20),(bin(20), oct(20)))
        self.assertEqual(utils.formatter(12.1), None)
        self.assertEqual(utils.formatter("1"), None)
