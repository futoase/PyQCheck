# -*- coding:utf-8 -*-

import random
import sys

class PyQInteger(object):
  '''
  PyQInteger class is returned random integer.
  '''

  def __init__(self):
    pass

  def generate(self, min=1, max=None):
    '''
    generate of random integer.
    '''
    min = min if isinstance(min, int) else 1
    max = max if max is not None and isinstance(max, int) else sys.maxsize
    return lambda : random.randint(min, max)
