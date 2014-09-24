# -*- coding:utf-8 -*-

import sys
from importlib import import_module


class ArbitraryAbstraction(object):
  def __init__(self):
    pass

  def generate(self):
    raise NoImplementedError("Should extends use only this class.")


class Arbitrary(object):
  '''
  Arbitrary is returned specified object.
  '''
  TEST_COUNT = 15

  def __init__(self, *args):
    self.arbitraries = args
    self.test_result = []

  def __get_arbitrary_content(self, arbitrary):
    if isinstance(arbitrary, str):
      module_filename = 'pq_' + arbitrary.lower()
      klass = 'PyQ' + arbitrary.title()
      module = import_module(
        'pyqcheck.arbitraries.' + module_filename
      )
      return getattr(module, klass)()

    if isinstance(arbitrary, ArbitraryAbstraction):
      return arbitrary

  def generate_arbitraries(self):
    arbitraries = []

    for arbitrary in self.arbitraries:
      if isinstance(arbitrary, tuple):
        arbitrary_name = arbitrary[0]
        arbitrary_limit = arbitrary[1]
      else:
        arbitrary_name = arbitrary
        arbitrary_limit = {}

      ar = self.__get_arbitrary_content(arbitrary_name)
      arbitraries.append(ar.generate(**arbitrary_limit))

    return arbitraries
