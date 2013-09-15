# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary, ArbitraryAbstraction

class CountryArbitrary(ArbitraryAbstraction):
  COUNTRIES = [
    'JAPAN',
    'GERMANY',
    'USA',
    'UK',
    'AUSTRALIA'
  ]

  def __init__(self):
    pass

  def generate(self):
    '''
    generate of random length array.
    '''
    import random
    return lambda : [random.choice(CountryArbitrary.COUNTRIES) for x in range(10)]

describe "Custom Arbitrary Test":
  it "generate custom arbitrary.":
    arbitrary = CountryArbitrary()
    assert isinstance(arbitrary, CountryArbitrary) == True

  it "arbitrary test run.":
    test_label = "set(x).issubset({'JAPAN', 'GERMANY', 'USA', 'UK', 'AUSTRALIA'}"
    test_func = lambda x: set(x).issubset({'JAPAN', 'GERMANY', 'USA', 'UK', 'AUSTRALIA'})

    label, func_name, func_code, success, failure, exceptions, verbose = (
      Arbitrary(
        CountryArbitrary()
      ).property(
        test_label, test_func
      ).run(1000).test_result
    )

    assert label == test_label
    assert success == 1000
    assert failure == 0
