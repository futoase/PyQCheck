# -*- coding:utf-8 -*-

from _import import PyQNumber

describe "PyQNumber Test":
  it "generate random variable.":
    number = PyQNumber().generate()
    assert str(type(number)).find("function")
    assert isinstance(number(), float)

  it "generate random variable by range set.":
    number = PyQNumber().generate(min=1000.0, max=10000.0)
    for i in range(1000):
      assert 1000.0 <= number() <= 10000.0

    number = PyQNumber().generate(min=-10.0, max=0.0)
    for i in range(1000):
      assert -10.0 <= number() <= 0.0

  it "Distributes test.":
    number = PyQNumber().generate()
    result = []

    for i in range(1000):
      result.append(number())

    assert len(set(result)) != 1

