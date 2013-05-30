#!/usr/bin/env python
# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary

def ten_or_less(n):
  if n > 10:
    raise ValueError
  return True

def test():
  PyQCheck(verbose=True).add(
    Arbitrary(('integer', dict(max=30))).property(
      'n <= 10 == True', ten_or_less, ValueError,
    )
  ).run(10).result()

if __name__ == '__main__':
  test()
