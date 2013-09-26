# -*- coding:utf-8 -*-

from unittest import TestCase

from _import import PyQCheck, Arbitrary

def get_result(property_result, encoding=None):
  if encoding is None:
    arb = Arbitrary(
            'integer',
            'integer'
          )
  else:
    arb = Arbitrary(
            'integer',
            'integer',
            _encoding=encoding
          )
  arb = arb.property('test', lambda x, y: property_result)

  return PyQCheck(verbose=True).add(arb).run(10).results

def setUp(klass):
  def setUp(self):
    PyQCheck().clear()
  klass.setUp = setUp
  return klass


@setUp
class TestGivenEncodingIsCP932(TestCase):
  def test_WhenRunArbitrarySuccessfullyThenShowSuccess(self):
    results = get_result(True, 'cp932')
   
    assert len(results) != 0
    for result in results:
      assert len(result.verbose) != 0
      for v in result.verbose:
        assert v.startswith('success')
   
  def test_WhenRunArbitraryWithFailureThenShowFailure(self):
    results = get_result(False, 'cp932')
   
    assert len(results) != 0
    for result in results:
      assert len(result.verbose) != 0
      for v in result.verbose:
        assert v.startswith('failure')

@setUp
class TestGivenEncodingIsUTF8(TestCase):
  def test_WhenRunArbitrarySuccessfullyThenShowCharacter0x2600(self):
    results = get_result(True)
   
    assert len(results) != 0
    for result in results:
      assert len(result.verbose) != 0
      for v in result.verbose:
        assert v[0] == '\u2600'

  def test_WhenRunArbitraryWithFailureThenShowCharacter0x2601(self):
    results = get_result(False)
   
    assert len(results) != 0
    for result in results:
      assert len(result.verbose) != 0
      for v in result.verbose:
        assert v[0] == '\u2601'
