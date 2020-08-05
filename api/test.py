import json
import unittest

from parsenames import toJson
import basictrie as trie

class TestParseNames(unittest.TestCase):
    def test_toJson(self):
        #
        # Test that it converts a list of strings to json of the correct format
        #
        strList = ['cool_apple', 'thatApple', 'cool_orange', 'thatOrange', 'cool_banana', 'cool_kiwi', 'thatKiwi', 'alaska']
        expected = json.dumps({'data': {'cool_': ['cool_apple', 'cool_orange', 'cool_banana', 'cool_kiwi'], 'that': ['thatApple', 'thatOrange', 'thatKiwi'], 'alaska': ['alaska']}})
        self.assertEqual(toJson(strList), expected)

class TestBasicTrie(unittest.TestCase):
    def test_longest_prefix(self):
        root = trie.TrieNode('*')
        trie.add(root, 'cool_runnings')
        trie.add(root, 'cool__runnings')
        trie.add(root, 'cool_')
        trie.add(root, 'fantabulous')
        self.assertEqual(trie.longest_prefix(root, 'cool_runnings'), 'cool_')
        self.assertEqual(trie.longest_prefix(root, 'cool__runnings'), 'cool_')
        self.assertEqual(trie.longest_prefix(root, 'cool_'), 'cool_')
        self.assertEqual(trie.longest_prefix(root, 'coolRunnings'), 'cool')
        self.assertEqual(trie.longest_prefix(root, 'fantabulous'), 'fantabulous')


if __name__ == "__main__":
    unittest.main()
    print("Everything has passed")
