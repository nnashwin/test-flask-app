import json
import unittest

from parsenames import toJson

class TestParseNames(unittest.TestCase):
    def test_toJson(self):
        #
        # Test that it converts a list of strings to json
        #
        strList = ['cool_apple', 'thatApple', 'cool_orange', 'thatOrange', 'cool_banana', 'cool_kiwi', 'thatKiwi', 'alaska']
        expected = json.dumps({'cool_': ['cool_apple', 'cool_orange', 'cool_banana', 'cool_kiwi'], 'that': ['thatApple', 'thatOrange', 'thatKiwi'], 'alaska': ['alaska']})
        self.assertEqual(toJson(strList), expected)

if __name__ == "__main__":
    unittest.main()
    print("Everything has passed")
