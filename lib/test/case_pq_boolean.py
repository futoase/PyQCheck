# -*- coding:utf-8 -*-

from _import import PyQBoolean

describe "PyQBoolean Test":
  it "generate random variable.":
    boolean = PyQBoolean().generate()
    assert str(type(boolean)).find("function")
    assert isinstance(boolean(), bool)

  it "Distributed test":
    boolean = PyQBoolean().generate()
    result = []
    for i in range(1000):
      result.append(boolean())

    assert False in set(result)
    assert True in set(result)

