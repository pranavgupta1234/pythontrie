import unittest
import os, sys

sys.path.insert(0, os.path.join(os.getcwd(), "../pythontrie/"))

from pythontrie import trie

class TrieBasicTests(unittest.TestCase):

    def test_trie_size_after_insertion(self):
        sample_trie = trie()
        sample_strings = ['heyy', 'heyay', 'heyey', 'hyyy', 'yoyo', 'heeyy', 'hoeyy']
        for sample_string in sample_strings:
            sample_trie.insert(sample_string)
        self.assertEqual(sample_trie.size(), 7)

    def test_trie_size_of_suggestions(self):
        sample_trie = trie()
        sample_strings = ['heyy', 'heyay', 'heyey', 'hyyy', 'yoyo', 'heeyy', 'hoeyy']
        for sample_string in sample_strings:
            sample_trie.insert(sample_string)
        suggested = sample_trie.suggestions(prefix='he')
        self.assertEqual(len(suggested), 4)

    def test_trie_search(self):
        sample_trie = trie()
        sample_strings = ['heyy', 'heyay',]
        for sample_string in sample_strings:
            sample_trie.insert(sample_string)
        self.assertEqual(sample_trie.search("this"), False)