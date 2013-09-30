# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary, ArbitraryResultSymbol

describe "With emoji":

  before each:
    ArbitraryResultSymbol.WITH_EMOJI = True
    PyQCheck().clear()

  it "should be result is always success":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways true', lambda x: True
      )
    ).run(10).results

    for result in results:
      for v in result.verbose:
        assert v.startswith(u'\u2600')

  it "should be result is always failure":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways false', lambda x: False
      )
    ).run(10).results

    for result in results:
      for v in result.verbose:
        assert v.startswith(u'\u2601')

  it "should be result is always throw error":

    class CustomError(BaseException):
      pass

    def throw_exception(n):
      raise CustomError("Error!")

    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways true', throw_exception, CustomError
      )
    ).run(10).results

    for result in results:
      for v in result.verbose:
        assert v.startswith(u'\u2603')

describe "Without emoji":

  before each:
    ArbitraryResultSymbol.WITH_EMOJI = False
    PyQCheck().clear()

  it "should be result is always success":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways true', lambda x: True
      )
    ).run(10).results

    for result in results:
      for v in result.verbose:
        assert v.startswith('success')

  it "should be result is always failure":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways false', lambda x: False
      )
    ).run(10).results

    for result in results:
      for v in result.verbose:
        assert v.startswith('failure')

  it "should be result is always throw error":

    class CustomError(BaseException):
      pass

    def throw_exception(n):
      raise CustomError("Error!")

    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways true', throw_exception, CustomError
      )
    ).run(10).results

    for result in results:
      for v in result.verbose:
        assert v.startswith('error  ')
