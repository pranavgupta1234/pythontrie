import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pythontrie',
    version='0.3',
    author="Pranav Gupta",
    author_email="pranavgupta4321@gmail.com",
    description="General Purpose Trie Data Structure in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranavgupta1234/pythontrie",
    license="Apache Software License",
    packages=["pythontrie"],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
 )