pythontrie : Python Implementation of Trie Data Structure
==========================

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5cfc11fad54443a3a222fb32f2616988)](https://app.codacy.com/app/pranavgupta1234/pythontrie?utm_source=github.com&utm_medium=referral&utm_content=pranavgupta1234/pythontrie&utm_campaign=Badge_Grade_Dashboard)
[![image](https://travis-ci.org/pranavgupta1234/pythontrie.svg?branch=master)](https://travis-ci.org/pranavgupta1234/pythontrie)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![image](https://img.shields.io/pypi/v/pythontrie.svg?label=pythontrie)](https://pypi.org/project/pythontrie/)
[![image](https://img.shields.io/pypi/pyversions/pythontrie.svg)](https://pypi.org/project/pythontrie/)
[![image](https://img.shields.io/github/issues/pranavgupta1234/pythontrie.svg)](https://github.com/pranavgupta1234/pythontrie/issues)
[![image](https://img.shields.io/github/issues-pr/pranavgupta1234/pythontrie.svg)](https://github.com/pranavgupta1234/pythontrie/pulls)

![image](https://github.com/pranavgupta1234/ptrie/blob/master/img/trie.jpg)

pythontrie includes sweet implementation of our favourite data structure trie in python.

Usage
------

``` {.sourceCode .python}
>>> from pythontrie import trie
>>> sample_trie = trie()
>>> sample_strings = ['heyy', 'heyay', 'heyey', 'hyyy', 'yoyo', 'heeyy', 'hoeyy']
>>> for sample_string in sample_strings:
>>>     sample_trie.insert(sample_string)
```

Then printing suggestions is as simple as:

```{.sourceCode .python}
>>> print(sample_trie.suggestions(prefix='he')
['heyy', heyay', heyey', 'heeyy']

```

Current Features
---------------

-  Adding arbitrary strings into trie
-  Searching for suggestion using prefix
-  Search whether any string is present in trie or not

pythontrie right now supports all python versions

Installation
------------

To install pythontrie, simply use all time favorite pip and type :

``` {.sourceCode .bash}
$ pip install pythontrie
✨🍰✨
```

Documentation
-------------
Coming Soon.

How to Contribute
-----------------

1.  Initial plan is to integrate all necessary functionality that trie can offer into this library so that it can act as 
    one place shot for everyone who is playing with trie.
2.  Please propose and feel free to raise an issue and submit a PR for some sensible feature. Try to elaborate the
    the area where this feature would be applicable so that all of us can be enlightened :).
3.  I am planning to integrate research work done on tries into this library as well so that it can provide advanced functionalities
    with tight algorithmic complexity bounds. Please feel free to share any paper.