from setuptools import setup, find_packages
from pathlib import Path
import codecs
import os

this_directory = Path(__file__).parent

VERSION = '0.0.4'
DESCRIPTION = 'Python wrapper for Genius API'
long_description = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="geniusdotpy",
    version=VERSION,
    author="jjoeldaniel",
    author_email="<joeldanielrico@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'genius', 'api-wrapper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)