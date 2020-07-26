import unittest
from src.Asrar.babil_yassar import *

class BabilYassarTest(unittest.TestCase):

    def test_iftakhly(self):
        babilYassar = BabilYassar()
        result = babilYassar.iftakhly()
        self.assertEqual(0, result)