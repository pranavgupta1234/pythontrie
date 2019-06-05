ptrie : Python Implementation of Trie Data Structure
==========================

![image](https://github.com/pranavgupta1234/ptrie/blob/master/img/trie.jpg)

ptrie includes sweet pythonic implementation of our favourite data structure trie.

Use ptrie as:

``` {.sourceCode .python}
>>> import ptrie
>>> sample_trie = trie()
>>> sample_strings = ['heyy', 'heyay', 'heyey', 'hyyy', 'yoyo', 'heeyy', 'hoeyy']
>>> for sample_string in sample_strings:
>>>     sample_trie.insert(sample_string)
>>> print(sample_trie.suggestions(prefix='he')
['heyy', heyay', heyey', 'heeyy']

```


Current Features
---------------

- Adding arbitrary strings into trie
- Searching for suggestion using prefix
- Search whether any string is present in trie or not

ptrie right now supports 3.4–3.7, and runs great on PyPy.

Installation
------------

To install ptrie, simply use all time fav pip and type :

``` {.sourceCode .bash}
$ pip install ptrie
✨🍰✨
```

Documentation
-------------
Coming Soon.


How to Contribute
-----------------

1.  Initial plan to to integrate all necessary functionality that trie can offer into this library so that it can act as 
    one place shot for everyone who is playing with trie.
2.  Please propose and feel free to raise and issue and then submit a PR for some sensible feature. Try to elaborate the
    implementational area where this feature would be applicable so that all of us can be enlightened :).
3.  I am planning to integrate research work done into this library as well so that it can provide advanced functionalities
    with tight algorithmic complexity bounds. Please feel free to share any paper.