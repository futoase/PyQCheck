# -*- coding:utf-8 -*-

import sys
import io
from _import import PyQCheck, Arbitrary, PrettyPrinter

describe "With emoji":

  before each:
    PyQCheck().clear()

  it "should be result is always success":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways true', lambda x: True
      )
    ).run(10).results

    printer = PrettyPrinter(True, True)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
        assert v.startswith(u'\u2600')

  it "should be result is always failure":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways false', lambda x: False
      )
    ).run(10).results

    printer = PrettyPrinter(True, True)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
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

    printer = PrettyPrinter(True, True)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
        assert v.startswith(u'\u2603')

describe "Without emoji":

  before each:
    PyQCheck().clear()

  it "should be result is always success":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways true', lambda x: True
      )
    ).run(10).results

    printer = PrettyPrinter(True, False)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
        assert v.startswith('success')

  it "should be result is always failure":
    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'allways false', lambda x: False
      )
    ).run(10).results

    printer = PrettyPrinter(True, False)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
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

    printer = PrettyPrinter(True, False)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
        assert v.startswith('error  ')

describe "Find encoding":

  before each:
    PyQCheck().clear()

  it "should print emoji":

    results = PyQCheck(verbose=True).add(
      Arbitrary('integer').property(
        'always true', lambda x: True
      )
    ).run(10).results

    printer = PrettyPrinter(True, True)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
        assert v.startswith(u'\u2600')

  it "should not print emoji":
    stdout = sys.stdout
    try:
      buffer = io.FileIO(0, mode='wb')
      sys.stdout = io.TextIOWrapper(buffer, encoding='cp932')

      results = PyQCheck(verbose=True).add(
        Arbitrary('integer').property(
          'always true', lambda x: True
        )
      ).run(10).results
    finally:
      sys.stdout = stdout

    printer = PrettyPrinter(True, False)
    for result in results:
      for v in printer.to_verbose_string(result.prop_results):
        assert v.startswith('success')
