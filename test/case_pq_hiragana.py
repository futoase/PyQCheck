#-*- coding:utf-8 -*-

from _import import PyQHiragana

describe "PyQHiragana Test":
  it "generate random variable.":
    hiragana = PyQHiragana().generate()
    assert str(type(hiragana)).find('function')
    assert isinstance(hiragana(), unicode)

  it "generate random variable of range set.":
    hiragana = PyQHiragana().generate(min=1, max=10)
    for i in range(1000):
      assert 1 <= len(hiragana()) <= 10

    hiragana = PyQHiragana().generate(min=20, max=20)
    for i in range(1000):
      assert len(hiragana()) == 20

    hiragana = PyQHiragana().generate(max=20)
    for i in range(1000):
      assert len(hiragana()) <= 20

  it "Distributed test":
    hiragana = PyQHiragana().generate()
    result = []
    for i in range(1000):
      result.append(hiragana())

    assert len(set(result)) != 1

