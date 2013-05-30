# -*- coding:utf-8 -*-

import random

class PyQHiragana(object):
  '''
  PyQHiragana of returned random hiragana charactors.
  unicode range is 3040-309F
  '''
  HIRAGANA_RANGE = list(range(int("3040", 16), int("309F", 16) + 1))

  def __init__(self):
    pass

  def generate(self, min=1, max=20):
    '''
    generate of Hiragana strings.
    '''
    min = min if isinstance(min, int) and min > 0 else 1
    max = max if isinstance(max, int) and max > 0 else 20
    range_length = random.randint(min, max)
    return (
        lambda : ''.join([chr(random.choice(PyQHiragana.HIRAGANA_RANGE))
                 for x in range(range_length)]))
