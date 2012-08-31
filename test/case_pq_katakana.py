#-*- coding:utf-8 -*-

from _import import PyQKatakana

describe "PyQKatakana Test":
  it "generate random variable.":
    katakana = PyQKatakana().generate()
    assert str(type(katakana)).find("function")
    assert isinstance(katakana(), unicode)

  it "generate random variable of range set.":
    katakana = PyQKatakana().generate(min=1, max=10)
    for i in range(1000):
      assert 1 <= len(katakana()) <= 10

    katakana = PyQKatakana().generate(min=20, max=20)
    for i in range(1000):
      assert len(katakana()) == 20

  it "Distributed test":
    katakana = PyQKatakana().generate()
    result = []
    for i in range(1000):
      result.append(katakana())

    assert len(set(result)) != 1

