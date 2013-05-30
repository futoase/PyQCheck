# -*- coding:utf-8 -*-

import random
import string

class PyQString(object):
  '''
  This String class is returend random character by letters and digits.
  '''

  def __init__(self):
    pass

  def generate(self, min=1, max=500):
    '''
    generate of random characters.
    '''
    min = min if min > 0 else 1
    max = max if max > 0 else 500

    return (lambda : ''.join([
      random.choice(string.ascii_letters + string.digits) for x in range(random.randint(min, max))
     ]))
