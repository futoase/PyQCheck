# -*- coding:utf-8 -*-

from _import import PyQCheck, Arbitrary

describe "Arbitrary Test":

  before each:
    PyQCheck().clear()

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

  it "should work with the obsolete property method.":
    def eq(x,y):
      return x * y == y * x and x + y == y + x

    test_label1 = '!(x || y) == !x && !y'
    test_func1 = lambda x, y: (not(x or y)) == ((not x) and (not y))
    test_label2 = 'x * y == y * x and x + y == y + x'
    test_func2 = eq
    test_count = 1000

    results = (
      PyQCheck(verbose=False).add(
        Arbitrary('boolean', 'boolean').property(
          test_label1, test_func1
        )
      ).add(
        Arbitrary('integer', 'integer').property(
          test_label2, test_func2
        )
      ).run(test_count).results
    )

    assert results[0].label == test_label1
    assert results[0].success == test_count
    assert results[0].failure == 0
    assert results[1].label == test_label2
    assert results[1].success == test_count
    assert results[1].failure == 0
