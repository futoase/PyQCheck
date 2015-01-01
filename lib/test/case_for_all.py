# -*- coding: utf-8 -*-

from _import import PyQCheck, Arbitrary, for_all, may_throw, PropRunner


describe "for_all test":

  before each:
    PyQCheck.TEST_STACK = []

  it "should succeed all tests when for_all creates an all true property":
    test_label = '!(x || y) == !x && !y'
    test_func = lambda x, y: (not(x or y)) == ((not x) and (not y))

    result = (
      PropRunner(1000).run(
        for_all(
          ('boolean', 'boolean'),
          test_label,
          test_func
        )
      ).test_result
    )

    assert result.label == test_label
    assert result.success == 1000
    assert result.failure == 0

  it "should succeed all tests when for_all creates an all true property with limitations":
    test_label = 'x + y == y + x'
    test_func = lambda x, y: x + y == y + x

    result = (
      PropRunner(1000).run(
        for_all(
          (('number', {"min":5, "max":10}), ('number', {"min":5, "max":10})),
          test_label,
          test_func
        )
      ).test_result
    )

    assert result.label == test_label
    assert result.success == 1000
    assert result.failure == 0

  it "should catch errors when for_all creates a fragile property":
    test_label = 'n <= 10 == True'
    test_number = 1000
    def ten_or_less(n):
      if n > 10:
        raise ValueError
      return True

    result = (
      PropRunner(test_number).run(
        for_all(
          (('integer', {"max":30}),),
          test_label,
          may_throw(ten_or_less, ValueError)
        )
      ).test_result
    )

    assert result.label == test_label
    assert result.success == test_number or not (result.exceptions.get("ValueError") is None)
