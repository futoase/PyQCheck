#!/usr/bin/env python
# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary, set_arbitrary

def test():
  PyQCheck().add(
    Arbitrary(
      ('integer', dict(min=10, max=100)), # range of 10 - 100
      ('integer', dict(min=30)), # range of 30 - max of default
    ).property(
      '10 <= x <= 100 and y >= 30', lambda x, y : 10 <= x <= 100 and y >= 30
    )
  )
 
  @set_arbitrary(
    ('string', dict(min=10, max=20)),
    ('integer', dict(max=30)))
  def repeat(chars, n):
    '''
    (chars * n).split(chars) == n + 1
    '''
    repeat_string = chars * n
    return len(repeat_string.split(chars)) == n + 1

  PyQCheck(verbose=True).run(10).result()

if __name__ == '__main__':
  test()
