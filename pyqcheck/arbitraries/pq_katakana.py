# -*- coding:utf-8 -*-

import random

class PyQKatakana(object):
  '''
  PyQKatakana of returned random katakana charactors.
  unicode range is 30A0-30FF
  '''
  KATAKANA_RANGE = list(range(int("30A0", 16), int("30FF", 16) + 1))

  def __init__(self):
    pass

  def generate(self, func=None, min=0, max=20):
    '''
    generate of Katakana strings.
    '''
    min = min if isinstance(min, int) and min > 0 else 1
    max = max if isinstance(max, int) and max > 0 else 20

    random_length = random.randint(min,max)
    return (
        lambda : ''.join([chr(random.choice(PyQKatakana.KATAKANA_RANGE))
                 for x in range(random_length)]))
