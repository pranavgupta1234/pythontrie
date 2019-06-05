import sys
from ptrie.trie import trie

if __name__ == '__main__':

    for p in sys.path:
        print(p)

    sample_trie = trie()

    sample_strings = ['heyy', 'heyay', 'heyey', 'hyyy', 'yoyo', 'heeyy', 'hoeyy']

    for sample_string in sample_strings:
        sample_trie.insert(sample_string)

    print(sample_trie.suggestions(prefix='he'))

    print(sample_trie.size())


