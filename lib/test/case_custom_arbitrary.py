# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary, ArbitraryAbstraction, Prop, PropRunner

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

    result = (
      PropRunner(1000).run(
        Prop(
          Arbitrary(
            CountryArbitrary()
          ),
          test_func, test_label
        )
      ).test_result
    )

    assert result.label == test_label
    assert result.success == 1000
    assert result.failure == 0
