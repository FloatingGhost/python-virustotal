#!/usr/bin/env python3

from setuptools import *
from vt import __version__ as v
setup(
  name="vtapi",
  version=v,
  author="Hannah Ward",
  author_email="hannah.ward9001@gmail.com",
  packages = find_packages(),
  install_requires = ["requests>=2.9.1"],
)
