# -*- coding:utf-8 -*-

from _import import PyQInteger

describe "PyQInteger Test":
  it "generate random variable.":
    integer = PyQInteger().generate()
    assert str(type(integer)).find("function")
    assert isinstance(integer(), int)

  it "generate random variable by range set.":
    integer = PyQInteger().generate(max=1000)
    for i in range(1000):
      assert integer() <= 1000

    integer = PyQInteger().generate(min=-10, max=0)
    for i in range(1000):
      assert -10 <= integer() <= 0

  it "Distributed test":
    integer = PyQInteger().generate()
    result = []
    for i in range(1000):
      result.append(integer())

    assert len(set(result)) != 1
