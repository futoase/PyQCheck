#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from _import import PyQCheck, Arbitrary
from decimal import Decimal, getcontext

def run():
  # decimal setting
  getcontext().prec = 60

  start = time.time()

  def is_hiragana(chars):
    result = [ord('\u3040') <= ord(x) <= ord('\u309F') for x in chars]
    return len(set(result)) == 1 and list(set(result))[0] == True

  def ten_or_less(n):
    if n > 10:
      raise ValueError
    return True

  # running test.
  PyQCheck(verbose=False, process=3).add(
    Arbitrary('integer', 'integer', 'integer').property(
      'x + y + z == z + y + x', lambda x, y, z : x + y + z == z + y + x
    )
  ).add(
    Arbitrary('number', 'number', 'number').property(
      'Decimal(x) + Decimal(y) + Decimal(z) ==  Decimal(z) + Decimal(y) + Decimal(x)', lambda x, y, z : Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)
    )
  ).add(
    Arbitrary('hiragana').property(
      'check characters whether hiragana.', is_hiragana
    )
  ).add(
    Arbitrary(
      ('integer', dict(max=20))
    ).property(
      'n <= 10 == True', ten_or_less, ValueError,
    )
  ).run(1000).result()

  end = time.time() - start
  print(('finish: ' + str(end)))

if __name__ == '__main__':
  run()
