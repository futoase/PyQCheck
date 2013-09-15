# -*- coding:utf-8 -*-

import os
import sys

INCLUDE_PATH = os.path.abspath(os.path.abspath(os.path.dirname(__file__)) + '/../')

if not INCLUDE_PATH in sys.path:
  sys.path.insert(0, INCLUDE_PATH)

from pyqcheck import PyQCheck, Arbitrary, set_arbitrary

