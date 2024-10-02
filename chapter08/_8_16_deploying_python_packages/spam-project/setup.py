from setuptools import setup

setup(
    name="spam",  # Package name
    version="0.0",
    packages=["spam"],  # A list of all package directories.
    scripts=["runspam.py"],
)

# To create a source distribution (spam-0.0.tar.gz):
#   python3 setup.py sdist

# To install:
#   python3 -m pip install spam-1.0.tar.gz
