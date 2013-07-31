#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if sys.version_info < (3, 3, 0):
  sys.stderr.write("PyQCheck is require Python 3.3 or newer.\n")
  sys.exit(-1)

from distutils.core import setup

setup(
  name="PyQCheck",
  version="0.3.1",
  description="PyQCheck is Quick Check-like random testing framework.",
  author="Keiji Matsuzaki",
  author_email="futoase@gmail.com",
  license="MIT License",
  url="https://github.com/futoase/PyQCheck",
  packages=["pyqcheck", "pyqcheck.arbitraries"]
)
