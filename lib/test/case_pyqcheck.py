# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary, set_arbitrary
from decimal import Decimal, getcontext

getcontext().prec = 60

describe "PyQCheck Test":
  before each:
    PyQCheck().clear()

  it "later run.":
    PyQCheck().add(
      Arbitrary(
        ('string', dict(min=10, max=1000)),
        ('integer', dict(max=30))
      ).property(
        'len(x * y) == len(x) * y',
        lambda x, y: len(x * y) == len(x) * y
      )
    )

    @set_arbitrary(
      ('number', dict(max=100.5)), ('integer', dict(min=3)))
    def identical(x, y):
      '''
      x * y == y * x
      '''
      return x * y == y * x

    results = PyQCheck().run(100).results

    test_1 = results[0]
    test_2 = results[1]

    assert test_1.label == 'len(x * y) == len(x) * y'
    assert test_2.label == 'x * y == y * x'


  it "register of three test by linear.":
    TEST_COUNT = 100

    results = PyQCheck().add(
      Arbitrary(
        ('integer', dict(max=10)), 
        ('integer', dict(min=30)),
        'integer'
      ).property(
        'x + y + z == z + y + x', 
        lambda x, y, z : x + y + z == z + y + x
      )
    ).add(
      Arbitrary(
        'number', 
        ('number', dict(min=0.5, max=100.3)),
        ('number', dict(max=130.3))
      ).property(
        'Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)',
        lambda x, y, z : Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)
      )
    ).add(
      Arbitrary(
        ('string', dict(max=10))
      ).property(
        'len(chars) <= 10',
        lambda chars : len(chars) <= 10
      )
    ).run(TEST_COUNT).results

    assert len(results) == 3

    test_1 = results[0] # x + y + z == z + y + x
    test_2 = results[1] # x + y + z == z + y + x (decimal)
    test_3 = results[2] # len(chars) <= 10

    assert test_1.label == 'x + y + z == z + y + x'
    assert test_1.success == TEST_COUNT
    assert test_1.failure == 0
    assert test_2.label == 'Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)'
    assert test_2.success == TEST_COUNT
    assert test_2.failure == 0
    assert test_3.label == 'len(chars) <= 10'
    assert test_3.success == TEST_COUNT
    assert test_3.failure == 0

  it "register of three test by decorator.":
    TEST_COUNT = 100

    @set_arbitrary('integer', 'integer', 'integer')
    def equals(x, y, z):
      '''
      x + y + z == z + y + x
      '''
      return x + y + z == z + y + x

    @set_arbitrary('number', 'number', 'number')
    def equals_use_decimal(x, y, z):
      '''
      Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)
      '''
      return Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)

    @set_arbitrary(('string', dict(max=10)))
    def length_10(chars):
      '''
      len(chars) <= 10
      '''
      return len(chars) <= 10

    results = PyQCheck().run(TEST_COUNT).results

    test_1 = results[0]
    test_2 = results[1]
    test_3 = results[2]

    assert test_1.label == 'x + y + z == z + y + x'
    assert test_1.success == TEST_COUNT
    assert test_1.failure == 0
    assert test_2.label == 'Decimal(x) + Decimal(y) + Decimal(z) == Decimal(z) + Decimal(y) + Decimal(x)'
    assert test_2.success == TEST_COUNT
    assert test_2.failure == 0
    assert test_3.label == 'len(chars) <= 10'
    assert test_3.success == TEST_COUNT
    assert test_3.failure == 0
