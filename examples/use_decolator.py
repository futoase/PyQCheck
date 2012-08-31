#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from _import import PyQCheck, set_arbitrary
from decimal import Decimal, getcontext

def run():
  # decimal setting
  getcontext().prec = 60

  start = time.time()

  @set_arbitrary('integer', 'integer', 'integer')
  def equal(x, y, z):
    '''
    x + y + z == z + y + x
    '''
    return x + y + z == z + y + x

  @set_arbitrary('number', 'number', 'number')
  def equal_use_decimal(x, y, z):
    '''
    Decimal(x) + Decimal(y) + Decimal(z) ==  Decimal(z) + Decimal(y) + Decimal(x)
    '''
    return Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)

  @set_arbitrary('hiragana')
  def is_hiragana(chars):
    '''
    check characters whether hiragana.
    '''
    result = map(lambda x : ord(u'\u3040') <= ord(x) <= ord(u'\u309F'), chars)
    return len(set(result)) == 1 and list(set(result))[0] == True

  @set_arbitrary(('integer', dict(max=20)), exceptions=(ValueError,))
  def lower_10(n):
    '''
    n <= 10 == True
    '''
    if n > 10:
      raise ValueError
    return True

  # running test.
  PyQCheck(verbose=False).run(1000).result()

  end = time.time() - start
  print('finish: ' + str(end))

if __name__ == '__main__':
  run()
