# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary, Prop, PropRunner

describe "Prop Test":

  before each:
    PyQCheck.TEST_STACK = []

  it "should succeed all tests when Prop shows true.":
    test_label = 'x + y == y + x'
    test_func = lambda x, y: x + y == y + x

    result = (
      PropRunner(1000).run(
        Prop(
          Arbitrary(
            ('number', {"min":5, "max":10}),
            ('number', {"min":5, "max":10})
          ),
          test_func, test_label
        )
      ).test_result
    )

    assert result.label == test_label
    assert result.success == 1000
    assert result.failure == 0

  it "should be able to catch errors.":
    test_label = 'n <= 10 == True'
    test_number = 1000
    def ten_or_less(n):
      if n > 10:
        raise ValueError
      return True

    result = (
      PropRunner(test_number).run(
        Prop(
          Arbitrary(('integer', {"max":30})),
          ten_or_less, test_label, ValueError
        )
      ).test_result
    )

    assert result.label == test_label
    assert result.success == test_number or not (result.exceptions.get("ValueError") is None)

  it "should check a given result type.":
    TEST_COUNT = 100

    def return_tuple(string):
      return tuple(string)

    result = (
      PropRunner(TEST_COUNT).run(
        Prop(
          Arbitrary(
            ('string', {"min":10})
          ),
          return_tuple, 'return result type is tuple', type=tuple
        )
      ).test_result
    )

    assert result.success == TEST_COUNT
