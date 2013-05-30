# -*- coding:utf-8 -*-

import types
import marshal

from _import import PyQCheck, Arbitrary

describe "Arbitrary Test":

  before each:
    PyQCheck.TEST_STACK = []

  it "generate arbitrary instance.":
    arbitrary = Arbitrary('number', 'number')
    assert isinstance(arbitrary, Arbitrary) == True

  it "generate random variable.":
    gen_arbitraries = Arbitrary('number', 'string').generate_arbitraries()

    assert len(gen_arbitraries) == 2
    assert str(type(gen_arbitraries[0])).find("function") != -1
    assert str(type(gen_arbitraries[1])).find("function") != -1
    assert isinstance(gen_arbitraries[0](), float)
    assert isinstance(gen_arbitraries[1](), str)

  it "arbitrary test run.":
    test_label = 'x + y == y + x'
    test_func = lambda x, y : x + y == y + x

    label, func_name, func_code, success, failure, exceptions, verbose = (
      Arbitrary(
        ('number', dict(min=5, max=10)), 
        ('number', dict(min=5, max=10))
      ).property(
        test_label, test_func
      ).run(1000).test_result
    )

    assert label == test_label
    assert success == 1000
    assert failure == 0

  it "arbitrary Exception test.":
    TEST_COUNT = 100

    class LengthOverError(Exception):
      pass

    def length_check(x):
      if len(x) > 10:
        raise LengthOverError("Length over!")
      else:
        return x

    label, func_name, func_code, success, failure, exceptions, verbose = (
      Arbitrary(
        ('string', dict(min=11, max=40))
      ).property(
        'len(x) > 10', length_check, LengthOverError,
      ).run(TEST_COUNT).test_result
    )
    assert exceptions.get("LengthOverError") is not None

  it "check result type test.":
    TEST_COUNT = 100

    def return_tuple(string):
      return tuple(string)

    label, func_name, func_code, success, failure, exceptions, verbose = (
      Arbitrary(
        ('string', dict(min=10))
      ).property(
        'return result type is tuple', return_tuple, type=tuple
      ).run(TEST_COUNT).test_result
    )

    assert success == TEST_COUNT
