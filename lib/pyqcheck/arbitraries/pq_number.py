# -*- coding:utf-8 -*-

import random

class PyQNumber(object):
  '''
  PyQNumber class is returned random numbers.
  '''

  def __init__(self):
    pass

  def generate(self, func=None, min=0.0, max=100.0):
    '''
    generate of random numbers.
    '''
    min = min if isinstance(min, float) else 0.0
    max = max if isinstance(max, float) else 100.0
    return lambda : random.uniform(min, max)
