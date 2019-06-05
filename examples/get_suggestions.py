import os, sys

sys.path.insert(0, os.path.join(os.getcwd(), "../pythontrie/"))

from pythontrie.trie import trie

if __name__ == '__main__':

    sample_trie = trie()

    sample_strings = ['heyy', 'heyay', 'heyey', 'hyyy', 'yoyo', 'heeyy', 'hoeyy']

    for sample_string in sample_strings:
        sample_trie.insert(sample_string)

    print(sample_trie.suggestions(prefix='he'))

    print(sample_trie.size())


