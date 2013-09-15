#-*- coding:utf-8 -*-

from _import import PyQString

describe "PyQString Test":
  it "generate random variable.":
    string = PyQString().generate()
    assert str(type(string)).find("function")
    assert isinstance(string(), str)

  it "generate random variable of range set.":
    string = PyQString().generate(min=20, max=20)
    for i in range(1000):
      assert len(string()) <=20

    string = PyQString().generate(min=10, max=30)
    for i in range(1000):
      assert 10 <= len(string()) <= 30

  it "Distribute test":
    string = PyQString().generate()
    result = []
    for i in range(1000):
      result.append(string())

    assert len(set(result)) != 1
