# -*- coding:utf-8 -*-

from _import import PyQMomoclo

import datetime

describe "PyQMomoclo test":
  it "generate momoclo variable.":
    momoclo = PyQMomoclo().generate()
    assert str(type(momoclo)).find("function")
    assert isinstance(momoclo(), dict)

  it "random member test by current member.":
    momoclo = PyQMomoclo().generate()
    member_names = [
      "Kanako Momota",
      "Shiori Tamai",
      "Ayaka Sasaki",
      "Momoka Ariyasu",
      "Reni Takagi"
    ]
    for i in range(1000):
      assert momoclo().get("name") in member_names

  it "random member test by all member.":
    momoclo = PyQMomoclo().generate()
    all_member_names = [
      "Kanako Momota",
      "Shiori Tamai",
      "Ayaka Sasaki",
      "Momoka Ariyasu",
      "Reni Takagi",
      "Tsukina Takai",
      "Miyuu Wagawa",
      "Manami Ikura",
      "Sumire Fujishiro",
      "Yukina Kashiwa",
      "Akari Hayami"
    ]
    for i in range(1000):
      assert momoclo().get("name") in all_member_names

