import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ptrie',
    version='0.1',
    scripts=['ptrie'] ,
    py_modules=["ptrie"],
    author="Pranav Gupta",
    author_email="pranavgupta4321@gmail.com",
    description="General Purpose Trie Data Structure in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranavgupta1234/ptrie",
    packages=setuptools.find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
 )