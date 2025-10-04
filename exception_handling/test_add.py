from exercise_4 import square
import unittest

class TextSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(5), 25)



