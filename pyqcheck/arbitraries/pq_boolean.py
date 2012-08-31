# -*- coding:utf-8 -*-

import random

class PyQBoolean(object):
  '''
  PyQBoolean class is returned True or False
  '''

  def __init__(self):
    pass

  def generate(self):
    '''
    generated of True or False
    '''
    return lambda : random.choice([True, False])
